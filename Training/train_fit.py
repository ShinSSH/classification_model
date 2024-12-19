from Preprocessing.utility import getTrainData
from construct_Model import train_fit_run
label_list=x_train=x_test=y_train=y_test=None
userSel = input("디렉토리에서 훈련파일을 생성하여 가져오시겠습니까? 취소시 0 입력\n"
                "디렉토리 명을 입력하세요. ex) d:\\imgs (필요 디렉토리 내부 구조 d:\\img\\a\\b.jpg) \n")
if userSel!="0":
    data_sets = getTrainData(r"{}".format(userSel))
    label_list = data_sets["label_list"]
    print(label_list)
    x_train,y_train = data_sets["train"]
    print(x_train.shape)
    x_test,y_test = data_sets["test"]
    print("x_train(",len(x_train),")y_train(",len(y_train),")")
    print("x_test(", len(x_test), ")y_test(", len(y_test), ")")

userSel = input("순차모델을 구성합니다.\n"
                "훈련횟수를 입력하면 최적의 검증데이터 정확도에 맞춰 조기 종료됩니다\n"
                "classification_image.history 파일로 훈련과정이 저장되며\n"
                "classification_image.keras 파일로 훈련 모델이 저장됩니다.\n"
                "훈련 횟수를 숫자로 입력하세요. 취소는 0 입력\n")
if userSel!="0" and len(x_train)>0 and len(y_train)>0 and len(x_test)>0 and len(y_test)>0:
    input("엔터 키를 누르면 10개의 이미지를 확인합니다. 정답과 일치하는지 확인하세요.\n"
          "확인 후 창을 닫으면 훈련이 시작됩니다.")
    train_fit_run(int(userSel),label_list,x_train,y_train,x_test,y_test)