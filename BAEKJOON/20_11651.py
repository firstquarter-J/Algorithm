
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
    s[i] = [y[i], x[i]]



# num = int(input())
# x = [0 for i in range(num)]
# y = [0 for i in range(num)]
# a = [0 for i in range(num)]
# for i in range(num):
#     x[i], y[i] = map(int, input().split())
#     a[i] = [x[i], y[i]]
# b = sorted(a)
# for i in range(num):
#     b[i] = str(b[i])[1:-1]
#     b[i] = b[i].replace(',', '')
#     print(b[i])
