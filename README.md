## YOLOv8 Real-Time Multi-Class Bot (Kriti 2026)
This repository contains a custom-trained YOLOv8 object detection system designed for real-time inference via webcam. It features specialized logic for differentiating between QR codes and license plates, and includes live QR data decoding.

 # Key Features
12-Class Detection: Detects faces, cars, motorbikes, dogs, cats, and more.

# Setup & Installation
Clone the repository:

Bash
```
git clone https://github.com/i-m-kartik-01/yolo.git
cd yolo
```
Create a virtual environment:

Bash
```
python -m venv yolo_env
source yolo_env/bin/activate  # On Windows: .\yolo_env\Scripts\activate
```
Install Dependencies:

Bash
```
pip install ultralytics opencv-python torch torchvision pyzbar numpy
```

# Usage
Running Live Inference
To start the webcam feed with the custom remapping logic and QR decoding, run:

Bash
```
python predict.py
```
# Project Structure
predict.py: Main script for live webcam detection and QR scanning.

train.py: Training script for YOLOv8n.

data.yaml: Configuration for dataset paths and class names.

## Live Feed Sharing (via ngrok)
This project uses ngrok to create a secure tunnel from your local development environment to the internet. This allows you to share your real-time YOLO detection dashboard with anyone, anywhere, without deploying to a cloud server.

1. Prerequisites
Account: Sign up for a free account at ngrok.com.

Installation: * Windows: Install via the Microsoft Store or download the ZIP.

Linux/Pi: sudo apt install ngrok.

Flask Configuration: Your app.py must be set to listen on all interfaces:

annotate.py / label_data.py: Helper scripts for dataset preparation.




