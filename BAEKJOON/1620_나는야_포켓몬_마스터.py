# 포켓몬 개수 n, 문제 개수 m ( 1 < n, m < 100,000 )
# n만큼 포켓몬 이름 입력 최대 20자 이름은 영어로만 첫글자만 대문자로
# n 입력 종료 후 m 입력하는데 입력값이 알파벳이면 포켓몬 번호, 숫자면 포켓몬 이름

import sys # 아주 이걸 기본으로 깔고 가야지 열받네

input = sys.stdin.readline

n, m = map(int, input().split())

name = {}

for i in range(1, n+1): # 인덱스 값으로 검색하기 위해 1부터 n+1까지
    p = input().strip() # strip으로 공백제거
    # ... 오 딕셔너리 key:value 누가 생각 해 냈어 천잰데
    name[i] = p # 번호 : 이름 저장
    name[p] = i # 이름 : 번호 저장

for _ in range(m):
    check = input().strip()
    # isdigit, isalpha 기가막히네 ...
    if check.isdigit():
        print(name[int(check)])
    else:
        print(name[check]) # !!!