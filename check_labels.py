import os
import cv2
from ultralytics.utils.plotting import Annotator
from pathlib import Path

# --- CONFIGURATION ---
IMG_DIR = r"all_data\images\train"
LBL_DIR = r"all_data\labels\train"
# Your list currently has 12 items (index 0-11)
CLASS_NAMES = ["dog","cat", "parcel_box","qr", "number_plate","jf", "djf", "kd", "dogs","jf", "djf", "kd"]

# Get list of images
image_files = sorted([f for f in os.listdir(IMG_DIR) if f.endswith(('.jpg', '.png', '.jpeg'))])

print(f"Loaded {len(image_files)} images.")
print("CONTROLS: [Spacebar] = Next Image | [q] = Exit")

for img_name in image_files:
    # 1. Load Image
    img_path = os.path.join(IMG_DIR, img_name)
    img = cv2.imread(img_path)
    if img is None: continue
    h, w, _ = img.shape
    
    # 2. Find and Draw Labels
    label_name = Path(img_name).stem + ".txt"
    label_path = os.path.join(LBL_DIR, label_name)
    
    annotator = Annotator(img.copy()) 
    
    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            for line in f:
                parts = list(map(float, line.split()))
                if not parts: continue

                cls_id = int(parts[0])
                x, y, bw, bh = parts[1:5]
                conf = parts[5] if len(parts) > 5 else None

                # Calculate coordinates
                x1 = (x - bw/2) * w
                y1 = (y - bh/2) * h
                x2 = (x + bw/2) * w
                y2 = (y + bh/2) * h

                # --- FIX: Safety check for Class Index ---
                if cls_id < len(CLASS_NAMES):
                    name = CLASS_NAMES[cls_id]
                else:
                    name = f"UNKNOWN({cls_id})"

                label_text = f"{name} {f'{conf:.2f}' if conf else ''}"
                annotator.box_label([x1, y1, x2, y2], label=label_text)
    
    # 3. Add Filename to the Image
    display_img = annotator.result()
    
    # Draw a background rectangle for the filename text to make it readable
    cv2.rectangle(display_img, (0, 0), (w, 40), (0, 0, 0), -1)
    cv2.putText(display_img, f"File: {img_name}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # 4. Show Image and Wait for Input
    cv2.imshow("Dataset Auditor", display_img)
    
    while True:
        key = cv2.waitKey(0) & 0xFF
        if key == ord('q'):
            print("Exiting...")
            cv2.destroyAllWindows()
            exit()
        elif key == 32: # Spacebar
            break 

cv2.destroyAllWindows()
print("Reached the end of the dataset.")