import pygame
from typing import Callable
class TextSprite(pygame.sprite.Sprite):
    def __init__(self,
                 text: str = '',
                 textFilter: Callable[[str], str] = lambda someString: someString,
                 position: tuple[int, int] = (0, 0), 
                 width: int = 100, 
                 fontSize:int = 10,
                 fontColor: tuple[int, int, int] = (255, 255, 255),
                 backColor: tuple[int, int, int] = None,
                 margin: int = 10) -> None:
        super().__init__()
        self.text = textFilter(text)
        self.textFilter = textFilter
        self.color = fontColor
        self.backcolor = backColor
        self.position = position
        self.width = width
        self.margin = margin
        self.font = pygame.font.SysFont(None, fontSize)
        self.render_text()

    def getWidth(self):
        return max(self.width, self.textSurface.get_width() + self.margin)
    def getHeight(self):
        return self.textSurface.get_height() + self.margin

    def setText(self, text: str):
        self.text = self.textFilter(text)
        self.render_text()

    def render_text(self):
        # create the text surface
        self.textSurface = self.font.render(
            self.text,
            True,
            self.color,
            self.backcolor
        )
        # create the image
        self.image = pygame.Surface(
            (self.getWidth(), self.getHeight()),
            pygame.SRCALPHA
        )
        # Add the background color to the image
        if (self.backcolor):
            self.image.fill(self.backcolor)
        # print the text onto the image
        self.image.blit(self.textSurface, (self.margin//2, self.margin//2))
        # draw a border to the image
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.position)
