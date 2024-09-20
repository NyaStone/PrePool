winnConditions = {
    "scissors": ["paper", "lizard"],
    "paper": ["rock", "spock"],
    "rock": ["lizard", "scissors"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

def rpsls(playOne: str, playTwo: str):
    if not playOne in winnConditions.keys() or not playTwo in winnConditions.keys():
        raise Exception("Illegal move played")
    if playTwo in winnConditions[playOne]:
        return 'Player 1 has won!'
    if playOne in winnConditions[playTwo]:
        return 'Player 2 has won!'
    return "Draw!"

print(rpsls('paper', 'spock'))