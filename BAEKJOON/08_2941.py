# 크알	변경
# č	    c=
# ć	    c-
# dž	dz=
# đ	    d-
# lj	lj
# nj	nj
# š	    s=
# ž	    z=
# 전부 변수에 넣고 반복문 안 조건문으로 검증???
# 예외처리?

# input = 'ljes=njak'
input = input(str())

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 예외 알파벳 리스트

for x in a: # 리스트 a 반복
    input = input.replace(x, 'a') # replace ? 문자열에서 값 찾아 변경 해 주는 함수  replace("찾을값", "바꿀값", [바꿀횟수])
print(len(input)) # len ? 문자열 길이 세 주는 함수
