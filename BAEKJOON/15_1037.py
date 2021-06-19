
# 첫 입력 i 로 약수 갯수 입력받고
# 두번째 입력으로 약수 입력 받아서
# 약수들의 배수를 구해?

# 약수가 전부 주어지니 최소값과 최댓값을 곱하면 됨!

n = int(input()) # 약수 개수 를 입력받는데 무슨 의미가...?

i = list(map(int, input().split())) # list, map 으로 입력받은 약수들 리스트에 저장

min = min(i) # 작은값 저장
max = max(i) # 큰 값 저장

print(min * max) # 최소값 * 최대값 = ? 공배수

# .sort() 함수로 정렬하여 배열 처음값, 마지막값 뽑아 사용 가능
# x = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(a[0]*a[-1])