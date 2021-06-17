i = input().upper() # 입력받은 문자 대문자로

a = {} # 빈 딕셔너리 생성

# 딕셔너리에 값 넣는 반복문
for x in i: # 입력받은 문자 반복
    if x in a: # 반복해서 담긴 문자열 검증하여
        a[x] += 1 # 증
    else:
        a[x] = 1 # 없으면 1

result = 0 # 결과
count = 0 # 횟수

# 담겨있는 입력값 수 검증하는 반복문
for x in a: # 입력값 담겨있는 상태의 a 반복하여
    if a[x] > count: # 횟수보다 크다면
        result = x # 결과값 저장
    elif a[x] == count: # 같다면
        result = '?' # ? 출력

print(result)