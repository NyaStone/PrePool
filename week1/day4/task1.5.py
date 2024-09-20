data = ""
while not data.isdigit():
    data = input("Enter a number: ")

data = int(data)

if data == 42:
    print(f'"{data}" is OK.')
elif data <= 21:
    print(f'"{data}" is OK.')
elif data % 2 == 0:
    print(f'"{data}" is OK.')
elif data / 2 < 21:
    print(f'"{data}" is OK.')
elif data % 2 == 1 and data >= 45:
    print(f'"{data}" is OK.')
else:
    print("SAIK, it's a wrong number!")