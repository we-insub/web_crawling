import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가지고 오기
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title 인 모든 element 를 반환한다
for cartoon in cartoons:
    print(cartoon.get_text())  # 모든 엘리먼트를 가지고오기

