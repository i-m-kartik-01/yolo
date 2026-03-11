# import os

# label_dir = "all_data/labels/val"

# for file in os.listdir(label_dir):

#     path = os.path.join(label_dir, file)

#     with open(path) as f:
#         lines = f.readlines()

#     new_lines = []

#     for line in lines:

#         parts = list(map(float, line.strip().split()))

#         cls = int(parts[0])
#         coords = parts[1:]

#         # polygon → bounding box
#         xs = coords[0::2]
#         ys = coords[1::2]

#         x_min = min(xs)
#         x_max = max(xs)
#         y_min = min(ys)
#         y_max = max(ys)

#         x_center = (x_min + x_max) / 2
#         y_center = (y_min + y_max) / 2
#         width = x_max - x_min
#         height = y_max - y_min

#         new_lines.append(f"{cls} {x_center} {y_center} {width} {height}")

#     with open(path,"w") as f:
#         f.write("\n".join(new_lines))

# print("All labels converted to bounding boxes")



import os
import cv2

image_dir = "all_data/images"
label_dir = "all_data/labels"

for split in ["train", "val"]:

    img_folder = os.path.join(image_dir, split)
    lbl_folder = os.path.join(label_dir, split)

    for file in os.listdir(lbl_folder):

        label_path = os.path.join(lbl_folder, file)
        image_path = os.path.join(img_folder, file.replace(".txt", ".jpg"))

        if not os.path.exists(image_path):
            continue

        img = cv2.imread(image_path)
        h, w = img.shape[:2]

        with open(label_path) as f:
            lines = f.readlines()

        new_lines = []

        for line in lines:

            parts = list(map(float, line.split()))
            cls = int(parts[0])
            x, y, bw, bh = parts[1:5]

            # convert pixel → normalized
            x /= w
            y /= h
            bw /= w
            bh /= h

            new_lines.append(f"{cls} {x} {y} {bw} {bh}")

        with open(label_path, "w") as f:
            f.write("\n".join(new_lines))

print("Labels normalized successfully.")