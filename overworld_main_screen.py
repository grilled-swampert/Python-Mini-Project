import pygame
from level_info import levels


class Node(pygame.sprite.Sprite):
    def __init__(self, pos, status, speed):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill('white' if status == 'available' else 'red')
        self.rect = self.image.get_rect(center=pos)
        # self.detection_zone = pygame.Rect(left, top, width, height)
        self.detection_zone = pygame.Rect(self.rect.centerx - (speed/2), self.rect.centery - (speed/2), speed, speed)


class Icon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(). __init__()
        self.pos = pos
        self.image = pygame.Surface((20, 20))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.center = self.pos


class Overworld:
    def __init__(self, start_level, last_level, surface, create_level):
        # setup
        self.display_surface = surface
        self.last_level = last_level
        self.current_level = start_level
        self.create_level = create_level

        # movement logic
        self.moving = False
        self.move_direction = pygame.math.Vector2(0, 0)
        self.speed = 7

        # sprites
        self.setup_nodes()
        self.setup_icon()

    def setup_nodes(self):
        self.nodes = pygame.sprite.Group()

        for index, node_data in enumerate(levels.values()):
            node_status = 'available' if index <= self.last_level else 'locked'
            node_sprite = Node(node_data['node_pos'], node_status, self.speed)
            self.nodes.add(node_sprite)

    def path(self):
        # pygame.draw.lines(surface, color, fill, points, line_width)
        points = [node['node_pos'] for index, node in enumerate(levels.values())if index <= self.last_level]
        pygame.draw.lines(self.display_surface, 'white', False, points, 8)

    def setup_icon(self):
        self.icon = pygame.sprite.GroupSingle()
        icon_sprite = Icon(self.nodes.sprites()[self.current_level].rect.center)
        self.icon.add(icon_sprite)

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.moving:
            if keys[pygame.K_RIGHT] and self.current_level < self.last_level:
                self.move_direction = self.movement('next')
                self.current_level += 1
                self.moving = True
            elif keys[pygame.K_LEFT] and self.current_level > 0:
                self.move_direction = self.movement('previous')
                self.current_level -= 1
                self.moving = True
            elif keys[pygame.K_SPACE]:
                self.create_level(self.current_level)

    def movement(self, target):
        start = self.nodes.sprites()[self.current_level].rect.center
        end_index = self.current_level + 1 if target == 'next' else self.current_level - 1
        end = self.nodes.sprites()[end_index].rect.center
        return (pygame.math.Vector2(end) - pygame.math.Vector2(start)).normalize()

    def update_icon_pos(self):
        if self.moving and self.move_direction:
            self.icon.sprite.pos += self.move_direction * self.speed
            target_node = self.nodes.sprites()[self.current_level]
            if target_node.detection_zone.collidepoint(self.icon.sprite.pos):
                self.moving = False
                self.move_direction = pygame.math.Vector2(0, 0)

    def run(self):
        self.input()
        self.update_icon_pos()
        self.icon.update()
        self.path()
        self.nodes.draw(self.display_surface)
        self.icon.draw(self.display_surface)
