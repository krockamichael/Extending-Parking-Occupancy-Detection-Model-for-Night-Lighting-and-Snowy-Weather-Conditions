import tensorflow as tf


model = tf.keras.models.load_model("/home/michael/Desktop/VNOS/model/keras_mAlexNet/out_keras.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model.
with open('/home/michael/Desktop/model.tflite', 'wb') as f:
  f.write(tflite_model)
