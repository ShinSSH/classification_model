from gc import get_count

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2 as cv
import os
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
    RF_model = tf.keras.layers.RandomFlip(mode="HORIZONTAL_AND_VERTICAL")
    RZ_model = tf.keras.layers.RandomZoom((-0.15,0.15),(-0.15,0.15))
    img = RR_model(img)
    img = RF_model(img)
    img = RZ_model(img)
    return img.numpy().astype(np.uint8)

def readImageDirect(rpath,get_count):
    cnt = 0
    f_lists = os.listdir(rpath)
    for folder in f_lists:
        f_name = os.listdir(rpath+"\\"+folder)
        print(folder,":",end="")
        for name in f_name:
            img = cv.imread(rpath+"\\"+folder+"\\"+name)
            img = cv.resize(img,(256,256))
            for ix in range(get_count):
                randomimg = imageAugment(img)
                cv.imwrite(rpath+"\\"+folder+"\\"+str(cnt)+name,randomimg)
                cnt+=1
            print(".",end="")
        print()

def load_directory(rootpath):  #{label:[이미지 리스트]}
    f_list = os.listdir(rootpath)
    # print(f_list)
    y_labels = []
    x_files= []
    data_sets = {}
    for label,fpath in enumerate(f_list):
        print(".", end="")
        data_sets[label]=[]
        f_name = r"{}\{}".format(rootpath,fpath)
        f_imgname = os.listdir(f_name)
        # print(f_name)
        for p in f_imgname:
            y_labels.append(label)
            fimg = cv.imread(r"{}\{}".format(f_name,p))
            fimg = cv.cvtColor(fimg,cv.COLOR_BGR2RGB)
            fimg = cv.resize(fimg,(64,64))
            x_files.append(fimg)
    return f_list,np.array(y_labels),np.array(x_files)

def getTrainData(dpath):
    label_list, y_data, x_data = load_directory(dpath)
    # suffle
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=10, stratify=y_data)
    return {"label_list":label_list,"train":(x_train,y_train),"test":(x_test,y_test)}

if __name__=="__main__":
    print("Preprocessing_Running 파일을 실행하세요")