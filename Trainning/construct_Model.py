import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
import random
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input, Conv2D, MaxPool2D, Flatten, Activation
from seaborn import heatmap
from sklearn.metrics import confusion_matrix,classification_report
from Preprocessing.utility import saveConfig


# image confirm
def train_fit_run(train_count,label_list,x_train,y_train,x_test,y_test):
    randomlist = [random.randint(0,len(x_train)) for i in range(10)]
    print(randomlist)
    curpath = os.path.dirname(os.path.abspath(__file__))
    path_list = curpath.split("\\")[:-1]
    rootpath = "\\".join(path_list)
    saveConfig(label_list,rootpath)
    for ix,xnum in enumerate(randomlist):
        plt.subplot(2,5,ix+1)
        plt.imshow(x_train[ix])
        plt.title(label_list[np.argmax(y_train[ix])])
        plt.xticks([]);plt.yticks([])
    plt.show()

    model = Sequential()
    model.add(Input(shape=(64,64,3)))
    model.add(Conv2D(filters=64,kernel_size=5,strides=2,padding="same",activation="relu"))
    model.add(MaxPool2D(pool_size=(3,2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(filters=128,kernel_size=5,strides=1,padding="same",activation="relu"))
    model.add(MaxPool2D(pool_size=(3,2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(filters=256,kernel_size=5,strides=1,padding="same",activation="relu"))
    model.add(MaxPool2D(pool_size=(3,2)))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dropout(0.3))
    model.add(Dense(256,activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(128,activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(32,activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(10,activation="softmax"))
    model.summary()
    model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
    callback = tf.keras.callbacks.EarlyStopping(
        monitor="val_accuracy",patience=30,verbose=1,restore_best_weights=True)
    fithist = model.fit(
        x_train,y_train,epochs=train_count,validation_data=(x_test,y_test),batch_size=100,callbacks=[callback])
    with open("../classification_image.history","wb") as fp:
        pickle.dump(fithist, fp)
    model.save("classification_image.keras")
    input("훈련이 종료되었습니다.\n"
          "모델과 결과를 저장하였으며 엔터키를 누르면 손실도와 정확률을 평가합니다.\n")
    loss, acc = model.evaluate(x_test,y_test)
    print("손실도:", loss, "정확도", "{:.2f}".format(acc*100),"%")
    input("엔터키를 누르면 훈련 결과 손실도와 정확도 그래프를 시각화 합니다.")
    plt.subplot(1,2,1)
    pt.plot(fithist.history["accuracy"],label="Train Acc")
    pt.plot(fithist.history["val_accuracy"], label="Valid Acc")
    plt.legend()
    plt.title("ACCURACY")
    plt.subplot(1,2,2)
    pt.plot(fithist.history["loss"], label="Train Loss")
    pt.plot(fithist.history["val_loss"], label="Valid Loss")
    plt.legend()
    plt.title("LOSS")
    plt.show()
    input("시각화 창을 닫고 엔터키를 누르면 테스트 파일 예측을 시각화합니다.")
    y_pred = model.predict(x_test)
    randomindex = [random.randint(0,len(x_test)) for ix in range(10)]
    for i in range(len(randomindex)):
        plt.subplot(2,5, i+1)
        plt.imshow(x_test[randomindex[i]])
        plt.title(f"true:{label_list[np.argmax(y_test[randomindex[i]])]}")
        plt.xlabel(f"predict:{label_list[np.argmax(y_pred[randomindex[i]])]}")
        plt.xticks([])
        plt.yticks([])
    plt.show()
    input("엔터키를 누르면 혼동행렬을 작성하여 시각화 합니다.")
    # 혼동행렬
    y_conv_true = np.array([label_list[np.argmax(ll)] for ll in y_test])
    y_conv_pred = np.array([label_list[np.argmax(ll)] for ll in y_pred])
    # confusion_matrix()
    cm = confusion_matrix(y_conv_true, y_conv_pred)
    print(cm)
    heatmap(cm, cmap="Blues", annot=True, fmt=".1f", xticklabels=label_list, yticklabels=label_list)
    plt.show()
    input("창을 닫고 엔터를 입력하시면 최종 훈련결과 리포트를 출력합니다.")
    print(classification_report(y_conv_true,y_conv_pred))