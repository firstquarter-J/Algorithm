
# 2차원 평면 위의 점 N개가 주어진다.
# 좌표를 y좌표가 증가하는 순으로,
# y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# y 증가 순으로 우선 정렬
# y 값이 같으면 x 순으로 정렬

# 정렬할 좌표 갯수 입력받고
n = int(input())

# x y 값을 배열로 입력 받아서
# 배열 내의 인덱스로 입력 받은 값들 순차적으로 비교하여 정렬
# y 배열에 동일한 값이 있다면 그 동일한 값들의 x 값들을 비교하여 정렬

# 리스트 표현식으로 2차원 리스트 만들기 참조
x = [0 for i in range(n)] # 오... 이런 방법도 있어?
y = [0 for i in range(n)]

s = [0 for i in range(n)] # x y 를 저장할 배열

for i in range(n):
    x[i], y[i] = map(int, input().split())
    s[i] = [x[i], y[i]]
sx = sorted(x)
sy = sorted(y)

for i in range(n):
    print(sx[i], sy[i])



n = int(input()) # 좌표 갯수 입력 받고

a = []  # 빈 배열 생성 해 두고
for _ in range(n): # 입력 받은 n 만큼 반복하며
    x, y = map(int, input().split()) # x, y 에 입력 받고
    a.append([y, x]) # 미리 생성해둔 a 배열에 y 값을 앞에 저장하여

s = sorted(a) # y 값 기준으로 정렬

for y, x in s: # y, x 로 저장된 s 배열 길이만큼 반복하여
    print(x, y) # 출력은 x, y 순으로
