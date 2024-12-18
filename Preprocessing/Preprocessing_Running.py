from RemoveBackground import removeBackgroundSingle,removeBackgroundFolder
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be
from utility import readImageDirect

userSel = input("배경을 제거할 대상을 선택 하세요(단일 제거는 1, 다수 제거는 2, 건너뛰기는 0을 눌러주세요\n")
if userSel!="0":
    if userSel=="1": # 단일제거
        print("::::::::::::::::::::::::::::")
        imagePathName = input("배경을 제거할 파일 경로와 파일명.확장자까지 입력해주세요\n"
              "ex) d:\\img\\abc\\myimg.jpg\n")
        removeBackgroundSingle(r"{}".format(imagePathName))
    else: # 다수 제거
        print("::::::::::::::::::::::::::::")
        rpath = input("배경을 제거할 디렉토리 경로를 입력해주세요\n"
              "ex)d:\\imgs [ 경로내에 (폴더명\\파일명.확장자) 형태의 하위 디렉토리가 존재해야합니다 ]\n")
        removeBackgroundFolder(r"{}".format(rpath))

while(1):
    userSel = input("이미지 증강 전처리를 수행 시 디렉토리 경로와 수량을 [,]로 구분지어 입력하세요. 취소는 0을 입력해주세요\n"
                    "ex) d:\\img, 2\n")

    if userSel=="0":
        break
    prolist = userSel.split(",")
    if len(prolist)<2:
        print("경로와 수량을 구분지어 정확히 입력해주세요")
        continue
    readImageDirect(r"{}".format(prolist[0]),int(prolist[1]))
    break
