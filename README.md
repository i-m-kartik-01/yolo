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

Bash
```
python train.py
```
# Project Structure
predict.py: Main script for live webcam detection and QR scanning.

train.py: Training script for YOLOv8n.

data.yaml: Configuration for dataset paths and class names.

annotate.py / label_data.py: Helper scripts for dataset preparation.


