# 🧠 ScanSage AI

<div align="center">

**AI-Powered Medical Imaging Analysis Platform**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.18-orange.svg)](https://www.tensorflow.org/)
[![Chainlit](https://img.shields.io/badge/Chainlit-2.4+-purple.svg)](https://docs.chainlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*An intelligent assistant for medical scan analysis using deep learning and large language models*

[Features](#-features) • [Architecture](#-architecture) • [Installation](#-quick-start) • [Documentation](#-documentation) • [Demo](#-demo)

</div>

---

## 📖 About

**ScanSage AI** is an advanced medical imaging analysis platform that combines deep learning classification models with state-of-the-art large language models to provide comprehensive insights into medical scans. The system specializes in analyzing MRI, CT, and X-ray images for brain, lung, and breast tumor detection, while offering an intuitive conversational interface for healthcare professionals and researchers.

### 🎯 Key Highlights

- **Multi-Modal AI Analysis**: Combines computer vision (CNN models) with natural language processing (Google Gemini 1.5 Pro)
- **Real-Time Tumor Detection**: Specialized models for brain, lung, and breast cancer detection
- **Intelligent Visualization**: Automated heatmap generation and Region of Interest (ROI) extraction
- **Conversational Interface**: Interactive chat-based UI built with Chainlit for natural interaction
- **Production-Ready**: FastAPI backend with async processing, caching, and Docker support
- **Persistent Chat History**: PostgreSQL-backed conversation storage with cloud file integration

---

## ✨ Features

### 🔍 Medical Image Analysis
- **Automated Scan Classification**: Identifies scan type (MRI, CT, X-ray) and organ system
- **Tumor Detection**: Deep learning models for detecting tumors in brain, lung, and breast scans
- **Confidence Scoring**: Provides confidence levels for all predictions
- **Heatmap Visualization**: Highlights areas of clinical interest using gradient-based attention

### 🤖 AI-Powered Insights
- **Natural Language Queries**: Ask questions about medical scans in plain language
- **Contextual Analysis**: Combines visual and textual information for comprehensive insights
- **Multi-Image Support**: Analyze multiple scans simultaneously
- **Detailed Reporting**: Generates structured medical imaging reports

### 🚀 Technical Features
- **Asynchronous Processing**: High-performance async image processing pipeline
- **SHA-256 Caching**: Intelligent caching system to avoid redundant computations
- **RESTful API**: Well-documented FastAPI endpoints for easy integration
- **User Authentication**: Secure login system with chat history persistence
- **Cloud Storage Integration**: Support for AWS S3, Azure Blob Storage, and Google Cloud Storage
- **Docker Support**: Containerized deployment for both development and production

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        ScanSage AI Platform                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────┐         ┌──────────────────┐              │
│  │   Frontend UI    │◄───────►│   Backend API    │              │
│  │    (Chainlit)    │  HTTP   │    (FastAPI)     │              │
│  └────────┬─────────┘         └────────┬─────────┘              │
│           │                            │                        │
│           │                            │                        │
│  ┌────────▼─────────┐         ┌────────▼─────────┐              │ 
│  │   Data Layer     │         │  AI/ML Services  │              │
│  │  (PostgreSQL)    │         │  ┌─────────────┐ │              │
│  │  Cloud Storage   │         │  │ CNN Models  │ │              │
│  └──────────────────┘         │  │ Gemini API  │ │              │
│                               │  │ OpenCV      │ │              │
│                               │  └─────────────┘ │              │
│                               └──────────────────┘              │
└─────────────────────────────────────────────────────────────────┘
```

### Technology Stack

**Backend**
- **Framework**: FastAPI (Python 3.8+)
- **AI/ML**: TensorFlow/Keras 2.18, Google Generative AI (Gemini 1.5 Pro)
- **Image Processing**: OpenCV, NumPy, Pillow
- **Server**: Uvicorn (ASGI)

**Frontend**
- **Framework**: Chainlit 2.4+
- **Database**: PostgreSQL (via SQLAlchemy, Prisma)
- **Storage**: AWS S3 / Azure Blob / Google Cloud Storage
- **Authentication**: JWT-based authentication

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- PostgreSQL 12+ (for frontend data layer)
- Docker (optional, for containerized deployment)
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/wizaye/ScanSage-AI.git
   cd ScanSage-AI
   ```

2. **Set up Backend**
   ```bash
   cd ScanSage_Backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
   # Create .env file
   echo "GENAI_API_KEY=your_google_gemini_api_key" > .env
   
   # Start the backend server
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Set up Frontend**
   ```bash
   cd ../ScanSage_Frontend/ScanSage_UI
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
   # Configure environment variables (see Frontend docs)
   # Start the frontend
   python main.py
   ```

4. **Access the Application**
   - Backend API: `http://localhost:8000`
   - Frontend UI: `http://localhost:3000/chainlit`
   - API Documentation: `http://localhost:8000/docs`

### Docker Deployment

```bash
# Build and run backend
cd ScanSage_Backend
docker build -t scansage-backend .
docker run -d -p 8000:8000 --env-file .env scansage-backend

# Access at http://localhost:8000
```

---

## 📚 Documentation

Comprehensive documentation for each component:

- **[Backend Server Documentation](./ScanSage_Backend/README.md)** - FastAPI server setup, API endpoints, and model details
- **[Frontend UI Documentation](./ScanSage_Frontend/ScanSage_UI/README.md)** - Chainlit interface setup and configuration
- **[Data Layer Documentation](./ScanSage_Frontend/ScanSage_Datalayer/README.md)** - PostgreSQL schema and cloud storage setup

---

## 🎬 Demo

### Sample Workflow

1. **Upload Medical Scan**: Drag and drop or upload an MRI/CT/X-ray image
2. **Automated Analysis**: System identifies scan type, organ, and performs tumor detection
3. **Visual Insights**: View heatmaps and regions of interest
4. **Interactive Q&A**: Ask follow-up questions about the scan
5. **Report Generation**: Get a comprehensive analysis report

### API Example

```python
import requests

# Analyze a medical scan
url = "http://localhost:8000/api/analyze"
files = {"file": open("brain_mri.jpg", "rb")}
response = requests.post(url, files=files)

result = response.json()
print(f"Tumor Type: {result['tumor_prediction']['predicted_class']}")
print(f"Confidence: {result['tumor_prediction']['confidence_level']:.2%}")
```

---

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/analyze` | POST | Upload and analyze a medical scan |
| `/api/chat` | POST | Submit text queries with optional images |
| `/process-image` | POST | Process MRI images for ROI and heatmaps |
| `/docs` | GET | Interactive API documentation (Swagger UI) |

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate tests.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

**Important**: ScanSage AI is designed for **research and educational purposes only**. This tool is not a medical device and should not be used as a substitute for professional medical diagnosis, advice, or treatment. Always consult qualified healthcare professionals for medical decisions.

The system's predictions and analyses should be considered as supplementary information and must be validated by certified medical practitioners before any clinical application.

---

## 🙏 Acknowledgments

- **TensorFlow/Keras** - Deep learning framework for medical image classification
- **Google Generative AI** - Gemini 1.5 Pro for natural language understanding
- **FastAPI** - Modern, fast web framework for building APIs
- **Chainlit** - Conversational AI framework for the user interface
- **OpenCV** - Computer vision library for image processing
- **Open-source medical imaging datasets** - For model training and validation

---

## 👨‍💻 Author

**Wizaye**
- GitHub: [@wizaye](https://github.com/wizaye)
- Project: [ScanSage-AI](https://github.com/wizaye/ScanSage-AI)

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/wizaye/ScanSage-AI?style=social)
![GitHub forks](https://img.shields.io/github/forks/wizaye/ScanSage-AI?style=social)
![GitHub issues](https://img.shields.io/github/issues/wizaye/ScanSage-AI)
![GitHub pull requests](https://img.shields.io/github/issues-pr/wizaye/ScanSage-AI)

---

<div align="center">

**Built with ❤️ for the healthcare community**

If you find this project useful, please consider giving it a ⭐ on GitHub!

</div>
