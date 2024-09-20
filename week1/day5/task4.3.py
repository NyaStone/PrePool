meetings = []

meetings.append(["Monday", "3:30 PM", "Joe", "Mama"])
meetings.append(["Tuesday", "9:15 AM", "Gaylord", "Samantha"])
meetings.append(["Thursday", "1:30 PM", "Joe", "Samantha", "Gaylord"])


def displayMeetings(person: str):
    for meeting in meetings:
        if person in meeting[2:]:
            print(meeting)

user = input("What's your name? ")

displayMeetings(user)