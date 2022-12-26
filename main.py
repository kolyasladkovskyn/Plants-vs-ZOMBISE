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

class Sun(pygame.sprite.Sprite):
    sun = load_image("sun.png", colorkey="white")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Sun.sun
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 9) * 180 + 20
        self.rect.y = random.randint(0, 4) * 180 + 130

    def update(self):
        print(1)

        self.kill()

class Zombi(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__(zombis)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 1730
        self.rect.y = random.randint(0, 4) * 180 + 130

    def update(self):
        self.rect = self.rect.move(-1, 0)
        if self.rect.x <= 20:
            self.kill()


class Zombi1(Zombi):
    def __init__(self):
        super().__init__(load_image("zombi_1.png"))
        self.health = 100

class Zombi2(Zombi):
    def __init__(self):
        super().__init__(load_image("zombi_2.png"))
        self.health = 150

class Zombi3(Zombi):
    def __init__(self):
        super().__init__(load_image("zombi_3.png"))
        self.health = 200

class Plant(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__(plants)
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Peas(Plant):
    def __init__(self, x, y):
        super().__init__(load_image("re.png"), x, y)

class Sunflower(Plant):
    def __init__(self, x, y):
        super().__init__(load_image("sn.png"), x, y)

class Nut(Plant):
    def __init__(self, x, y):
        super().__init__(load_image("cu.png"), x, y)

if __name__ == '__main__':
    image = load_image("grass.png")
    image2 = load_image("grass2.png")
    zombis = pygame.sprite.Group()
    plants = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    suns = pygame.sprite.Group()
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
    money = 0
    board = Board(10, 5)
    d = 0
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
    board.render(screen)
    ti2 = 0
    clock2 = pygame.time.Clock()
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
            if typ != 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if typ == 1 and money >= 100:
                        x_p = (board.get_cell(event.pos)[0]) * 180 + 20
                        y_p = (board.get_cell(event.pos)[1]) * 180 + 130
                        Peas(x=x_p, y=y_p)
                        money -= 100
                    elif typ == 2 and money >= 50:
                        x_p = (board.get_cell(event.pos)[0]) * 180 + 20
                        y_p = (board.get_cell(event.pos)[1]) * 180 + 130
                        Sunflower(x=x_p, y=y_p)
                        money -= 50
                    elif typ == 3 and money >= 50:
                        x_p = (board.get_cell(event.pos)[0]) * 180 + 20
                        y_p = (board.get_cell(event.pos)[1]) * 180 + 130
                        Nut(x=x_p, y=y_p)
                        money -= 50
            if event.type == pygame.MOUSEBUTTONDOWN:
                for sun in suns:
                    if sun.rect.collidepoint(event.pos):
                        print(1)
                        sun.update()
                        money += 25
                        print(money)
        ti += clock.tick()
        ti2 += clock2.tick()
        if ti >= 15000:
            d = random.randint(0, 2)
            if d == 0:
                Zombi1()
            elif d == 1:
                Zombi2()
            elif d == 2:
                Zombi3()
            ti = 0
        if ti2 >= 5000:
            Sun(suns)
            ti2 = 0
        suns.draw(screen)
        zombis.draw(screen)
        plants.draw(screen)
        zombis.update()
        pygame.display.flip()
    pygame.quit()       
