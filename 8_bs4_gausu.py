import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가지고 오기
#cartoons = soup.find_all("td", attrs={"class": "title"})
# class 속성이 title 인 모든 element 를 반환한다
#for cartoon in cartoons:
#    print(cartoon.get_text())  # 모든 엘리먼트를 가지고오기
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)


# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#    title = cartoon.a.get_text()
#    link = "https://comic.naver.com" + cartoon.a["href"]
#    print(title, link)

# 평점 구하기
total_rate = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rate += float(rate)
print("전체점수 : ",total_rate)
print("평균점수 : ",total_rate / len(cartoons))