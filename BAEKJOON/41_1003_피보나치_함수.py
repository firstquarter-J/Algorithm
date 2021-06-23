# 문제가 요구하는 동작
# f(2) = f(1) + f(0)

# 한번 구한 수는, 다시 구하지 않고 값을 저장하여 이용할 수 있도록
# DP(Dynamic Programming) 개념을 이용

# 입력
# 테스트케이스 T 입력 후 f(n) 입력
# 0, 1 이 몇 번 씩 호출되는지 출력

# 문제 규칙
# 주어진 n이 0일 경우 0 return, n이 1일 경우 1 return 만 제외
# 그 외엔 one(n-1) + zero(n-2) return
# N : 0 1 2 3 4 5 6 7 8
# 0 : 1 0 1 1 2 3 5 8 13
# 1 : 0 1 1 2 3 5 8 13 21

arr = [0, 1]
for i in range(1, 40):
    arr.append(arr[i-1]+arr[i])

t = int(input())

for _ in range(t):
    ff = int(input())
    if(ff == 0):
        print("1, 0")
    elif(ff == 1):
        print("0, 1")
    else:
        print(arr[ff-1], arr[ff])
