import pygame

def draw_stickman(screen: pygame.Surface, score: int, position: tuple[int, int], color: tuple[int, int, int] = (0,0,0), thiccness: int = 2):
    # draw a partially transparent backdrop for the stickman
    backdrop = pygame.Surface((245, 320))
    backdrop.set_alpha(200)
    backdrop.fill((255,255,255))
    screen.blit(
        backdrop,
        (position[0] - 175, position[1] - 155)
    )
    
    # drawing the pole
    if score == 0:
        return  False
    pygame.draw.line(
        screen,
        color,
        (position[0] - 80, position[1] +150 ),
        (position[0] - 160, position[1] +150 ),
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    pygame.draw.line(
        screen,
        color,
        (position[0] - 120, position[1] + 5),
        (position[0] - 120, position[1] + 150),
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    pygame.draw.line(
        screen,
        color,
        (position[0] - 120, position[1] - 140),
        (position[0] - 120, position[1] + 5),
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    pygame.draw.line(
        screen,
        color,
        (position[0] - 60, position[1] - 140),
        (position[0] - 120, position[1] -80 ),
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    pygame.draw.line(
        screen,
        color,
        (position[0], position[1] - 140),
        (position[0] - 120, position[1] - 140),
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    pygame.draw.line(
        screen,
        color,
        (position[0], position[1] - 115),
        (position[0], position[1] - 140),
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    # draw head
    pygame.draw.circle(
        screen,
        color,
        (position[0], position[1] - 75),
        40,
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    # draw body shape
    pygame.draw.line(
        screen,
        color,
        (position[0], position[1] + 50),
        (position[0], position[1] - 35),
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    # draw arms
    pygame.draw.line(
        screen,
        color,
        (position[0], position[1]),
        (position[0] + 40, position[1] + 10),
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    pygame.draw.line(
        screen,
        color,
        (position[0], position[1]),
        (position[0] - 40, position[1] + 10),
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    # draw leggs
    pygame.draw.line(
        screen,
        color,
        (position[0], position[1] + 50),
        (position[0] + 50, position[1] + 100),
        thiccness
    )
    score -= 1
    if score == 0:
        return False
    pygame.draw.line(
        screen,
        color,
        (position[0], position[1] + 50),
        (position[0] - 50, position[1] + 100),
        thiccness
    )
    return True