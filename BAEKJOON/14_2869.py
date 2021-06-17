# V 높이
# A 낮에 올라가
# B 밤에 내려와

# 입력 A B V

# 반복문 한 번당 A - B 해서 변수에 저장, 카운트 변수 +1
# 저장된 변수가 V 와 같으면 끝내고 카운트 변수 출력
# 실패!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 마지막 날은 내려오지 않는다가 핵심
# (a-b) * day + a = v

a = 2  # 증
b = 1  # 감
v = 5  # 최종

# ((v-a) / (a-b)



a, b, v = map(int, input().split())

if (v - b) % (a - b) == 0:
    print((v - b) // (a - b))
else:
    print((v - b) // (a - b) + 1)

# go = 0
# count = 0
#
# while 1:
#     go = a - b
#     count += 1
#     if v == go:
#         break
# print(count)
