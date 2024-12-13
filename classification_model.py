import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2 as cv
import os
from keras.src.layers.preprocessing.image_preprocessing.random_flip import HORIZONTAL_AND_VERTICAL
from tensorflow.keras import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout, Input, Conv2D, MaxPool2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from background import removeBackgroundFolder, removeBackgroundSingle
#########################################################################


def imageAugment (img): # 이미지증강
    rn = np.random.randint(3,6)
    rn = round(rn/10,1)
    img = tf.image.random_brightness(img, rn)
    # img = tf.image.random_crop(img, size=(150,150,3))
    # img = tf.image.resize(img,size=(256,256,3),method="nearest",preserve_aspect_ratio=True)
    # img = tf.image.random_flip_left_right(img)
    # img = tf.image.random_flip_up_down(img)
    RR_model = tf.keras.layers.RandomRotation(factor=(-0.2,0.3))
    RF_model = tf.keras.layers.RandomFlip(mode=HORIZONTAL_AND_VERTICAL)
    RZ_model = tf.keras.layers.RandomZoom((-0.15,0.15),(-0.15,0.15))
    img = RR_model(img)
    img = RF_model(img)
    img = RZ_model(img)
    return img.numpy().astype(np.uint8)

def readImageDirect(rpath):
    cnt = 0
    f_lists = os.listdir(rpath)
    for folder in f_lists:
        f_name = os.listdir(rpath+"\\"+folder)
        print(folder,":",end="")
        for name in f_name:
            img = cv.imread(rpath+"\\"+folder+"\\"+name)
            img = cv.resize(img,(256,256))
            for ix in range(5):
                randomimg = imageAugment(img)
                cv.imwrite(rpath+"\\"+folder+"\\"+str(cnt)+name,randomimg)
                cnt+=1
            print(".",end="")
        print()
readImageDirect(r"d:\imgs")
SEED=10
np.random.seed(SEED)
tf.random.set_seed(SEED)