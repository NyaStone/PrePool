from functools import reduce
import random
import sys
import re

import os




class WordGenerator:
    def __init__(self):
        # Find the directory in which the current script resides:
        file_dir = os.path.dirname(os.path.realpath(__file__))
        with open(f'{file_dir}/words.txt') as file:
            words = file.readlines()
        self.words = list(set([word.strip() for word in words]))

    def getRandom(self):
        return random.choice(self.words)




class Hangman:
    def __init__(self, word: str) -> None:
        self.word = word.upper()
        self.wordLength = len(self.word)
        self.triedLetters = []
        self.score = 0

    def startGameLoop(self, cheat = None):
        while not self.hasWon():
            self.gameTurn(cheat)
        print(f'You found the word "{self.word}" with a score of {self.score}')

    def hasWon(self):
        victory = True
        for character in self.word:
            victory = victory and character in self.triedLetters
        return victory

    def getWord(self):
        res = ""
        for character in self.word:
            if not character.isalpha() or character in self.triedLetters:
                res += f'{character} '
            else:
                res += "_ "
        return res

    def tryLetter(self, letter: str):
        if len(letter) > 1:
            raise Exception("Too many characters")
        if len(letter) < 1:
            raise Exception("Too few characters")
        letter = letter.upper()
        count = self.word.count(letter)
        if not letter in self.triedLetters:
            self.triedLetters.append(letter)
        if count == 0:
            self.score += 3
        elif not self.hasWon():
            self.score += 1
        

    def tryWord(self, word:str):
        if len(word) < 2:
            raise Exception("Too few characters")
        word = word.upper()
        if word != self.word:
            self.score +=5
            return
        for character in self.word:
            if not character in self.triedLetters:
                self.triedLetters.append(character)

    def gameTurn(self, cheat = None):
        someTry = ""
        while len(someTry) == 0 or not someTry.isalpha():
            prediction = ""
            if cheat:
                prediction = f'({cheat.prediction()})\n'
            someTry = input(f'{self.getWord()}/ Score: {self.score} / Tried: {self.triedLetters}\n{prediction}')
        if len(someTry) == 1:
            self.tryLetter(someTry)
        else:
            self.tryWord(someTry)
        

class CheatEngine:
    def __init__(self, wordGen: WordGenerator, game: Hangman):
        self.frequencyString = "etaoinshrdlcumwfgypbvkjxqz".upper()
        self.triedWords = []
        # filtering the dictionary by wordlength 
        self.words = list(filter(lambda item: len(item) == game.wordLength, wordGen.words))
        self.game = game

    def failWord(self, someWrod: str):
        self.triedWords.append(someWrod)

    def possibleWords(self):
        wordState = self.game.getWord()
        # generating a regex based on the the already guessed letters
        forbidenLetters = reduce(lambda acc, letter: acc + letter, self.game.triedLetters, '')
        if len(forbidenLetters) == 0:
            forbidenLetters = '.'
        else:
            forbidenLetters = f'[^{forbidenLetters}]'
        knownWord = wordState.replace(" ", "")
        knownWord = knownWord.replace("_", forbidenLetters)
        regex = rf'^{knownWord}$'
        print(regex)
        res = []
        for word in self.words:
            if re.match(regex, word.upper()):
                res.append(word)
        return res

    def possibleLetters(self):
        letters = self.frequencyString
        for letter in self.game.triedLetters:
            letters = letters.replace(letter, "")
        return letters

    def prediction(self):
        # get a list of possible words
        possibleWords = self.possibleWords()
        # if there is only one suggest it
        if len(possibleWords) == 1:
            return f'You should try "{possibleWords[0]}"'
        # else use frequency analysis on the possible words to find the letter used in most words 
        # aka map to each letter in how many of the possible words it is present
        frequencyAnalysis = {}
        for letter in self.possibleLetters():
            count = 0
            for word in possibleWords:
                if letter in word:
                    count +=1
            frequencyAnalysis[letter] = count
        # find the most used letter(s)
        maxOccurence = max(frequencyAnalysis.values())
        letters = list(filter(lambda letter: frequencyAnalysis[letter] == maxOccurence, frequencyAnalysis))
        # if len(letters) == 1:
        return f'You should try "{letters[0]}"'
            
        


wordGen = WordGenerator()
game = Hangman(wordGen.getRandom())
cheat = None
if len(sys.argv) > 1 and sys.argv[1] == '-cheat':
    cheat = CheatEngine(wordGen, game)
game.startGameLoop(cheat)