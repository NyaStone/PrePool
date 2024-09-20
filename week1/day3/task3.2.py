username = input("What's your name mah boi? ")
if username == "":
    username = "World"
username = username.lower().title()
print(f'Hello {username}')