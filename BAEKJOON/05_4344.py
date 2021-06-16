p = int(input())

for x in range(p): # range (받은 길이만큼 반복)
    num = list(map(int, input().split(' '))) # list + map 으로 묶어서 input.split 각 배열에 저장
    avg = sum(num[1:]) / num[0] # sum 으로 슬라이싱 된 배열값 합쳐서 나눔
    count = 0 # 학생 수 카운트
    for score in num[1:]:
        if score > avg:
            count += 1
    rate = count/num[0] * 100
    print(f'{rate:.3f}%') # f스트링으로 rate: .3f 소숫점 세자리까지 백분율 표시