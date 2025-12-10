

import os
import time
import numpy as np
import tensorflow as tf
from picamera import PiCamera
from pygame import mixer
from PIL import Image

MODEL_PATH = "Project.keras" 
SOUND_PATH = "alarm.wav"      
IMG_SIZE = (100, 100)       
CONFIDENCE_THRESHOLD = 0.7   

mixer.init()
def play_alarm():
    if not mixer.music.get_busy(): 
        mixer.music.load(SOUND_PATH)
        mixer.music.play()

model = tf.keras.models.load_model(MODEL_PATH)\

camera = PiCamera()
camera.resolution = (1024, 768)
time.sleep(2)

try:
    while True:
        temp_file = "current_scan.jpg"
        camera.capture(temp_file)
        
        img = Image.open(temp_file).resize(IMG_SIZE)
        img_array = np.array(img)
        
        img_array = img_array / 255.0
        
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array, verbose=0)
        
        score = prediction[0][0] 
        

        if score > CONFIDENCE_THRESHOLD:
            play_alarm()
        else:

        time.sleep(1)

except KeyboardInterrupt:
    camera.close()
