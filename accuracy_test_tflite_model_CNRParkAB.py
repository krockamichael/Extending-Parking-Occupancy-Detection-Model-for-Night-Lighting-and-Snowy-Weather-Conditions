from ALPR import ALPR, CharacterSegmenter
import pandas as pd
import numpy as np
import cv2


def segment_parking_lot(image:np.ndarray, seg_mask:pd.DataFrame) -> list:
    segmented = []
    for _, row in seg_mask.iterrows():
        left_top_point = (row['left_top_x'], row['left_top_y'])
        right_bottom_point = (row['right_bottom_x'], row['right_bottom_y'])
        seg_image = image[row['left_top_y']:row['right_bottom_y'], row['left_top_x']:row['right_bottom_x']]
        segmented.append([seg_image, (left_top_point, right_bottom_point)])

    return segmented


if __name__ == "__main__":
    input_value = input()

    alpr = ALPR()
    char_segmenter = CharacterSegmenter()

    if str(input_value) == '1':
        image = cv2.imread('/home/michael/Desktop/1.jpg')
        #print(image)
        lp = alpr.get_license_plate_candidates(image)
        print(char_segmenter.get_text(lp))

    else:
        # image = cv2.imread('/home/michael/Downloads/ZG4515-AH.jpg')
        image = cv2.imread('/home/michael/Downloads/0000.jpg')
        print(image.shape)
        cv2.imshow('1440, 1920', image)
        cv2.waitKey(0)
        image_2 = cv2.resize(image, (1440, 1080), cv2.INTER_LANCZOS4)
        print(image_2.shape)
        cv2.imshow('1080, 1920', image_2)
        cv2.waitKey(0)
        segmentation_mask = pd.read_csv('/home/michael/Desktop/VNOS/data/segmentation_mask.csv')
        segmented = segment_parking_lot(image, segmentation_mask)

        for i, value in enumerate(segmented):
            parking_space_image, points = value[0], value[1]
            occupied = True
            color = (0,0,255) if occupied else (0,255,0)
            # TODO if occupied do this else nothing
            # TODO draw contours! color based on occupancy
            license_plate_candidates = alpr.get_license_plate_candidates(parking_space_image)
            found_text = char_segmenter.get_text(license_plate_candidates)
            print(found_text)
            cv2.imshow('ps', parking_space_image)
            cv2.waitKey(0)
            image = cv2.rectangle(image, points[0], points[1], color, 2)

    cv2.imshow('test', image)
    cv2.waitKey(0)
    #lp = alpr.get_license_plate_candidates(image)
    #text = char_segmenter.get_text(lp)
    #print(text)
