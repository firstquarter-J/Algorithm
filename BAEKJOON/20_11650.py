n = int(input())

li = []  # 2차원리스트
for _ in range(n):
    xy = list(map(int, input().split()))
    li.append(xy)

li.sort()
for i in li:
    print(i[0], i[1])


# 2차원 리스트 형태로 저장하기 위해 리스트 한개를 만들어준다.
#
# for문을 이용하여 입력된 x, y 숫자를 리스트에 저장해준다.
#
# sort함수를 이용하여 오름차순으로 정렬
