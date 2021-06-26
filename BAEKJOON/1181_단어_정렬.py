n = int(input()) # 반복횟수 입력

w = [] # 입력받을 문자 넣을 배열 생성
for _ in range(n): # 입력받은 반복횟수만큼 반복
    w.append(input()) # 생성해 둔 배열에 붙여주고

set = set(w) # set 중복제거, 집합 자료형{}
list = list(set) # 다시 리스트로 변환

list.sort()
list.sort(key=len) # 정렬된 리스트 내부 문자열 길이 순으로 다시 정렬

for i in list:
    print(i)