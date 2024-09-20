someList = []

for i in range(1,11):
    someList.append(i)

res = 1

for someNumber in someList:
    res *= someNumber

print(res)