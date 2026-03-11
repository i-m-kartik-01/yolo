import os
import shutil
import random
import yaml

# Dataset paths
datasets = {
    "apple": "datasets/apple",
    "cat": "datasets/cats",
    "chair": "datasets/chairs",
    "dining_table": "datasets/dining_table",
    "dog": "datasets/dogs",
    "face": "datasets/face",
    "number_plate": "datasets/number_plate",
    "parcel_box": "datasets/parcel_box",
    "qr": "datasets/qr",
    # "dog": "datasets/dogs",
    # "cat": "datasets/cats",
    # "parcel_box": "datasets/parcel_box",
    # "qr": "datasets/qr",
    # # "number_plate": "datasets/number_plate"
}

# Final class IDs
class_map = {
    "apple": 0,
    "cat": 1,
    "chair": 2,
    "dining_table": 3,
    "dog": 4,
    "face": 5,
    "number_plate": 6,
    "parcel_box": 7,
    "qr": 8
}

# Output dataset
base_output = "all_data"

train_img = os.path.join(base_output, "images/train")
train_lbl = os.path.join(base_output, "labels/train")

val_img = os.path.join(base_output, "images/val")
val_lbl = os.path.join(base_output, "labels/val")

os.makedirs(train_img, exist_ok=True)
os.makedirs(train_lbl, exist_ok=True)
os.makedirs(val_img, exist_ok=True)
os.makedirs(val_lbl, exist_ok=True)

VAL_PER_CLASS = 10

for cls_name, path in datasets.items():

    image_dir = os.path.join(path, "images")
    label_dir = os.path.join(path, "labels")

    images = os.listdir(image_dir)
    random.shuffle(images)

    val_images = images[:VAL_PER_CLASS]

    for img in images:

        base = img.rsplit(".", 1)[0]

        img_src = os.path.join(image_dir, img)
        lbl_src = os.path.join(label_dir, base + ".txt")

        # Prevent overwriting
        new_name = f"{cls_name}_{base}"

        if img in val_images:

            img_dst = os.path.join(val_img, new_name + ".jpg")
            lbl_dst = os.path.join(val_lbl, new_name + ".txt")

        else:

            img_dst = os.path.join(train_img, new_name + ".jpg")
            lbl_dst = os.path.join(train_lbl, new_name + ".txt")

        shutil.copy(img_src, img_dst)

        if os.path.exists(lbl_src):

            with open(lbl_src) as f:
                lines = f.readlines()

            new_lines = []

            for line in lines:
                parts = line.strip().split()

                # Remap class id
                parts[0] = str(class_map[cls_name])

                new_lines.append(" ".join(parts))

            with open(lbl_dst, "w") as f:
                f.write("\n".join(new_lines))

print("Dataset merged successfully")

# -------- Generate data.yaml --------

# yaml_data = {
#     "path": base_output,
#     "train": "images/train",
#     "val": "images/val",
#     "names": class_map
# }

# with open(os.path.join(base_output, "data.yaml"), "w") as f:
#     yaml.dump(yaml_data, f)

# print("data.yaml generated")