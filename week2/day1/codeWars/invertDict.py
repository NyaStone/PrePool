from typing import Dict, List

def invertDict(someDict: Dict[str, str]):
    res: Dict[str, List[str]] = {}
    for key, value in someDict.items():
        if not value in res:
            res[value] = []
        res[value].append(key)
    return res


someDict = {'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}
print(invertDict(someDict))