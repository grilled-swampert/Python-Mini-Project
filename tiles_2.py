import pygame
from support_2 import import_folder
class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, shift):
        self.rect.x += shift

class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

class Animated(Tile):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, shift):
            self.animate()
            self.rect.x += shift

class Coins(Animated):
    def __init__(self, size, x, y, path):
        super().__init__(size, x, y, path)
        cen_x = x + int(size/2)
        cen_y = y + int(size/2)
        self.rect = self.image.get_rect(center = (cen_x, cen_y))

class Palm(Animated):
    def __init__(self, size, x, y, path, offset):
        super().__init__(size, x, y, path)
        off_y = y - offset
        self.rect.topleft = (x, off_y)