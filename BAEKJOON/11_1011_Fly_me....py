# 1
# 11
# 111
# 121
# 1211
# 1221
# 12211
# 12221
# 12321
# 123211
# 123221
# 123321
# 1233211
# 1233221
# 1233321
# 1234321

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때,
            move += 1
    print(count)

    # https: // ooyoung.tistory.com / 91