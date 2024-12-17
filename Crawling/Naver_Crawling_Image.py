import os.path
import requests
from pandas.io.common import is_url
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from urllib import parse
import uuid
import re

def get_naver (search_data,save_directory,cnt_count):
    for searchKeyword,keyword in search_data:
        searchKeyword = searchKeyword.strip()
        keyword = keyword.strip()
        time.sleep(3)
#네이버 접속
        driver = webdriver.Chrome()
        driver.get(r"https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query={}".format(searchKeyword))
        driver.fullscreen_window()
        time.sleep(3)
        cnt = 0
        for i in range(100):
            cnt += 30
            if cnt >= cnt_count:
                break
            ActionChains(driver).send_keys(Keys.END).perform()
            time.sleep(2)
        # class = image_group 이미지 컨테이너
        # img > src 이미지 경로
        f_ele = driver.find_elements(By.CSS_SELECTOR,".image_group img")
        f_ele = f_ele[:cnt_count]
        # print(len(f_ele))
        f_ele = [ie.get_attribute("src") for ie in f_ele if ie.get_attribute("src").startswith("http")]
        # pattern = ".*imgurl=(.*)&imgrefurl.*"
        pattern = r".+src=(http.+(\.jpg|\.JPG|\.png))"
        f_url=[]
        for ele in f_ele:
            try:
                f_url.append(parse.unquote(re.search(pattern=pattern,string = ele).groups()[0]))
            except:
                pass
        icount = 0
        for u in f_url:
            print(".",end="")
            img_site = requests.get(u)
            time.sleep(0.5)
            # print(img_site.headers)
            try:
                contentLength = img_site.headers["Content-Length"] or img_site.headers["content-length"]
            except:
                continue
            if int(contentLength)<5100:
                print("pass")
                continue
            simg = img_site.content
            save_path = f"{save_directory}\\n_{keyword}\\"
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            expandfile = u.split(".")[-1]
            ru = "n"+str(uuid.uuid4())
            file_path = ru + "." + expandfile
            with open(save_path+file_path,"wb") as fp:
                fp.write(simg)
                icount+=1
        print()
        print("네이버에서 {}개의 이미지를 받았습니다.".format(icount))
        driver.quit()

if __name__=="__main__":
    print("Crawling_image_running 파일에서 실행하세요")

# print(element.tag_name)

# element.send_keys(Keys.ENTER)
# https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query=%ED%98%B8%EB%9E%91%EC%9D%B4