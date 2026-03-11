from ultralytics import YOLO
import cv2
import os

model = YOLO("yolov8n.pt")

image_dir = "datasets/dining_table/images"
label_dir = "datasets/dining_table/labels"

os.makedirs(label_dir, exist_ok=True)

for img_name in os.listdir(image_dir):

    img_path = os.path.join(image_dir, img_name)

    image = cv2.imread(img_path)

    if image is None:
        continue

    h, w = image.shape[:2]

    results = model(image)[0]

    label_file = os.path.join(label_dir, img_name.replace(".jpg", ".txt"))

    with open(label_file, "w") as f:

        for box in results.boxes:

            cls = int(box.cls[0])

            # 56 = chair
            if cls == 60:

                x1, y1, x2, y2 = box.xyxy[0].tolist()

                x_center = ((x1 + x2) / 2) / w
                y_center = ((y1 + y2) / 2) / h
                width = (x2 - x1) / w
                height = (y2 - y1) / h

                f.write(f"{cls} {x_center} {y_center} {width} {height}\n")

print("Chair labels saved.")