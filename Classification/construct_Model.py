import pickle
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2 as cv
import os
import random
from classification_model import getTrainData
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input, Conv2D, MaxPool2D, Flatten, Activation
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from background import removeBackgroundFolder, removeBackgroundSingle

data_sets = getTrainData(r"d:\imgs")
label_list = data_sets["label_list"]
x_train,y_train = data_sets["train"]
x_test,y_test = data_sets["test"]
# print(x_train.shape, y_train.shape)
# print(x_test.shape, y_test.shape)
# print(y_train[:10])

x_train = x_train/255.
x_test = x_test/255.

# image confirm
# randomlist = [random.randint(0,len(x_train)) for i in range(10)]
# # print(randomlist)
# for ix,xnum in enumerate(randomlist):
#     plt.subplot(2,5,ix+1)
#     plt.imshow(x_train[ix])
#     plt.title(label_list[y_train[ix]])
#     plt.xticks([]);plt.yticks([])
# plt.show()
y_train = tf.one_hot(y_train,10)
y_test = tf.one_hot(y_test,10)
# print(y_train.shape,y_test.shape)
model = Sequential()
model.add(Input(shape=(64,64,3)))
model.add(Conv2D(filters=64,kernel_size=5,strides=1,padding="same",activation="relu"))
model.add(MaxPool2D(pool_size=(3,2),padding="same"))
model.add(Dropout(0.3))
model.add(Conv2D(filters=128,kernel_size=5,strides=1,padding="same",activation="relu"))
model.add(MaxPool2D(pool_size=(3,2),padding="same"))
model.add(Dropout(0.3))
model.add(Conv2D(filters=256,kernel_size=5,strides=2,padding="same",activation="relu"))
model.add(MaxPool2D(pool_size=(3,2),padding="same"))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dropout(0.3))
model.add(Dense(256,activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(128,activation="relu"))
model.add(Dropout(0.4))
model.add(Dense(32,activation="relu"))
model.add(Dense(10,activation="softmax"))
model.summary()
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
callback = tf.keras.callbacks.EarlyStopping(
    monitor="val_accuracy",patience=10,verbose=1,restore_best_weights=True
)
fithist = model.fit(x_train,y_train,epochs=100,validation_data=(x_test,y_test),batch_size=100,callbacks=[callback])
with open("classification_image.history","wb") as fp:
    pickle.dump(fithist, fp)
model.save("classification_image.keras")