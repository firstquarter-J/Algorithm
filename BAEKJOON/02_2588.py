#제출본

a = int(input())
b = int(input())

B = b % 10
BB = int((b % 100 - B) / 10)
BBB = int((b - (B+BB)) /100)

result1 = a * B
result2 = a * BB
result3 = a * BBB
result = a * b

print(result1)
print(result2)
print(result3)
print(result)

# a = input()
# b = input()
#
# c = int(a) * int(b[2])
# d = int(a) * int(b[1])
# e = int(a) * int(b[0])
# f = int(a) * int(b)
#
# print(c)
# print(d)
# print(e)
# print(f)