import cv2
import pandas as pd
import os

def reading(file_path, h):
    data = pd.read_csv(file_path, sep=",", header = h)
    return data

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images

def merge_channels(input_dir, output_dir):
    n = int(open("image_counter.txt", "r").read())
    images = load_images_from_folder(input_dir)
    for i in range(0, n):
        b, a, a = cv2.split(images[i*3])
        a, r, a = cv2.split(images[i*3+1])
        a, a, g = cv2.split(images[i*3+2])
        img = cv2.merge((b, r, g))
        cv2.imwrite(os.path.join(output_dir, str(i+1) + ".jpg"), img)

merge_channels(r"data", r"output")

