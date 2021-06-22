
# 문제가 요구하는 동작
# f(2) = f(1) + f(0)

# 한번 구한 수는, 다시 구하지 않고 값을 저장하여 이용할 수 있도록
# DP(Dynamic Programming) 개념을 이용

# 입력
# 테스트케이스 T 입력 후 f(n) 입력
# 0, 1 이 몇 번 씩 호출되는지 출력
t = int(input())
# 문제 규칙
# 주어진 n이 0일 경우 0 return, n이 1일 경우 1 return 만 제외
# 그 외엔 fi(n-1) + fi(n-2) return
# N : 0 1 2 3 4 5 6 7 8
# 0 : 1 0 1 1 2 3 5 8 13
# 1 : 0 1 1 2 3 5 8 13 21

# n = 3 -> 1, 2
for _ in range(t): # 입력받은 테스트 케이스만큼 반복
    n = int(input()) # 테스트할 정수 입력
    fi0 = 1 # 0 출력되는 횟수 검증
    fi1 = 0 # 1 출력되는 횟수 검증
    temp = 0 # 임시 저장 변수
    for _ in range(n): # 입력받은 정수만큼 반복하며
        temp = fi1 # fi1 임시 저장
        fi1 = fi1 + fi0 # fi1 + fi0 합하여 저장
        fi0 = temp # f0 에 f1 저장
    print(fi0, fi1)

# n = 3의 경우
# temp = 0
# fi1 = 0 + 1 = 1
# fi0 = 0
#
# temp = 1
# fi1 = 1 + 0 = 1
# fi0 = 1
#
# temp = 1
# fi1 = 1 + 1 = 2
# fi0 = 1
# 결과 1 2