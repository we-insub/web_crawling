# 웹사이트에서 접속하는 사용자정보 (헤더정보) 를 확인 한다. 웹에선
# ex) 스마트폰 네이버는 모바일룔 Pc에선 PC Mode

import requests

res = requests.get("http://https://unualti.tistory.com/")
res.raise_for_status()

#with open("tstory.html", "w", encoding="uft8") as f:
#     f.write(res.text)

# 결과적으로 T sroty 에서는 유저로 로그인이 안됨 컴퓨터로되서 검색이 되지 않는다.
# 접속 브라우저에 따라서 에이전트 값이 다 다르다.  