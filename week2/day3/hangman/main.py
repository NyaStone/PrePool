import pygame
import time 
import os
import sys
from textInput import *
from hangMan import *
from drawStickman import *
from textSprite import *
from timerComponent import *
from button import *

current_directory = os.path.dirname(os.path.abspath(__file__))

fileName = None
for index, option in enumerate(sys.argv):
    if option in ['-file', '-f']:
        if len(sys.argv) > index + 1:
            fileName = sys.argv[index + 1]
        else:
            raise Exception('File option given without a file')

screenSize = (600, 600)

if pygame.get_sdl_version()[0] == 2:
    pygame.mixer.pre_init(44100, 32, 2, 1024)
pygame.init()
if pygame.mixer and not pygame.mixer.get_init():
    print("Warning, no sound")
    pygame.mixer = None

wordGen = WordGenerator(fileName)
game = Hangman(wordGen.getRandom())

# print(wordGen.difficulty(game.word), wordGen.difficultyTitle(game.word), f'{wordGen.minDifficulty}-{wordGen.maxDifficulty}')
timer = Timer(position= (10, 10),
            margin = 26,
            width= 100,
            fontSize= 30,
            fontColor=(0, 0, 0),
            backColor=(255, 255, 255))


cheat = None
for option in sys.argv:
    if option in ['-cheat', '-c']:
        cheat = CheatEngine(wordGen, game)
        print(cheat.prediction())



screen = pygame.display.set_mode(screenSize)


background = pygame.image.load(os.path.join(current_directory, 'garydosBG.jpg')).convert()
background = pygame.transform.scale(background, screenSize)
background.set_alpha(100)


def wordCheatFilter(word):
    prediction = f' {cheat.prediction()}' if cheat and not game.hasWon() else ''
    return f'{word}{prediction}'

wordView = TextSprite(text=game.getWord(),
                    textFilter=wordCheatFilter,
                    position= (50, 500),
                    margin = 26,
                    width= 0,
                    fontSize= 35,
                    fontColor=(0, 0, 0),
                    backColor=(255, 255, 255))
scoreView = TextSprite(text=str(game.score),
                    position= (wordView.getWidth() + 25 + wordView.margin, 500),
                    margin = 26,
                    width= 0,
                    fontSize= 35,
                    fontColor=(0, 0, 0),
                    backColor=(255, 255, 255))
difficultyView = TextSprite(text = wordGen.difficultyTitle(game.word),
                            position = (320, 150),
                            margin = 26,
                            width= 0,
                            fontSize= 35,
                            fontColor=(0, 0, 0),
                            backColor=(255, 255, 255))

def advanceGameState(someString: str):
    if not someString:
        return
    game.gameTurn(someString)
    wordView.setText(game.getWord())
    scoreView.position = (wordView.getWidth() + 25 + wordView.margin, 500)
    scoreView.setText(str(game.score))


textbox = TextInput(callback = advanceGameState,
                    position= (50, 70),
                    margin = 26,
                    width= 500,
                    fontSize= 40,
                    fontColor=(0, 0, 0),
                    backColor=(255, 255, 255),
                    active=True)

def restartGame():
    game.restart(wordGen.getRandom())
    if cheat:
        cheat.restart()
    wordView.setText(game.getWord())
    difficultyView.setText(wordGen.difficultyTitle(game.word))
    timer.restart()
    scoreView.position = (wordView.getWidth() + 25 + wordView.margin, 500)
    scoreView.render_text()
    textbox.reset()
    


restartButton = Button( text = "Restart",
                        callback = restartGame,
                        position = (440, 150),
                        margin = 26,
                        width= 0,
                        fontSize= 35,
                        fontColor=(0, 0, 0),
                        backColor=(225, 225, 225))


# Sprite grouping to make the display loop easier
group = pygame.sprite.Group((textbox, 
                             wordView, 
                             scoreView,
                             difficultyView,
                             restartButton,
                             timer))


    
# display loop
qutting = False
    
while not qutting:
    # second condition is to avoid having it run multiple times
    if game.hasWon() and not textbox.locked:
        textbox.locked = True
        timer.stop()
        highScore = wordGen.getHighScore(game.word)
        textbox.text = f'Well done! New highscore!'
        if not highScore:
            wordGen.setHighScore(game.word, game.score)
        elif game.score < highScore:
            wordGen.setHighScore(game.word, game.score)
        else:
            textbox.text = f'Well done! Highscore is {highScore} for this word.'
        textbox.render_text()

    events = pygame.event.get()
    group.update(events)
    screen.fill((255,255,255))
    screen.blit(background, (0, 0))
    draw_stickman(screen, game.score, (225, screenSize[1]//2))
    group.draw(screen)
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and game.hasWon() and not restartButton.rect.collidepoint(event.pos):
            qutting = True
        if event.type == pygame.QUIT:
            qutting = True
    pygame.display.update()

