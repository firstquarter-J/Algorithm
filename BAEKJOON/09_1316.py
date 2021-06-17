# n = int(input())
#
# result = 0
#
# for x in range(n): # n 변수로 입력받은 숫자 만큼 반복
#     word = input() # 문자열 입력
#     for y in range(len(word)-1):
#         if word.find(word[y]) > word.find(word[y]+1):
#             result -= 1
#             break
# print(result)

n = int(input())

result = n # 입력받는 문자의 수를 그대로 저장하여 중복검사 하며 차감하기 위한 결과 변수

for _ in range(n): # 입력받은 n 변수만큼 반복
    word = input() # 문자열 입력받고
    for i in range(len(word)-1): # 받은 문자열 길이의 -1만큼 반복 ( 인덱스는 0부터 시작하니까 )
        if word[i] != word[i+1]: # 인덱스 0번째 문자와 1번째 문자가 같지 않을 때
            if word[i] in word[i+1:]: # 인덱스 0번째 문자와 1번째 이후의 문자들 중복 검증하여
                result -= 1 # 결과값 감소
                break # 중지 시키고 다음 반복으로 넘어감
print(result)