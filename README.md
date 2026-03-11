## YOLOv8 Real-Time Multi-Class Bot (Kriti 2026)
This repository contains a custom-trained YOLOv8 object detection system designed for real-time inference via webcam. It features specialized logic for differentiating between QR codes and license plates, and includes live QR data decoding.

 # Key Features
12-Class Detection: Detects faces, cars, motorbikes, dogs, cats, and more.

Smart QR vs. Plate Logic: Uses aspect-ratio analysis to resolve common misidentifications between square QR codes and rectangular number plates.

Live QR Scanning: Automatically crops and decodes QR code data using pyzbar.

Hardware Optimized: Designed to run on NVIDIA RTX 3050 (Laptop) using CUDA acceleration.

# Setup & Installation
Clone the repository:

Bash
git clone https://github.com/i-m-kartik-01/yolo.git
cd yolo
Create a virtual environment:

Bash
python -m venv yolo_env
source yolo_env/bin/activate  # On Windows: .\yolo_env\Scripts\activate
Install Dependencies:

Bash
pip install ultralytics opencv-python torch torchvision pyzbar numpy
# Usage
Running Live Inference
To start the webcam feed with the custom remapping logic and QR decoding, run:

Bash
python predict.py
Training the Model
If you need to retrain the model with your custom data.yaml:

Bash
python train.py
# Project Structure
predict.py: Main script for live webcam detection and QR scanning.

train.py: Training script for YOLOv8n.

data.yaml: Configuration for dataset paths and class names.

annotate.py / label_data.py: Helper scripts for dataset preparation.

# Academic Context
Developed as part of a B.Tech Project at the Indian Institute of Technology Guwahati (IITG). The project focuses on integrating computer vision with embedded systems (Arduino/PID control).

Next Steps
Open your README.md on GitHub.

Click the Edit (pencil icon).

Paste the text above and click Commit changes.

Would you like me to add a section to the README explaining how the PID control interacts with these detections for your fan project?
