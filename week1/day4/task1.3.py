data = ""
while not data.isdigit():
    data = input("Enter a number: ")

data = int(data)

if data == 0:
    print(f'"{0}" is neither even nor odd.')
elif data % 2 == 0:
    print(f'"{data}" is even.')
else:
    print(f'"{data}" is odd.')