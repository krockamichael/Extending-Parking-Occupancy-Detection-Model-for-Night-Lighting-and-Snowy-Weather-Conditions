import tflite_runtime.interpreter as tflite
import numpy as np
import cv2
import os


def preprocess_image(img_path):
    global interpreter, height, width, floating_model
    image = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    input_data = cv2.resize(image, (height, width))
    input_data = np.expand_dims(input_data, 0)
    if floating_model:
        input_data = np.float32(input_data / 255)
    interpreter.set_tensor(0, input_data)
    interpreter.invoke()
    result = str(np.argmax(interpreter.get_tensor(output_details[0]['index'])))
    confidence = [[round(i[0], 3), round(i[1], 3)] for i in interpreter.get_tensor(output_details[0]['index'])]
    return result, confidence


if __name__ == '__main__':
    global height, width, floating_model
    model_path = '/home/michael/Desktop/VNOS/model/model.tflite'
    interpreter = tflite.Interpreter(model_path=model_path, num_threads=4)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]
    floating_model = False
    if input_details[0]['dtype'] == np.float32:
        floating_model = True

    acc_dict = {'correct': 0, 'incorrect': 0}
    with open('/home/michael/Downloads/CNRParkAB_all.txt') as f:
        for line in f.readlines():
            image_path, label = line.strip().split(' ')
            image_path = os.path.join('/home/michael/Downloads/CNRParkAB', image_path)
            result, confidence = preprocess_image(image_path)
            # print(f'Actual: {label}\tPredicted: {result}\tConfidence: {confidence}')
            if label == result:
                acc_dict['correct'] += 1
            else:
                acc_dict['incorrect'] += 1

    print(acc_dict)
