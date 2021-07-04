str = input()

check = 1

for i in range(len(str)):
    if str[i] != str[-(i+1)]:
        check = 0
        break
print(check)