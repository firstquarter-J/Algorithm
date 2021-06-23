# 최대공약수(GCD : Greatest Common Divisor)

# 유클리드 호제법
# a를 b로 나눈 나머지를 r
# a와 b의 최대공약수는 b 와 r 의 최대공약수
# 즉 a와 b의 최대공약수는 b와 a%b 의 최대공약수

# gcd(24, 18) = gcd(18, 6) = gcd(6, 0)
# b 가 0 이 되는 순간이 최대 공약수 즉 6

a, b = map(int, input().split())

def gcd(a, b): # 최대공약수 구하는 함수
    while b != 0: # 최종적으로 b가 0이 될때까지 반복
        r = a % b # a를 b로 나눈 나머지를 r 에 저장
        a = b # b 값을 a 로
        b = r # r 값을 b 로 넣어 준 후 반복
    return a # b 가 0일 때 a 값 리턴

print(gcd(a, b)) # 최대공약수 출력

# 최소공배수(LCM : Least Common Multiple

# 최대 공약수를 G라고 했을 때
# a = G * x
# b = G * y
# 이다. G가 최대공약수 그 자체이기에, x, y는 서로소이다.
# 하튼, a * b = G * G * x * y   이다.
# 그럼 최소공배수는 a * b / G 이다.
# 놀랍지 않은가?

def lcm(a,b): # 최소공배수 구하는 함수
    lcm = (a * b) // gcd(a, b) # a * b 값에 a, b의 최대공약수를 나누면 최소공배수
    return lcm
print(lcm(a, b))


# import math # 사기...
# a, b = map(int, input().split())
# print(math.gcd(a, b))
# print(math.lcm(a, b))
