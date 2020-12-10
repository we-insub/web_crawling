# 정규화
import re  #re 정규식 라이브러리 사용

# 조금더 공부하고싶다면 w3schools. run python 예제들 확인해도좋다
# python re 파이썬 공식문서 페이지에서도 확인 해볼수 있다.

# abcd , book, desk
# ca?e 라고 생각을 한다면
# care, cafe, case ,cave ? 에 들어가는 문자를 A~Z 까지 다 입력해서 해볼수도있지만
# 정규식을 사용하자,

p = re.compile("ca.e")
# . : 점은 하나의 문자를 의미한다. - care, cafe, case | caffe 매칭안됨
# ^ : 문자열의 시작의미. - desk, destination | fade 매칭안됨
# % : 문자열의 끝 - case, base | face 매칭안됨

def print_match(m):
    if m:
        print("m.group() :", m.group()) # 일치하는 문자열을 반환
        print("m.string :", m.string) # 입력받는 문자열을 출력 변수이기때문에 괄호없음
        print("m.start() :", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() :", m.end()) # 일치하는 문자열의 끝 index
        print("m.span() :", m.span()) # 일치하는 문자열의 시작 / 끝 index 함께 표시
    else:
        print("매칭 되지 않았습니다.")

# careless 출력결과
# m.group() : care
# m.string : careless
# m.start() : 0
# m.end() : 4
# m.span() : (0, 4)

# m = p.match("care")
# print_match(m)
# careless 라고 입력을 하면 매칭이 되 었다고 뜬다
# 매치 : 주어진 문자열의 처음부터 일치하는지 확인하는 역활이다.


#m = p.match("cafe")
#print(m.group()) # 매치 되면 그룹안에있다 표시 , 않으면 에러가 발생된다.

# m = p.search("careless") # 서치 : 주어진 문자열중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("careless") # findall: 일치하는 모든것을 리스트 형태로 반환한다.
# print(lst)  # ['care']

# 1. p = re.compile("원하는정보")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = findall("비교할 문자열") 일차하는 모든것을 "리스트" 형태로 변환

# 원하는 형태 : 정규식
# . : 점은 하나의 문자를 의미한다. - care, cafe, case | caffe 매칭안됨
# ^ : 문자열의 시작의미. - desk, destination | fade 매칭안됨
# % : 문자열의 끝 - case, base | face 매칭안됨