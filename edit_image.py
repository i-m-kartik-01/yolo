import os
import cv2
import albumentations as A

# Input and output folders
input_folder = "dataset\Tesla"
output_folder = "dataset\Tesla_augmented"

os.makedirs(output_folder, exist_ok=True)

# Augmentation pipeline
transform = A.Compose([
    A.Rotate(limit=20, p=0.7),                     # rotation ±20°
    A.HorizontalFlip(p=0.5),                       # flip
    A.RandomBrightnessContrast(                    # brightness change
        brightness_limit=0.3,
        contrast_limit=0.3,
        p=0.7
    ),
    A.GaussianBlur(blur_limit=(3,7), p=0.5),       # blur
    A.GaussNoise(var_limit=(10.0,50.0), p=0.5),    # noise
    A.RandomScale(scale_limit=0.2, p=0.5),         # zoom in/out
    A.RandomCrop(height=400, width=400, p=0.4),    # crop
    A.Perspective(scale=(0.05,0.1), p=0.5)         # perspective transform
])

# number of augmented images per original
AUG_PER_IMAGE = 20

for filename in os.listdir(input_folder):

    if filename.lower().endswith((".jpg",".png",".jpeg")):

        img_path = os.path.join(input_folder, filename)
        image = cv2.imread(img_path)

        base_name = os.path.splitext(filename)[0]

        # save original
        cv2.imwrite(os.path.join(output_folder, filename), image)

        for i in range(AUG_PER_IMAGE):

            augmented = transform(image=image)
            aug_img = augmented["image"]

            new_name = f"{base_name}_aug_{i}.jpg"
            save_path = os.path.join(output_folder, new_name)

            cv2.imwrite(save_path, aug_img)

print("Dataset augmentation complete.")