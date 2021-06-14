# h = 1
# m = 10

h, m = map(int, input().split())

if (m>44):
    m = m - 45
elif (h<1):
    h = 23
    m = m + 60 - 45
elif (m<45):
    h -= 1
    m = m + 60 - 45

print(h, m)

# 천재인가...?
# a,b=map(int,input().split())
# c=a*60+b-45
# print(c//60%24, c%60)