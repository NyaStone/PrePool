import random
import math
import time

print('Generating the list...')
generationStartTime = time.time()
someList = []
for i in range(1000000):
    someList.append(math.floor(random.random()*10000))
generationDoneTime = time.time()
print(f'Done generating in {generationDoneTime - generationStartTime}s')
someList.sort()
print(f'Finished sorting in {time.time() - generationDoneTime}s')