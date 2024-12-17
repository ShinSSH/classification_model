import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from rembg import remove
import os

# https://github.com/xuebinqin/U-2-Net
# https://github.com/xuebinqin/DIU

rpath=r"d:\imgs"

def removeBackgroundFolder(rpath):
    f_lists = os.listdir(rpath)
    print(f_lists)
    for folder in f_lists:
        f_name = os.listdir(rpath+"\\"+folder)
        print(folder,":",end="")
        for name in f_name:

            img = cv2.imread(rpath+"\\"+folder+"\\"+name)
            img = cv2.resize(img,(256,256))
            # cv2.imshow("origin"+name,img)
            reimg = remove(img)
            cv2.imwrite(rpath+"\\"+folder+"\\"+name,reimg)
             # cv2.imshow(name,reimg)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            print(".",end="")
        print()

def removeBackgroundSingle(imagePathName):
    img = cv2.imread(imagePathName)
    img = cv2.resize(img, (256, 256))
    # cv2.imshow("origin"+name,img)
    reimg = remove(img)
    cv2.imwrite(imagePathName)
    print("배경제거가 완료 되었습니다.")
if __name__=="__main__":
    pass # 이 파일을 직접 실행했을 때 작동 코드
else:
    pass # 다른 파일에서 import 시 작동되는 코드
# img = cv2.imread(r"d:\imgs\n_tiger\n0b5f4c48-f1a0-4b3b-81be-e2a908dd8b8e.jpg")
# img = cv2.resize(img,(256,256))
# cv2.imshow("origin",img)
# reimg = remove(img)
# cv2.imshow("remove",reimg)

cv2.waitKey(0)
cv2.destroyAllWindows()
