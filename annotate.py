import os
import cv2

# Folder containing images
image_folder = r"datasets\face\images"

# Folder where labels will be saved
label_folder = r"datasets\face\labels"

os.makedirs(label_folder, exist_ok=True)

for file in os.listdir(image_folder):
    
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        
        image_path = os.path.join(image_folder, file)
        img = cv2.imread(image_path)

        if img is None:
            continue

        # YOLO annotation for full image
        annotation = "0 0.5 0.5 1.0 1.0"

        label_name = os.path.splitext(file)[0] + ".txt"
        label_path = os.path.join(label_folder, label_name)

        with open(label_path, "w") as f:
            f.write(annotation)

print("Annotations created successfully!")