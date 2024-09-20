import random
import math
someList = []
for i in range(100):
    someList.append(math.floor(random.random()*100))
    
someList.sort(reverse=True)
print(someList)