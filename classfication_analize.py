import pickle
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2 as cv
import os
import random
from classification_model import load_directory
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input, Conv2D, MaxPool2D, Flatten, Activation

with open("classification_image.history",'rb') as fp:
    fit_hist = pickle.load(fp)

print(fit_hist.history.keys)

plt.subplot(1,2,1)
plt.plot(fit_hist.history["acc"],label="train acc")
plt.plot(fit_hist.history["val_acc"],label="val acc")
plt.legend()
plt.title("ACC")
plt.subplot(1,2,2)
plt.plot(fit_hist.history["loss"],label="train loss")
plt.plot(fit_hist.history["val_loss"],label="val loss")
plt.legend()
plt.title("LOSS")
plt.show()

model.predict