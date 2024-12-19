import cv2 as cv
from Preprocessing.RemoveBackground import removeBackgroundSingle
from Preprocessing.utility import getPred_Preprocess
sample_data = input("샘플 데이터의 파일 경로와 파일명을 지정해주세요\n")
rembg_img = removeBackgroundSingle(r"{}".format(sample_data))
rembg_img = getPred_Preprocess(rembg_img)
cv.imshow("sampling",rembg_img)
cv.waitKey(0)
cv.destroyWindow("sampling")
print(rembg_img.shape)
print(rembg_img[32][32])
print((rembg_img<0).sum())