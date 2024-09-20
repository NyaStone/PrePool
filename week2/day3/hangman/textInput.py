import pygame
from typing import Callable

class TextInput(pygame.sprite.Sprite):
    def __init__(self,
                 callback: Callable[[str], None] = lambda someString: None,
                 position: tuple[int, int] = (0, 0), 
                 width: int = 100, 
                 fontSize:int = 10,
                 fontColor: tuple[int, int, int] = (255, 255, 255),
                 backColor: tuple[int, int, int] = None,
                 margin: int = 10,
                 active: bool = False) -> None:
        super().__init__()
        self.color = fontColor
        self.backcolor = backColor
        self.position = position
        self.width = width
        self.margin = margin
        self.font = pygame.font.SysFont(None, fontSize)
        self.active = active
        self.text = ""
        self.callback = callback
        self.locked = False
        self.render_text()
    
    def render_text(self):
        # create the text surface
        textSurface = self.font.render(
            self.text,
            True,
            self.color,
            self.backcolor
        )
        # create the image
        self.image = pygame.Surface(
            (max(self.width, textSurface.get_width() + self.margin), textSurface.get_height() + self.margin),
            pygame.SRCALPHA
        )
        # Add the background color to the image
        if (self.backcolor):
            self.image.fill(self.backcolor)
        # print the text onto the image
        self.image.blit(textSurface, (self.margin//2, self.margin//2))
        # draw a border to the image
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.position)

    def update(self, event_list):
        if self.locked:
            self.active = False
        for event in event_list:
            # Manage the focus of the textinput
            if not self.locked and event.type == pygame.MOUSEBUTTONDOWN:
                self.active = self.rect.collidepoint(event.pos)
            # manage keypresses
            if event.type == pygame.KEYDOWN and self.active:
                #submit text and reset it
                if event.key == pygame.K_RETURN:
                    self.callback(self.text)
                    self.text = ""
                # remove a letter on backspace
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                # register the character
                else:
                    self.text += event.unicode
                self.render_text()
    
    def reset(self):
        self.text = ""
        self.active = True,
        self.locked = False
        self.render_text()