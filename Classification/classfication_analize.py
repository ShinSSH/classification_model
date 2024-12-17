import pickle
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2 as cv
import os
import random
import seaborn as sns
from classification_model import getTrainData
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input, Conv2D, MaxPool2D, Flatten, Activation
from sklearn.metrics import confusion_matrix
data_sets = getTrainData(r"d:\imgs")
label_list = data_sets["label_list"]
x_train,y_train = data_sets["train"]
x_test,y_test = data_sets["test"]
y_test = tf.one_hot(y_test,10)
with open("classification_image.history",'rb') as fp:
    fit_hist = pickle.load(fp)

print(fit_hist.history.keys())

plt.subplot(1,2,1)
plt.plot(fit_hist.history["accuracy"],label="train acc")
plt.plot(fit_hist.history["val_accuracy"],label="val acc")
plt.legend()
plt.title("ACC")
plt.subplot(1,2,2)
plt.plot(fit_hist.history["loss"],label="train loss")
plt.plot(fit_hist.history["val_loss"],label="val loss")
plt.legend()
plt.title("LOSS")
plt.show()

model = tf.keras.models.load_model("classification_image.keras")
loss,acc = model.evaluate(x_test,y_test)
print("손실값:",loss,"정확도:",acc)
y_pred = model.predict(x_test)
randomindex = [random.randint(0,len(x_test)) for ix in range(10)]
for i in range(len(randomindex)):
    plt.subplot(2,5,i+1)
    plt.imshow(x_test[randomindex[i]])
    plt.title(label_list[np.argmax(y_test[randomindex[i]])])
    plt.xlabel(label_list[np.argmax(y_pred[randomindex[i]])])
    plt.xticks([]);plt.yticks([])
plt.show()

# 혼동행렬
y_conv_true = np.array([label_list[np.argmax(ll)] for ll in y_test])
y_conv_pred = np.array([label_list[np.argmax(ll)] for ll in y_pred])
# print(y_conv_true.shape)
# print(y_conv_pred.shape)
# print(y_conv_true[1:10])
# print(y_conv_pred[1:10])
cm = confusion_matrix(y_conv_true,y_conv_pred)
sns.heatmap(cm, cmap="Blues",annot=True,fmt=".1f",xticklabels=label_list,yticklabels=label_list)
plt.show()