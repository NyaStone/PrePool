import pygame
from typing import Callable

class Button(pygame.sprite.Sprite):
    def __init__(self,
                 text: str = "",
                 callback: Callable[[], None] = lambda:None,
                 position: tuple[int, int] = (0, 0),
                 width: int = 100, 
                 fontSize:int = 10,
                 fontColor: tuple[int, int, int] = (255, 255, 255),
                 backColor: tuple[int, int, int] = None,
                 margin: int = 10) -> None:
        super().__init__()
        self.color = fontColor
        self.backcolor = backColor
        self.position = position
        self.width = width
        self.margin = margin
        self.font = pygame.font.SysFont(None, fontSize)
        self.text = text
        self.callback = callback
        self.render_button()

    def render_button(self):
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

    def update(self, eventList):
        for event in eventList:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.callback()
