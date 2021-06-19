f = int(input())
l = int(input())

sosu = []
for num in range(f, l+1): # 입력받은 처음값~끝값까지 반복하여 num 변수에 저장
    count = 0 # 소수인지 판단하기 위해 나누어 떨어졌을때 +1 하는 변수
    if num > 1: # 입력값이 1보다 클때 ( 소수는 2부터 )
        for i in range(2, num): # 2부터 num 까지 반복하며 i 증가시켜서
            if num % i == 0: # num 이 i 로 나누어 떨어지면
                count += 1 # 카운트 증가시켜서
                break # num 이 i 로 나누어 졌다? 소수 아니니 멈춰!
        if count == 0: # num 이 i 로 나누어 떨어지지 않았다면?
            sosu.append(num) # sosu 리스트에 현재의 num 값 추가

if len(sosu) > 0: # len 함수로 소수 리스트 길이 검증하여 0보다 크면
    print(sum(sosu)) # sum 함수로 소수 리스트 값 더하여 출력
    print(min(sosu)) # min 함수로 소수 리스트의 최소값 찾아내 출력
else:
    print(-1) # 소수 리스트에 소수가 없으면 -1 출력

