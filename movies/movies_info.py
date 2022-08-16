import requests
import json
from datetime import date, timedelta
import json


today = date.today()
yesterday = date.today() - timedelta(1)
today = yesterday.strftime('%Y%m%d')

# 사이트 영화 박스오피스 랭킹
url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=d6ac93238cc6e7506345ca7a1af1b6af&targetDt=' + today + "&itemPerPage=10"
res = requests.get(url)
text= res.text

d = json.loads(text)


movie_list = []
for b in d['boxOfficeResult']['dailyBoxOfficeList']:
    data = {'rank': b['rank'], 'movie_name': b['movieNm'], 'open_date': b['openDt'], 'audience_count': b['audiCnt']}
    
    
# json 파일 출력
with open('boxoffice_movie_list.json','w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent="\t")



# 엑셀 파일로 출력
# data = pd.DataFrame(movie_list)
# data.columns = ['rank', 'movie_name', 'open_date', 'audience_count']
# data.head()
# data.to_csv("boxoffice_movie_list.csv", mode='w', encoding='euc-kr', index=False)