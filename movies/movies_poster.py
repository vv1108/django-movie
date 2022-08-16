import json
import time
from selenium import webdriver
from selenium.webdriver import ActionChains  # 액션체인 활성화
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By


options = Options()
options.binary_location= 'C:\Program Files\Google\Chrome\Application/chrome.exe'

dr = webdriver.Chrome(r"C:\Users\chromedriver.exe", chrome_options = options)
time.sleep(1)

dr.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver')

act = ActionChains(dr)  # 드라이버에 동작을 실행시키는 명령어를 act로 지정

movie_name_text_list = []
movie_poster_src_list = []
for i in range(0, 10):
    element = dr.find_elements(By.CSS_SELECTOR, "div.tit3 > a")  # 동작 할 요소 선택
    act.click(element[i]).perform()
    poster = dr.find_element(By.CSS_SELECTOR, "div.poster > a > img")
    movie_name = dr.find_element(By.CSS_SELECTOR, "div.mv_info > h3.h_movie > a")
    movie_name_text = movie_name.get_attribute('innerHTML')
    movie_poster_src = poster.get_attribute("src")
    movie_name_text_list.append(movie_name_text)
    movie_poster_src_list.append(movie_poster_src)
    time.sleep(3)
    dr.back()
dr.close()

movie_poster_name_list = []
data = {'movie_poster_name':movie_name_text_list, 'movie_poster_src':movie_poster_src_list}

# json 파일 출력
with open('poster_list.json','w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent="\t")


# 엑셀 파일 출력
# data = pd.DataFrame({'movie_poster_name':movie_name_text_list, 'movie_poster_src':movie_poster_src_list})
# data.to_csv("poster_list.csv", mode='w', encoding='euc-kr', index=False)

