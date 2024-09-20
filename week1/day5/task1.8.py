someList = [1, 2, 3, 4, 5, 6, 7, 8]

reversedList = []

for i in range(len(someList) -1, -1, -1):
    reversedList.append(someList[i])

print(reversedList)