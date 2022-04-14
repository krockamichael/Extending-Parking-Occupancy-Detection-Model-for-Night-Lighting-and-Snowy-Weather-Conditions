import cv2
import os

root_dir = '/mnt/c/Users/krock/Desktop/SvJur/'

for dir in os.listdir(root_dir):
    for image_path in os.listdir(os.path.join(root_dir, dir)):
        cur_path = os.path.join(root_dir, dir, image_path)
        image = cv2.imread(cur_path)
        if image is None or image.size == 0:
            print(cur_path)
            break
        resized = cv2.resize(image, (1920, 1440), interpolation=cv2.INTER_LANCZOS4)
        # print(os.path.join(root_dir, dir, 'resized', image_path))
        cv2.imwrite(os.path.join(root_dir, dir, 'resized', image_path), resized)
