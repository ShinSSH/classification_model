import os
import pickle
import cv2 as cv
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
rembg_img = removeBackgroundSingle(r"{}".format(sample_data))
rembg_img = getPred_Preprocess(rembg_img)
cv.imshow("sampling",rembg_img)
cv.waitKey(0)
cv.destroyWindow("sampling")
print(rembg_img.shape)
print(rembg_img[32][32])
print((rembg_img<0).sum())