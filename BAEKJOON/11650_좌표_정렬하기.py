# n = int(input()) # 좌표 갯수 입력 받고
#
# a = []  # 2차원 리스트 생성을 위한 빈 리스트 생성 해 두고
# for _ in range(n): # n 만큼 반복
#     xy = list(map(int, input().split())) # xy 변수에 리스트 형태로 값 저장
#     a.append(xy) # 미리 생성해둔 리스트에 리스트로 입력받은 xy 저장
#
# a.sort() # a 리스트 sort 함수로 오름차순 정렬
# for i in a: # a 리스트 길이만큼 반복
#     print(i[0], i[1]) # i 번째의 인덱스0:x 인덱스1:y 출력

# 시 간 초 과 !?



num = int(input())
x = [0 for i in range(num)]
y = [0 for i in range(num)]
a = [0 for i in range(num)]
for i in range(num):
    x[i], y[i] = map(int, input().split())
    a[i] = [x[i], y[i]]
b = sorted(a)
for i in range(num):
    b[i] = str(b[i])[1:-1]
    b[i] = b[i].replace(',', '')
    print(b[i])