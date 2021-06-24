# while True:
#     s = input() # 문장 입력 받고
#     if s == '.': # 마침표 입력시 종료
#         break
#     stack = [] # 빈 스택 생성
#     check = True # 스택 내부 검증 변수 생성
#     for i in s:
#         if i == '(' or '[': # 여는 기호면
#             stack.append(i) # 배열에 붙여주고
#         elif i == ')': # ) 닫는 기호면
#             if not stack or stack[-1] == '[': # 스택이 비었거나 여는 기호와 맞지 않으면
#                 check = False # 글러먹었으니 멈추고
#                 break
#             elif stack == '(': # 서로 맞는 여는 기호가 들어있으면
#                 stack.pop() # 스택에서 그 기호 빼서 비워주고
#         elif i == ']': # ] 닫는 기호일때
#             if not stack or stack[-1] == '(': # 스택이 비었거나 여는 기호와 맞지 않으면
#                 check = False # 펄스 저장 후 멈춰
#                 break
#             elif stack == '[': # 여는 기호와 짝이라면
#                 stack.pop() # 스택에서 제거
#     if check == True and not stack: # 검증 변수가 트루고 스택이 비어있으면
#         print('yes')
#     else:
#         print('no')
# 실 패

# while True:
#     s = input() # 문장 입력
#     if s == '.': # 마침표 있으면 종료
#         break
#     stack = [] # 입력받는 기호 넣을 빈 스택
#     check = True # 스택 안에 기호 있는지 검증 변수
#
#     for i in s:
#         if i == '(' or '[': # 여는 기호 들어왔을때
#             stack.append(i) # 스택에 붙여주고
#         elif i == ')': # 닫는 기호 들어왔을때
#             if len(stack) == 0: # 스택이 비어있다면
#                 check = False # 짝이 안 맞으니 False
#                 break
#             if stack[-1] == '(': # 닫는 기호 들어왔는데 스택에 여는 기호 들어가 있으면
#                 stack.pop() # 여는 기호 빼 줌
#             else:
#                 check = False
#                 break
#
#         elif i == ']':
#             if len(stack) == 0:
#                 check = False
#                 break
#             if stack[-1] == '[':
#                 stack.pop()
#             else:
#                 check = False
#                 break
#
#     if check and not stack:
#         print('yes')
#     else:
#         print('no')
# 실패


while True:
    s = input() # 문장 입력
    check = True # 문장 내 기호 짝 맞는지 검증 변수
    stack = [] # 기호 저장할 변수
    if s == '.': # 마침표면 종료
        break
    for i in s:
        if i in '([': # 괄호 ( [ 들어오면 스택에 붙여주고
            stack.append(i)
        elif i == ')': # 닫는괄호 ) 일때
            if stack and stack[-1] == '(': # 스택에 ( 있다면
                stack.pop() # 추출
            else: # 없다면
                check = False # 짝이 안 맞으니 False
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                check = False
                break
    if not stack and check:
        print('yes')
    else:
        print('no')