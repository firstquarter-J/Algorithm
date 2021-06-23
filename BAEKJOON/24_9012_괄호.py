# 괄호 문자열(Parenthesis String, PS)
# 올바른 괄호 문자열(Valid PS, VPS)

# () 괄호 숫자 각각 세서 같으면 yes 다르면 no - 매번 비교하면 비효율

# 괄호 나올 때 마다 변수 하나에 증, 감으로 0이면 yes 아니면 no 출력

# t = int(input())
#
# for _ in range(t):
#     ps = list(input())
#     count = 0
#     for i in ps:
#         if i == '(':
#             count = count + 1
#         elif i == ')':
#             count = count - 1
#         if count < 0:
#             print('NO')
#             break
#     if count > 0:
#         print('NO')
#     elif count == 0:
#         print('YES')

# 스택으로 풀이

# t = int(input())
#
# for _ in range(t):
#     stack = [] # 빈 배열 생성
#     ps = input() # 괄호 입력 받고
#     count = 0 # 배열 내 괄호 상태 체크 변수
#     for i in ps: # 입력받은 괄호들 하나씩 반복
#         if i == '(': # ( 면 스택에 넣고
#             stack.append(i)
#         elif i == ')': # ) 면
#             if len(stack) == 0: # 스택 길이가 0일 때 이미 글러 먹었으니
#                 print('NO') # NO 출력
#                 check = 1 #
#                 break
#             else:
#                 stack.pop(-1) # 스택 끝 값 추출
#
#     if len(stack) != 0 and check == 0: # 스택 길이가 0 아니면서 체크변수가 0이면 괄호 숫자가 다르니
#         print('NO')
#     elif len(stack) == 0 and check == 0: # 스택이 비었고 체크도 0이면
#         print('yes')
# 런타임 에러

t = int(input())

for _ in range(t):
    stack = []
    ps = input()
    check = True
    for i in ps:
        if i == '(':
            stack.append(i)
        else:
            if not stack: # ) 들어왔는데 비어있으면 시작부터 글러먹었으니 false
                check = False
                break
            if stack[-1] != '(': # 스택의 끝 값이 ( 아니여도 글러먹었으니 false
                check = False
                break
            else: # 스택이 비어있지 않고 ( 값이 들어 있다면 ( 값 빼서 다시 비워 줘
                stack.pop()
    if check and not stack: # 입력받은 ps 값 전부 검증하고 나온 후 체크 값이 트루고 스택이 비어있지 않을 때
        print('YES')
    else:
        print('NO')
