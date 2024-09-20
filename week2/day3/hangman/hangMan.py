from functools import reduce
import math
import random
import re
import json

import os

# Scrabble letter scores to aproximate the difficulty of the word to guess
letterScore = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10
}

class WordGenerator:
    def __init__(self, fileName: str = "words.json"):
        if not fileName:
            fileName = "words.json"
        # Find the directory in which the current script resides:
        self.file_path = f'{os.path.dirname(os.path.realpath(__file__))}/{fileName}'
        with open(self.file_path) as file:
            words = json.load(file)
        self.words = words
        difficulties = list(map(lambda word: self.difficulty(word) ,list(self.words.keys())))
        self.maxDifficulty = max(difficulties)
        self.minDifficulty = min(difficulties)

    def getRandom(self):
        return random.choice(list(self.words.keys()))
    
    def write(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.words, file, ensure_ascii=False, indent=4)

    def getHighScore(self, word:str):
        return self.words[word.lower()]
    
    def setHighScore(self, word: str, score: int):
        self.words[word.lower()] = score
        self.write()

    def difficulty(self, word: str):
        return reduce(lambda acc, letter: acc + letterScore[letter], list(word.upper()), 0)
    
    def difficultyTitle(self, word:str):
        difficultyScore = self.difficulty(word)
        difficultySplit = self.maxDifficulty - self.minDifficulty
        if difficultyScore > difficultySplit * 0.75 + self.minDifficulty:
            return 'Extreme'
        if difficultyScore > difficultySplit * 0.5 + self.minDifficulty:
            return 'Hard'
        if difficultyScore > difficultySplit * 0.25 + self.minDifficulty:
            return 'Normal'
        return 'Easy'



class Hangman:
    def __init__(self, word: str) -> None:
        self.word = word.upper()
        self.wordLength = len(self.word)
        self.triedLetters = []
        self.score = 0

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

    def gameTurn(self, guess: str):
        if len(guess) == 1:
            self.tryLetter(guess)
        else:
            self.tryWord(guess)

    def restart(self, newWord: str):
        self.word = newWord.upper()
        self.wordLength = len(newWord)
        self.triedLetters = []
        self.score = 0
        

class CheatEngine:
    def __init__(self, wordGen: WordGenerator, game: Hangman):
        self.wordGen = wordGen
        self.frequencyString = "etaoinshrdlcumwfgypbvkjxqz".upper()
        self.triedWords = []
        # filtering the dictionary by wordlength 
        self.words = list(filter(lambda item: len(item) == game.wordLength, list(wordGen.words.keys())))
        self.game = game

    def restart(self):
        self.triedWords = []
        # filtering the dictionary by wordlength 
        self.words = list(filter(lambda item: len(item) == self.game.wordLength, list(self.wordGen.words.keys())))

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
        print(f'Word matching /{regex}/')
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
            return f'Try "{possibleWords[0]}"'
        # else use frequency analysis on the possible words to find the letter used in most words 
        # aka map to each letter in how many of the possible words it is present
        frequencyAnalysis = {}
        for letter in self.possibleLetters():
            count = 0
            for word in possibleWords:
                if letter in word.upper():
                    count +=1
            frequencyAnalysis[letter] = count
        # find the most used letter(s)
        maxOccurence = max(frequencyAnalysis.values())
        letters = list(filter(lambda letter: frequencyAnalysis[letter] == maxOccurence, frequencyAnalysis))
        # if len(letters) == 1:
        hitRate = math.floor((maxOccurence / len(possibleWords))*100)
        return f'("{letters[0]}" {hitRate}%)'