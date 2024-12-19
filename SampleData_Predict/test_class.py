import os
import pickle
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from Preprocessing.Remove_Background import removeBackgroundSingle
from Preprocessing.utility import getPred_Preprocess, saveConfig



# label_list = os.listdir(r"d:\imgs")
curpath = os.path.dirname(os.path.abspath(__file__))
path_list = curpath.split("\\")[:-1]
rootpath = "\\".join(path_list)
# saveConfig(label_list,rootpath)

with open(f"{rootpath}\\config", "rb") as fp:
    label_list = pickle.load(fp)
print("라벨리스트 확인:", label_list)
sample_data = input("라벨리스트가 불러 와 졌는지 확인 후\n"
                    "샘플 데이터의 파일 경로와 파일명을 지정해주세요\n")
origin_img = cv.imread(sample_data,cv.COLOR_BGR2RGB)
origin_img = cv.resize(origin_img,(128,128))
rembg_img = removeBackgroundSingle(r"{}".format(sample_data))
rembg_img = getPred_Preprocess(rembg_img)
rembg_img = np.array([rembg_img])
# d:\123123.jpg
# print(rembg_img.shape)
# print(rembg_img[0][32][32])d
# print((rembg_img<0).sum())

# 모델로딩
model = load_model(f"{rootpath}\\Training\\classification_image.keras")
y_pred = model.predict(rembg_img)


plt.imshow(origin_img)
plt.xlabel("pred:"+label_list[np.argmax(y_pred)])
plt.xticks([]);plt.yticks([])
plt.show()