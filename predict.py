import cv2
import torch
from ultralytics import YOLO

# Load your model
model = YOLO("runs/detect/train9/weights/best.pt")

# Define our problematic class indices from your data.yaml
PLATE_CLS = 6
QR_CLS = 8

results = model.predict(source=0, show=False, stream=True, conf=0.4)

for r in results:
    img = r.orig_img
    
    for box in r.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        w = x2 - x1
        h = y2 - y1
        aspect_ratio = w / h if h > 0 else 0

        # --- THE FIX: FORCED REMAPPING ---
        # If it says it's a number plate, but it's shaped like a square (QR code)
        if cls == PLATE_CLS:
            if 0.8 < aspect_ratio < 1.2:
                cls = QR_CLS
                label_name = "QR (Corrected)"
                color = (0, 255, 0) # Green for corrected QR
            else:
                label_name = "Number Plate"
                color = (255, 0, 0) # Blue for Plate
        else:
            label_name = model.names[cls]
            color = (0, 255, 255) # Yellow for others

        # Draw custom bounding box and label
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(img, f"{label_name} {conf:.2f}", (x1, y1 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("Corrected Inference", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()