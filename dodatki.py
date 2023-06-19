import pygame

def muzyka():
    pygame.init()
    pygame.mixer.music.load("muzyka.mp3")
    pygame.mixer.music.play(-1, 0.0)

