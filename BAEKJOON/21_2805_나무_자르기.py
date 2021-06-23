# 입력 나무 수 n 가져갈 나무 길이 m
# 두번째 입력 나무 높이
# 출력 적어도 m미터 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값 출력

# Binary search ( 이진 탐색 )

# 벌목 높이를 움직여 필요 나무 길이를 채우는지 검증
#
# 1. 가장 짧은 길이 1을 start, 나무 중 가장 긴 길이를 end
# 2. 이분탐색이 끝날 때 까지 while
#
# 3. mid를 start와 end의 중간으로 두고, 모든 값에서 mid를 빼 총 어느정도 길이의 벌목된 나무가 나오나 살펴보고
# 4-1. 벌목 나무가 목표치 이상이면 mid+1를 start로 두고 다시 while
# 4-2. 벌목나무가 목표치 이하면 mid-1을 end로 두고 다시 while
# 5. start와 end가 같아지면 : 조건을 만족하는 최대의 나무 절단 높이를 찾아서 탈출
# 6. 결과값인 end출력

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)  # 이분탐색 검색 범위 설정

while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start + end) // 2

    log = 0  # 벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid

    # 벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
