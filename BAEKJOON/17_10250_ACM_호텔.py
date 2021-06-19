


# h 층수 w 방수 n 손님수

# h 를 먼저 최대로 증가 시키며 손님수 차감하고
# 입력받은 h 값을 넘어서면 w 값 증가 시켜서 다시 h 값 증가
# 최종적으로 손님수 n 값이 0일 때 h, w 값 출력

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
