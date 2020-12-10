# pip install beautifulsoup4
# pip install lxml # 구문을 분석하는것

import requests
from bs4 import BeautifulSoup

# https://comic.naver.com/webtoon/weekday.nhn 네이버 웹툰을 갖고해볼것임
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# 가지고오는 html 문서를 lxml 을 통해서 숩으로 처넣기
# print(soup.title) # <title>네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
# print(soup.title.get_text()) # 네이버 만화 > 요일별  웹툰 > 전체웹툰
# print(soup.a) # soup 객체에서 처음으로 발견되는 a 발견
# print(soup.a.attrs) # 속성값들을 볼수가 있다.
# print(soup.a["href"]) # #menu
##################### 위 방법은 페이지에대한 이해도가 높을때 사용할수 있는것이다.

# print(soup.find("a", attrs={"class":"Nvtn_upload"})) # 클래스값이 엔버튼인것을 찾아줘
# print(soup.find(attrs={"class":"Nvtn_upload"})) # 버튼이 하나인것을 알기 떄문에 사용가능

# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = (soup.find("li", attrs={"class":"rank01"}))
# print(rank1.a) # a 엘리먼트만 잘 나온다
# print(rank1.a.get_text()) # a 태그의 글자만 가지고온다
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# rank1.find_next_siblings("li")
# print(rank1.find_next_siblings("li"))

# webtoon = soup.find("a",text="연애혁명")
# print(webtoon)