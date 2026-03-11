import os
import shutil
from ultralytics import YOLO

# 1. Setup Paths
dataset_path = r'datasets\chairs' # Using raw string for Windows paths
images_dir = os.path.join(dataset_path, 'images')
labels_dir = os.path.join(dataset_path, 'labels')
no_table_dir = os.path.join(dataset_path, 'no_chairs')

os.makedirs(labels_dir, exist_ok=True)
os.makedirs(no_table_dir, exist_ok=True)

# 2. Load model
model = YOLO('yolov8n.pt') 

# Class ID for dining table in COCO dataset
TABLE_CLASS_ID = 56

# 3. Process Images
for img_name in os.listdir(images_dir):
    if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(images_dir, img_name)
        
        # Run inference
        results = model(img_path)[0]
        
        # Filter boxes to only include dining tables (class 60)
        table_boxes = [box for box in results.boxes if int(box.cls[0]) == TABLE_CLASS_ID]
        
        if len(table_boxes) == 0:
            # No tables found specifically -> Move to no_tables
            shutil.move(img_path, os.path.join(no_table_dir, img_name))
            print(f"Moved {img_name}: No dining table (class 60) detected.")
        else:
            # Table(s) detected -> Save labels
            label_filename = os.path.splitext(img_name)[0] + '.txt'
            label_path = os.path.join(labels_dir, label_filename)
            
            with open(label_path, 'w') as f:
                for box in table_boxes:
                    cls = int(box.cls[0])
                    coords = box.xywhn[0].tolist()
                    f.write(f"{cls} {' '.join(map(str, coords))}\n")
            print(f"Labeled {img_name}: {len(table_boxes)} table(s) found.")

print("Processing complete.")