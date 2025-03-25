# ScanSage AI - User Interface

![ScanSage AI Logo](https://via.placeholder.com/150?text=ScanSage+AI)

ScanSage AI is a medical imaging analysis platform that provides AI-powered insights into MRI scans through an interactive conversational interface. This repository contains the frontend application built with Chainlit, designed to interact seamlessly with the ScanSage AI backend.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Overview

The ScanSage AI frontend provides a user-friendly interface for interacting with the AI-powered backend. It allows users to upload MRI scans, receive real-time AI analysis, and interact with the system via a conversational chat interface. The application is built using Chainlit and requires the backend API for processing and analysis.

## Features

- **Interactive Chat Interface**: Upload and analyze MRI scans via a chat-based UI.
- **Real-time Analysis**: Instant AI feedback on uploaded MRI scans.
- **AI-Powered Insights**: Advanced models for scan type identification, organ detection, and tumor classification.
- **Heatmap and ROI Visualization**: Highlight key areas of concern in the scans.
- **Secure Authentication**: User login system for protected access.
- **Multi-Device Support**: Responsive design for desktop and mobile.

## System Requirements

- Python 3.7+
- PostgreSQL (for chat history storage)
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ScanSage-AI-Frontend.git
cd ScanSage-AI-Frontend
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root with the following variables:

```
PORT=3000
CHAINLIT_AUTH_SECRET=your_secret_key
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
API_URL=http://localhost:8000/api/chat
```

Replace the placeholder values with actual configuration details.

## Configuration

### Chat History and Authentication Setup

To enable chat history and proper authentication, the application requires a chat database (data layer). This is configured in the `custom_datalayer` directory. Follow the guide in that folder to set up the data layer properly. [Custom Data Layer Guide](link-to-guide).

### Database Setup

1. Create a PostgreSQL database:

```bash
createdb scansage_db
```

2. Update the `DATABASE_URL` in your `.env` file to match your PostgreSQL instance.

### API Configuration

The application communicates with the backend API for image analysis. Ensure the `API_URL` variable in `.env` is set correctly to the backend endpoint.

## Usage

### Starting the Application

```bash
python main.py
```

The application will be available at `http://localhost:3000/chainlit`.

### Using the Interface

1. **Login**: Enter your credentials.
2. **Upload an MRI Image**: Click the upload button or drag and drop an image.
3. **Ask Questions**: Interact with the AI via chat.
4. **View Analysis**: Receive AI-generated insights.

## API Integration

The frontend communicates with the backend API via HTTP requests, sending images and queries for processing. The expected API response format includes:

```json
{
  "message": "Analysis complete. I've detected a tumor in the brain MRI.",
  "image_analysis": [
    {
      "filename": "brain_scan.jpg",
      "analysis": {
        "llm_analysis": {
          "scan_type": "T1-weighted MRI",
          "organ": "Brain",
          "tumor_type": "Meningioma",
          "detailed_description": "..."
        },
        "tumor_prediction": {
          "predicted_class": "Meningioma",
          "confidence_level": 0.92
        },
        "heatmap": "base64_encoded_image",
        "roi": "base64_encoded_image"
      }
    }
  ]
}
```

## Project Structure

```
ScanSage-AI-Frontend/
├── components/              # Application components
│   └── chainlit_app.py      # Main Chainlit application logic
├── custom_datalayer/        # Chat history and authentication data layer
├── public/                  # Public assets
│   ├── elastic.css          # Custom CSS
│   └── theme.json           # UI theme configuration
├── .env                     # Environment variables
├── .gitignore               # Git ignore file
├── chainlit.md              # Chainlit welcome page
├── main.py                  # Chainlit app entry point
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Customization

### UI Theme Customization

Modify `public/theme.json` to customize the UI appearance.

### CSS Customization

Edit `public/elastic.css` for styling adjustments.

### Welcome Page Customization

Update `chainlit.md` for welcome page modifications.

## Security

- **Authentication**: Secure login with Chainlit's authentication system.
- **Data Privacy**: No permanent storage of user data.
- **Environment Variables**: Secure configuration management.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

[Your License Here]

## Disclaimer

ScanSage AI is designed as an assistive tool and should not replace professional medical judgment. Always consult a medical expert for diagnosis and treatment decisions.

---

© 2025 ScanSage AI. All rights reserved.