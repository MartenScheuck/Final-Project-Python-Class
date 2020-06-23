import os
import pygame as pg

# implement class that keeps check of colors and globals etc.

# Center the application
os.environ["SDL_VIDEO_CENTERED"] = "1"

# Set screen
FULLSCREEN = pg.display.set_mode((0, 0), pg.FULLSCREEN)
SCREEN = FULLSCREEN

# Get screen size
info = pg.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
MAX_RESOLUTION = (info.current_w, info.current_h)

# Set fps and clock
FPS, clock = 25, pg.time.Clock()

# Define colors
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)

# Font
font = "assets/Gameplay.ttf"

# Size of the circles/planets
BLOCK_SIZE = 25
CIRCLE_RADIUS = int(BLOCK_SIZE/2)

# max_number of objects and object_counter
max_object_number = 20
object_counter = 0
objects = []
radius = []

# make solarsystem objects accesible via options menu via singleton

# Temporarly sprite host, make functions into classes and use sprite functionality
