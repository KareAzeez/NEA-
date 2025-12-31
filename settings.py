# settings.py
import pygame
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (253, 253, 150)
RED = (244, 194, 194)

# Screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800

# Asset files
BACKGROUND_IMG = "image.png"
MUSIC_FILE = "gamemusic.mp3"

# Maze area where questions are shown (for positioning the text, etc.)
QUESTION_AREA_Y = 650

# Option boxes positions and size
OPTION_BOXES = [
    pygame.Rect(100, 250, 25, 25),
    pygame.Rect(290, 500, 25, 25),
    pygame.Rect(501, 384, 25, 25),
    pygame.Rect(670, 170, 25, 25)
]

# Question feedback delay (in milliseconds)
QUESTION_DELAY = 2000