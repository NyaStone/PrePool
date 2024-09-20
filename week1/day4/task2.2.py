data = input('Enter something: ')

res = ""
for character in data:
    res += f'{character}{character}'

print(res)

