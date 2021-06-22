# deque = 양방향 큐
# 앞, 뒤로 큐 내의 요소 출,삭 가능
# rotate 사용 - 검색 - from collection import deque

# 문제가 요구하는 동작

# 1. 큐의 왼쪽만 추출
# 2. 큐 왼쪽 뽑아 오른쪽 삽입
# 3. 큐 오른쪽 뽑아 왼쪽 삽입
# 큐 크기와 뽑을 갯수 입력
# 뽑고자 하는 수 위치 입력
# 큐를 옮긴 횟수 카운트 하여 출력

# 첫 줄에 큐의 크기 N 뽑을 수 M   # 10 3
# 둘째 줄에 뽑을 수 위치    # 2 9 5
# 위 입력값의 출력은 8

from collections import deque
n, m = map(int, input().split()) # 큐 크기 n, 뽑을 수 m 입력
num = list(map(int, input().split())) # 뽑을 수의 위치 입력

count = 0 # 옮긴 횟수 저장 변수
q = deque() # 빈 deque 생성
for i in range(1, n + 1): # 1부터 n+1 까지 큐에 값 넣고
    q.append(i)

for n in num: # 입력받은 뽑을 수를 큐 크기만큼 반복

    id = q.index(n) # id 변수에 q의 n번째 값을 인덱스로 저장( 저장된 인덱스 값으로 비교하여 검색 위해 )
    if id == 0: # id 값이(index) 0 이면? ( 큐의 맨 앞에 있다면? )
        q.popleft() # 큐의 제일 왼쪽값 추출 ( 이동 불필요 )

    else: # 0이 아니면 찾을 값 까지의 최단 거리를 계산하기 위해
        #뒤에서 이동할지 len(q) - id
        if id < len(q) - id: # 큐 길이에서 id 값(입력받은 위치 인덱싱 한 id 변수) 차감한 값 보다 id 값이 작다면?
            count += id # 카운트에 id 값 저장
            q.rotate(-id) # 큐 위치 맨 앞으로 이동
            q.popleft() # 큐 좌측값 추출
        #앞에서 이동할지
        else: # 큐 - id 값이 작지 않다면?
            count += len(q) - id # 큐 길이에서 id 값 차감 하여 count 저장
            q.rotate(len(q) - id) # 큐 길이에서 id값 차감하여 이동
            q.popleft() # 큐 좌측값 추출
print(count)