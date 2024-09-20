import random
import math
someList = []
for i in range(100):
    someList.append(math.floor(random.random()*100))

for someNumber in someList:
    if someNumber < 7:
        print(someNumber)