a = int(input())

num = a
count = 0
while True:
    sum = (num // 10) + (num % 10) # 2 + 6 = 8 -> 6 + 8 = 14 -> 8 + 4 = 12 -> 4 + 2 = 6
    new = ((num % 10) * 10) + (sum % 10) # 60 + 8 -> 80 + 4 -> 40 + 2 -> 20 + 6
    count += 1
    if (new == a):
        break
    num = new
print(count)