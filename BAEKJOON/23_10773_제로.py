n = int(input()) # 배열에 들어갈 정수 갯수
arr = [] # 스택 배열 생성
for i in range(n):
    ip = int(input()) # 배열에 들어갈 정수 입력
    if ip == 0: # 입력값이 0이면 전 값 삭제
        arr.pop()
    else: # 0이 아닌 정수면 스택 배열에 추가
        arr.append(ip)
print(sum(arr)) # sum 함수로 배열 더해서 출력