someList = [1,2,3,4,5]



def removeLast(someList: list):
    if len(someList) == 0:
        return
    someList.pop()



removeLast(someList)
print(someList)
