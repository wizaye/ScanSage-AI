from fastapi import FastAPI
from chainlit.utils import mount_chainlit
import uvicorn

app = FastAPI(
    title="ScanSage AI",
    description="An AI-powered application for analyzing MRI scans and providing detailed medical insights",
    version="1.0.0"
)

@app.get("/app")
def read_main():
    return {"message": "Hello World from ScanSage AI"}

mount_chainlit(app=app, target="./components/chainlit_app.py", path="/chainlit")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)