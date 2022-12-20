import sys
import os
import random

import pygame

pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.left = 20
        self.top = 130
        self.cell_size = 180
        self.image = load_image("grass.png")

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell):
        pass

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def render(self, scree):
        for gg in range(self.height):
            for g in range(self.width):
                pygame.draw.rect(scree, pygame.Color(225, 225, 225), (
                    g * 180 + self.left, gg * 180 + self.top, 180,
                    180), 3)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением "{fullname}" не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Zombi1(pygame.sprite.Sprite):
    com = load_image("zombi_1.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Zombi1.com
        self.rect = self.image.get_rect()
        self.rect.x = 1730
        self.rect.y = random.randint(5) * 180 + 130


class Zombi2(pygame.sprite.Sprite):
    rar = load_image("zombi_2.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Zombi1.rar
        self.rect = self.image.get_rect()
        self.rect.x = 1730
        self.rect.y = random.randint(5) * 180 + 130


class Zombi3(pygame.sprite.Sprite):
    hard = load_image("zombi_3.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Zombi1.hard
        self.rect = self.image.get_rect()
        self.rect.x = 1730
        self.rect.y = random.randint(5) * 180 + 130


class Plant(pygame.sprite.Sprite):
    re = load_image("re.png")
    sn = load_image("sn.png")
    cu = load_image("cu.png")

    def __init__(self, *group, num, x, y):
        super().__init__(*group)
        self.num = num
        self.x = x
        self.y = y
        if num == 1:
            self.image = Plant.re
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            print(1)
        elif num == 2:
            self.image = Plant.sn
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            print(2)
        elif num == 3:
            self.image = Plant.cu
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            print(3)


if __name__ == '__main__':
    image = load_image("grass.png")
    image2 = load_image("grass2.png")
    zombis = pygame.sprite.Group()
    plants = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    plant = pygame.sprite.Sprite()
    plant.image = load_image("green.png")
    plant.rect = plant.image.get_rect()
    plant.rect.x = 10
    plant.rect.y = 10
    all_sprites.add(plant)
    sunflower = pygame.sprite.Sprite()
    sunflower.image = load_image("sunflow.png")
    sunflower.rect = plant.image.get_rect()
    sunflower.rect.x = 100
    sunflower.rect.y = 10
    all_sprites.add(sunflower)
    nut = pygame.sprite.Sprite()
    nut.image = load_image("nut.png")
    nut.rect = plant.image.get_rect()
    nut.rect.x = 190
    nut.rect.y = 10
    all_sprites.add(nut)
    typ = 0
    x = 0
    y = 0
    board = Board(10, 5)
    running = True
    for i in range(5):
        if y % 2 == 0:
            x = 0
            y += 1
        else:
            x = 1
            y += 1
        for t in range(10):
            if x % 2 == 0:
                x += 1
                screen.blit(image, (20 + 180 * t, 130 + 180 * i))
            else:
                x += 1
                screen.blit(image2, (20 + 180 * t, 130 + 180 * i))
    all_sprites.draw(screen)
    pygame.display.flip()
    board.render(screen)
    ti = 0
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    typ = 1
                elif event.key == pygame.K_2:
                    typ = 2
                elif event.key == pygame.K_3:
                    typ = 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_p = (board.get_cell(event.pos)[0]) * 180 + 20
                y_p = (board.get_cell(event.pos)[1]) * 180 + 130
                print(x_p, y_p)
                Plant(plants, num=typ, x=x_p, y=y_p)
            ti += clock.tick()
            if ti >= 15000:
                d = random.randint(3)
                if d == 0:
                    Zombi1(zombis)
                elif d == 1:
                    Zombi2(zombis)
                elif d == 2:
                    Zombi3(zombis)
            zombis.draw(screen)
            plants.draw(screen)
        board.render(screen)
        pygame.display.flip()
    pygame.quit()       
