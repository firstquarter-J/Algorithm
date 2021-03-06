# 소수 구하기
# n=100
#
# def isPrime(a):
#   if(a<2):
#     return False
#   for i in range(2,a):
#     if(a%i==0):
#       return False
#   return True
#
# for i in range(n+1):
#   if(isPrime(i)):
#     print(i)
# sqrt ? 루트

# 에라토스테네스의 체
# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n
#
#     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:  # i가 소수인 경우
#             for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
#                 sieve[j] = False
#
#     # 소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]


import math

n = int(input())

while n != 0:
    array = [True for _ in range(2 * n + 1)]

    for i in range(2, int(math.sqrt(2 * n)) + 1):
        if array[i]:
            j = 2
            while i * j <= 2 * n:
                array[i * j] = False
                j += 1

    count = 0

    for i in range(n + 1, 2 * n + 1):
        if array[i]:
            count += 1

    print(count)

    n = int(input())
