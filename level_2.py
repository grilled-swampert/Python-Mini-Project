import pygame
from support_2 import import_csv_layout, import_cut_graphics
from settings_2 import tile_size
from tiles import Tile, StaticTile, Animated, Coins, Palm

class Level:
    def __init__(self, level_data, surface):
        # general
        self.display_surface = surface
        self.world_shift = -3

        #player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)
        # terrain
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')
        print(terrain_layout)

        #coins
        coins_layout = import_csv_layout(level_data['coins'])
        self.coins_sprites = self.create_tile_group(coins_layout, 'coins')

        #fg palms
        fgpalm_layout = import_csv_layout(level_data['fgpalm'])
        self.fgpalm_sprites = self.create_tile_group(fgpalm_layout, 'fgpalm')

        #bg palms
        bgpalm_layout = import_csv_layout(level_data['bgpalm'])
        self.bgpalm_sprites = self.create_tile_group(bgpalm_layout, 'bgpalm')

        #enemies
        enemies_layout = import_csv_layout(level_data['enemies'])
        self.enemies_sprites = self.create_tile_group(bgpalm_layout, 'enemies')
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for column_index, val in enumerate(row):
                if val != '-1':
                    x = column_index * tile_size
                    y = row_index * tile_size

                    if type == "terrain":
                        terrain_tile_list = import_cut_graphics('../graphics/terrain/[64x64] Rocky Grass.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)
                    if type == "coins":
                        if val == '0':
                            sprite = Coins(tile_size, x, y,'../graphics/coins/gold')
                        if val == '1':
                            sprite = Coins(tile_size, x, y, '../graphics/coins/silver')
                        sprite_group.add(sprite)
                    if type == "fgpalm":
                        sprite = Palm(tile_size, x, y, '../graphics/palm_small', 38)
                        sprite_group.add(sprite)
                    if type == "bgpalm":
                        sprite = Palm(tile_size, x, y, '../graphics/palm_bg', 38)
                        sprite_group.add(sprite)
                    #if type == "enemies":
                    #    sprite = Enemies(tile_size, x, y)

        return sprite_group
    def player_setup(self, layout):
    for row_index, row in enumerate(layout):
        for column_index, val in enumerate(row):
            if val != '-1':
                x = column_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    print('player goes here')
                if val == '1':
                    hat_surface = pygame.image.load()
                    sprite = StaticTile(tile_size, x, y, hat_surface)
                    self.goal.add(add)

    def run(self):
       # bgpalm
       self.bgpalm_sprites.draw(self.display_surface)
       self.bgpalm_sprites.update(self.world_shift)
       # terrain
       self.terrain_sprites.draw(self.display_surface)
       self.terrain_sprites.update(self.world_shift)
       # coins
       self.coins_sprites.draw(self.display_surface)
       self.coins_sprites.update(self.world_shift)
       # fgpalm
       self.fgpalm_sprites.draw(self.display_surface)
       self.fgpalm_sprites.update(self.world_shift)