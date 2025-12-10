{\rtf1\ansi\ansicpg1251\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import os\
import time\
import numpy as np\
import tensorflow as tf\
from picamera import PiCamera\
from pygame import mixer  # \uc0\u1041 \u1080 \u1073 \u1083 \u1080 \u1086 \u1090 \u1077 \u1082 \u1072  \u1076 \u1083 \u1103  \u1079 \u1074 \u1091 \u1082 \u1072 \
from PIL import Image\
\
MODEL_PATH = "Project.keras" \
SOUND_PATH = "alarm.wav"      \
IMG_SIZE = (100, 100)       \
CONFIDENCE_THRESHOLD = 0.7   \
\
mixer.init()\
def play_alarm():\
    if not mixer.music.get_busy(): # \uc0\u1063 \u1090 \u1086 \u1073 \u1099  \u1085 \u1077  \u1085 \u1072 \u1082 \u1083 \u1072 \u1076 \u1099 \u1074 \u1072 \u1083 \u1086 \u1089 \u1100 , \u1077 \u1089 \u1083 \u1080  \u1091 \u1078 \u1077  \u1080 \u1075 \u1088 \u1072 \u1077 \u1090 \
        mixer.music.load(SOUND_PATH)\
        mixer.music.play()\
\
model = tf.keras.models.load_model(MODEL_PATH)\
\
camera = PiCamera()\
camera.resolution = (1024, 768)\
time.sleep(2)\
\
try:\
    while True:\
        temp_file = "current_scan.jpg"\
        camera.capture(temp_file)\
        \
        img = Image.open(temp_file).resize(IMG_SIZE)\
        img_array = np.array(img)\
        \
        img_array = img_array / 255.0\
        \
        img_array = np.expand_dims(img_array, axis=0)\
\
        prediction = model.predict(img_array, verbose=0)\
        \
        score = prediction[0][0] \
        \
\
        if score > CONFIDENCE_THRESHOLD:\
            play_alarm()\
        else:\
\
        time.sleep(1)\
\
except KeyboardInterrupt:\
    camera.close()}