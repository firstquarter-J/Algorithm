# n개의 원판
# n-1개의 원판 ( 맨 밑 원판 제외 나머지 원판들 ) 을 1번에서 2번으로, 맨 밑 원판을 1번에서 3번으로
# 그 후 n-1개의 원판들을 다시 2번에서 3번으로

n = int(input())

def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, b, c)
        print(a, c)
        hanoi(n - 1, b, a, c)
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)