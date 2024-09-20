import os

def listDir(path:str = os.path.dirname(__file__), prefix:str = ""):
    content = os.listdir(path)
    directories = list(filter(os.path.isdir, content))
    files = list(filter(lambda item: item not in directories, content))
    for item in files:
        itemPath = f'{path}/{item}'
        print(f'{prefix}{itemPath}')
    for item in directories:
        itemPath = f'{path}/{item}'
        print(f'{prefix}{itemPath}')
        listDir(itemPath, f'{prefix}\t')


listDir()