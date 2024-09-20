invitedPeople = ["Gaylord", "Jaques", "Michel"]

yourName = input("What is your name? ")

if yourName in invitedPeople:
    print(f'Welcome in {yourName}')
else:
    print("Get lost!")