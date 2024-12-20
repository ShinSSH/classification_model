//데이터
data_sets=[]
//데이터 아키텍처{sub_title:"",sub_content:"",sub_img:[],user_fill:"",asso_file:""}
data_sets.push({
  sub_title:"이미지 크롤링",
  sub_content:"구글과 네이버에서 이미지 수집",
  sub_img:["19mE7FPBYbmIENItnh77EuZV6jEjr5UID",
           "1Y9RZRagyRDnfTr5yaqWC8LoPuRC__MMv",
           "1aHiGpZwqN62MyzKF_v_1tnGBZPkv2cRt",
           "19hK3BsTAPmscS4vO4uvb5Oxv1Ov7OXbs"],
  user_fill:"selenium 라이브러리와 크롬 드라이버를 활용한 데이터 수집 자동화 - 관련없는 데이터는 임의로 삭제",
  asso_file:"관련파일 /Crawling/Crawling_Running 실행"
})

data_sets.push({
  sub_title:"이미지 배경제거 및 증대",
  sub_content:"수집한 이미지의 배경을 제거 시키고 밝기,회전 등을 조정하여 이미지 수량을 증대함",
  sub_img:["17C4Ez2sSvNGsR-3RIZceUkzo4tOzOT0T",
           "1FCrZupnf6SHt4v1dUN2ytHxGjIfuIYUB"],
  user_fill:"배경제거를 위해 remgb 라이브러리를 사용, 이미지 증대를 위해 텐서플로우의 밝기,회전 등의 라이브러리를 사용",
  asso_file:"관련파일 /Preprocessing/Preprocessing_Running.readImageDirect 호출 실행"
})

data_sets.push({
  sub_title:"이미지 전처리",
  sub_content:"증대된 이미지의 사이즈 변경 및 수치표준화와 원핫 인코딩을 적용하여 훈련데이터를 셋팅",
  sub_img:["1RZ9SPbGw_ebGbnCJNPghPu_rSm5nXpiZ",
           "10DhEE9dXtQBve3fYcs2ZFyhNYM5rB4v6"],
  user_fill:"배경제거를 위해 remgb 라이브러리를 사용, 이미지 증대를 위해 텐서플로우의 밝기,회전 등의 라이브러리를 사용",
  asso_file:"관련파일 /Training/construct_Model"
})

data_sets.push({
  sub_title:"데이터 확인 및 모델 구성",
  sub_content:"전처리 된 정답과 이미지 순서 일치를 확인 후 모델 구성",
  sub_img:["1WTBkf6EqWL85kiuRthuz9HAbBJr0cEPp",
           "10DhEE9dXtQBve3fYcs2ZFyhNYM5rB4v6"],
  user_fill:"Conv2D 레이어와 MaxPool2D 및 Dropout을 이용해 특성 추출과 과적합 방지 및 일반화",
  asso_file:"관련파일 /Training/construct_Model,train_fit"
})

data_sets.push({
  sub_title:"훈련 시작",
  sub_content:"구성된 모델을 전처리 한 훈련데이터를 이용해 훈련",
  sub_img:["1actwvjUvRCo6KY9DNFEQahYF15EVqRFr",
           "1ntYNLd8hdLVITvyE9Xt0_mDM04yATNho"],
  user_fill:"콜백 함수를 이용해 최적의 정확도를 가진 모델을 훈련",
  asso_file:"관련파일 /Training/train_fit"
})

data_sets.push({
  sub_title:"모델 성능 시각화와 요약",
  sub_content:"모델의 종합적인 성능평가를 위해 여러 그래프 시각화 시킴",
  sub_img:["1ot1ZHx9GhFp219OCJMKOHN1ltR_WaXC6",
           "1iTAlaIXegJ9yIvreJkFZ3gfoe4q2BZeW",
           "16_YS7c9Vloxxa0sRTK1XNkrBKjazycOb",
           "1L74T1-PPTR1sq7hZlgo2zzTi0mqxZx1L"],
  user_fill:"matplotlib, confusion_matrix,classification_report 라이브러리를 이용한 시각화 및 성능확인 - 확인 결과 성능이 다소 떨어짐, 앵무새와 호랑이를 제외한 나머지 이미지에 대한 추가 훈련이미지 수집이 필요.",
  asso_file:"관련파일 /Training/train_fit"
})