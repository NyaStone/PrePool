import random
someList = []
for i in range(10):
    someList.append(random.random())

theMin = someList[0]
theMax = someList[0]
for someNumber in someList[1:]:
    theMax = max(theMax, someNumber)
    theMin = min(theMin, someNumber)

print(f'Min: {theMin}')
print(f'Max: {theMax}')