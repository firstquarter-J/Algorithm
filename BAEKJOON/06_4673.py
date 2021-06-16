# number = range(1, 10000)
#
# d = set()
#
# for num in number:
#     for n in str(num):
#         num += int(n)

def d(n):  # 반복시키는 함수
    result = n  # 결과
    for x in list(str(n)):  # 숫자 한자리씩 문자열로 분리
        result += int(x)  # 첫 수 + 분리시킨 문자열 숫자로 변환하여 더하고
    return result  # 결과 리턴


성자 = []  # 생성자 맹글기
for x in range(10001):  # 만번까지 반복
    성자.append(d(x))  # append 함수 이용해서 d함수 호출 후 배열에 넣기

for x in range(1, 10001):
    if x in 성자:  # 배열에 담긴 생성자 반복해서 변수 x에 담고
        continue  # 계속
    else:
        print(x)  # 끝나면 출력