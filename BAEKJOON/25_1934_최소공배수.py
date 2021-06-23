# 최대공약수(GCD : Greatest Common Divisor)

# 유클리드 호제법
# a를 b로 나눈 나머지를 r
# a와 b의 최대공약수는 b 와 r 의 최대공약수
# 즉 a와 b의 최대공약수는 b와 a%b 의 최대공약수

# 최소공배수(LCM : Least Common Multiple

# 최대 공약수를 G라고 했을 때
# a = G * x
# b = G * y
# 이다. G가 최대공약수 그 자체이기에, x, y는 서로소이다.
# 하튼, a * b = G * G * x * y   이다.
# 그럼 최소공배수는 a * b / G 이다.
# 놀랍지 않은가?

t = int(input())

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    lcm = (a * b) // gcd(a, b)
    return lcm

for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))

# import math # 사기...
# a, b = map(int, input().split())
# print(math.gcd(a, b))
# print(math.lcm(a, b))