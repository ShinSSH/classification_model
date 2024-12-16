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
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from background import removeBackgroundFolder, removeBackgroundSingle

label_list,y_data, x_data = load_directory(r"d:\imgs")
# print(y_data.shape,x_data.shape)
# print(y_data[0])
# print(len(label_list))
# print(label_list[0])
# suffle
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.2,random_state=10,stratify=y_data)
# print(x_train.shape, y_train.shape)
# print(x_test.shape, y_test.shape)
# print(y_train[:10])

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
model.add(MaxPool2D(pool_size=(3,3),padding="same"))
model.add(Dropout(0.2))
model.add(Conv2D(filters=128,kernel_size=5,strides=1,padding="same",activation="relu"))
model.add(MaxPool2D(pool_size=(3,3),padding="same"))
model.add(Dropout(0.2))
model.add(Conv2D(filters=256,kernel_size=5,strides=1,padding="same",activation="relu"))
model.add(MaxPool2D(pool_size=(3,3),padding="same"))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dropout(0.4))
model.add(Dense(256,activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(64,activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(32,activation="relu"))
model.add(Dropout(0.1))
model.add(Dense(10,activation="softmax"))
model.summary()
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
callback = tf.keras.callbacks.EarlyStopping(
    monitor="val_accuracy",patience=20,verbose=1,restore_best_weights=True
)
fithist = model.fit(x_train,y_train,epochs=150,validation_data=(x_test,y_test),batch_size=1000,callbacks=[callback])
with open("classification-image.history","wb") as fp:
    pickle.dump(fithist, fp)
model.save("classification-image.keras")