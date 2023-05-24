import pygame
import sys
from display_settings import screen_width, screen_height
from overworld_main_screen import Overworld
from levels_setup import Level


class Game:
    def __init__(self):
        self.max_level = 1
        self.overworld_screen = Overworld(0, self.max_level, game_screen, self.load_level)
        self.status = 'overworld'

    def load_level(self, current_level):
        self.level_screen = Level(current_level, game_screen, self.load_overworld)
        self.status = 'level'

    def load_overworld(self, current_level, new_max_level):
        self.max_level = max(new_max_level, self.max_level)
        self.overworld_screen = Overworld(current_level, self.max_level, game_screen, self.load_level)
        self.status = 'overworld'

    def run(self):
        getattr(self, self.status + '_run')()

    def overworld_run(self):
        self.overworld_screen.run()

    def level_run(self):
        self.level_screen.run()


pygame.init()
game_screen = pygame.display.set_mode((screen_width, screen_height))
clock_frame_rate = pygame.time.Clock()
game_instance = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_screen.fill('black')
    game_instance.run()
    pygame.display.update()
    clock_frame_rate.tick(60)  # Limit the frame rate to 60 FPS

