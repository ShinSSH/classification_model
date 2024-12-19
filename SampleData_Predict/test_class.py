import os
import pickle
import cv2 as cv
from Preprocessing.Remove_Background import removeBackgroundSingle
from Preprocessing.utility import getPred_Preprocess, saveConfig

ROOTPATH = os.path.dirname(os.path.abspath(__file__))
print(ROOTPATH)

label_list = os.listdir(r"d:\imgs")
saveConfig(label_list)
with open("config","rb") as fp:
    label_list = pickle.load("config")
print(label_list)
#
# sample_data = input("샘플 데이터의 파일 경로와 파일명을 지정해주세요\n")
# rembg_img = removeBackgroundSingle(r"{}".format(sample_data))
# rembg_img = getPred_Preprocess(rembg_img)
# cv.imshow("sampling",rembg_img)
# cv.waitKey(0)
# cv.destroyWindow("sampling")
# print(rembg_img.shape)
# print(rembg_img[32][32])
# print((rembg_img<0).sum())