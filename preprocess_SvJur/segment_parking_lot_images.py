import pandas as pd
import cv2
import os


root_dir = '/mnt/c/Users/krock/Desktop/SvJur'

for dir in os.listdir(root_dir):
    if len(os.listdir(os.path.join(root_dir, dir, 'segmented'))) != 0:
        continue
    df = pd.read_csv(os.path.join(root_dir, dir, '_' + dir + '_segmentation_mask.csv'))
    for filename in os.listdir(os.path.join(root_dir, dir, 'resized')):
        if filename[0].isdigit():
            img = cv2.imread(os.path.join(root_dir, dir, 'resized', filename))
            for index, row in df.iterrows():
                sub_img_orig = img[row['left_top_y']:row['right_bottom_y'], row['left_top_x']:row['right_bottom_x']]
                sub_img_resized = cv2.resize(sub_img_orig, (250,250))
                new_filename = filename.replace('.jpg', '') + '_' + str(index + 1) + '.jpg'
                print(os.path.join(root_dir, dir, 'segmented', new_filename))
                cv2.imwrite(os.path.join(root_dir, dir, 'segmented', new_filename), sub_img_resized)
