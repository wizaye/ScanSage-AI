import os
import requests
import chainlit as cl
import asyncio
import base64
from typing import List
import io
from PIL import Image

# Configuration
API_URL = "http://localhost:8000/api/chat"  # Your updated chat endpoint


@cl.on_chat_resume
async def on_chat_resume(thread):
    pass


@cl.password_auth_callback
def auth_callback(username: str, password: str):
    if (username, password) == ("admin", "admin"):
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None


@cl.step(type="tool", name=" Medical Analysis Tool")
async def analyze_medical_data(user_message, image_files=None):
    try:
        # Prepare the request data
        data = {"message": user_message}
        files = {}

        # Add images to the request if provided
        if image_files:
            for i, (image_path, image_filename) in enumerate(image_files):
                with open(image_path, "rb") as f:
                    image_data = f.read()
                files[f"images"] = (image_filename, image_data, "image/jpeg")

        # Make the API request
        response = requests.post(API_URL, data=data, files=files)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error from analysis service: {response.text}"}
    except Exception as e:
        return {"error": f"Error processing your request: {str(e)}"}


def base64_to_image(base64_string, output_path):
    """Convert a base64 string to an image file and save it"""
    try:
        image_data = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(image_data))
        image.save(output_path)
        return output_path
    except Exception as e:
        print(f"Error converting base64 to image: {str(e)}")
        return None


@cl.on_message
async def on_message(message: cl.Message):
    user_message = message.content
    image_files = []

    # Check if there are any images uploaded
    if message.elements:
        for element in message.elements:
            if isinstance(element, cl.Image):
                image_path = element.path
                image_filename = os.path.basename(image_path)
                image_files.append((image_path, image_filename))

    # Run the analysis
    result = await analyze_medical_data(user_message, image_files if image_files else None)

    if "error" in result:
        await cl.Message(content=result["error"]).send()
        return

    # Display the text response with typing animation
    if "message" in result and result["message"]:
        response_msg = cl.Message(content="")

        # Stream the message with typing animation
        words = result["message"].split()
        for word in words:
            await response_msg.stream_token(word + " ")
            await asyncio.sleep(0.02)  # Adjust for desired typing speed

        await response_msg.send()

    # Process and display image analysis results
    if "image_analysis" in result and result["image_analysis"]:
        for img_analysis in result["image_analysis"]:
            filename = img_analysis.get("filename", "Unknown")

            if "error" in img_analysis:
                await cl.Message(content=f"Error analyzing image: {img_analysis['error']}").send()
                continue

            analysis = img_analysis.get("analysis", {})
            llm_analysis = analysis.get("llm_analysis", {})
            tumor_prediction = analysis.get("tumor_prediction", {})

            # Create analysis message with typing animation
            analysis_msg = cl.Message(content="")

            # Add LLM analysis sections
            if llm_analysis:
                sections = [
                    ("Scan Analysis", ""),
                    ("Scan Type", llm_analysis.get('scan_type', 'N/A')),
                    ("Organ", llm_analysis.get('organ', 'N/A')),
                    ("Tumor Type", llm_analysis.get('tumor_type', 'N/A')),
                    ("Tumor Subclass", llm_analysis.get('tumor_subclass', 'N/A')),
                    ("Detailed Description", llm_analysis.get('detailed_description', 'N/A')),
                    ("Possible Causes", llm_analysis.get('possible_causes', 'N/A')),
                    ("Clinical Insights", llm_analysis.get('clinical_insights', 'N/A'))
                ]

                for title, content in sections:
                    if title == "Scan Analysis":
                        await analysis_msg.stream_token(f"### {title}\n\n")
                    else:
                        await analysis_msg.stream_token(f"**{title}**: ")

                    if content:
                        words = content.split()
                        for word in words:
                            await analysis_msg.stream_token(word + " ")
                            await asyncio.sleep(0.01)  # Faster typing for smoother experience

                    await analysis_msg.stream_token("\n\n")
                    await asyncio.sleep(0.1)  # Small pause between sections

            # Add tumor prediction with typing animation
            if tumor_prediction:
                await analysis_msg.stream_token("### AI Model Prediction\n\n")

                prediction_sections = [
                    ("Predicted Class", tumor_prediction.get('predicted_class', 'N/A')),
                    ("Confidence Level", str(tumor_prediction.get('confidence_level', 'N/A'))),
                    ("Prediction Status", tumor_prediction.get('prediction_status', 'N/A'))
                ]

                for title, content in prediction_sections:
                    await analysis_msg.stream_token(f"**{title}**: {content}\n")
                    await asyncio.sleep(0.1)

            # Send the analysis text
            await analysis_msg.send()

            # Process and display heatmap and ROI images if available
            elements = []

            # Original image (if we have it)
            if image_files:
                for path, fname in image_files:
                    if fname == filename:
                        elements.append(cl.Image(path=path, name="Original Scan"))
                        break

            # Heatmap image
            if "heatmap" in analysis and analysis["heatmap"]:
                heatmap_path = f"temp_heatmap_{filename}.png"
                if base64_to_image(analysis["heatmap"], heatmap_path):
                    elements.append(cl.Image(path=heatmap_path, name="Heatmap"))

            # ROI image
            if "roi" in analysis and analysis["roi"]:
                roi_path = f"temp_roi_{filename}.png"
                if base64_to_image(analysis["roi"], roi_path):
                    elements.append(cl.Image(path=roi_path, name="Region of Interest"))

            # Send the images if we have any
            if elements:
                await cl.Message(content="### Visualization", elements=elements).send()


if __name__ == "__main__":
    print("Starting Chainlit app - use 'chainlit run app.py' to start the server")
