import tensorflow as tf
import os


model = tf.keras.models.load_model('hand.model')

image_number = 1

while os.path.isfile(f"digits/digit{image_number}.png")