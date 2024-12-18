from RemoveBackground import removeBackgroundSingle,removeBackgroundFolder

userSel = input("배경을 제거할 대상을 선택 하세요(단일 제거는 1, 다수 제거는 2를 눌러주세요\n")
if userSel==1: # 단일제거
    print("::::::::::::::::::::::::::::")
    imagePathName = input("배경을 제거할 파일 경로와 파일명.확장자까지 입력해주세요\n"
          "ex) d:\\img\\myimg.jpg\n")
    removeBackgroundSingle(r"{}".format(imagePathName))
else:
    print("::::::::::::::::::::::::::::")
    rpath = input("배경을 제거할 디렉토리 경로를 입력해주세요\n"
          "ex)d:\\imgs [ 경로내에 (폴더명\\파일명.확장자) 형태의 하위 디렉토리가 존재해야합니다 ]\n")
    removeBackgroundFolder(r"{}".format(rpath))