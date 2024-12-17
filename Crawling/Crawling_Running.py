import os
from Naver_Crawling_Image import get_naver
from Google_Crawling_Image import get_google
#------------------------------------------------------------------------------------------
# searchKeywords = None
# keywords = None
# cnt_count = None
# search_data = None

while True:
    searchKeywords = None
    keywords = None
    cnt_count = None
    search_data=None

    save_directory = input("검색 후 저장할 디렉토리 이름을 드라이브명과 함께 적어주세요. [ ex) d:\\svimg ]\n")
    save_directory = r"{}".format(save_directory)
    searchKeyword_input = input("검색하고싶은 이미지를 입력하세요(다수 입력시 콤마로 구분)\n")
    keyword_input = input("파일명 사용할 영문 이름(다수 입력시 콤마로 구분)\n")
    cnt_count = int(input("다운로드 받을 수량을 입력해주세요\n"))
    searchKeywords = searchKeyword_input.split(",")
    keywords = keyword_input.split(",")
    search_data = zip(searchKeywords,keywords)
    cnt_count=int(cnt_count*1.8)
    if not save_directory:
        print("저장 할 디렉토리 이름을 반드시 적어주세요")
        continue
    try:
        if not os.path.exists(save_directory):
            os.mkdir(save_directory)
    except:
        print("디렉토리명이 잘못되었습니다. 다시 한번 입력해주세요")
        continue
    if len(searchKeywords)!=len(keywords):
        print("파일명과 검색단어 수량이 일치하지 않습니다. 다시 입력해주세요.")
    else:
        break

search_data=zip(searchKeywords,keywords)
get_google(search_data,save_directory,cnt_count)
search_data=zip(searchKeywords,keywords)
get_naver(search_data,save_directory,cnt_count)