import sys
import os
import random

import pygame

pygame.init()
size = width, height = 1900, 1100
screen = pygame.display.set_mode(size)


def text(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


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
        self.rect = self.rect.move(0, 0)
        self.rect.x = random.randint(0, 9) * 180 + 20
        self.rect.y
        self.kill()


class Zombi(pygame.sprite.Sprite):
    def __init__(self, image, health):
        super().__init__(zombis)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos = 1730
        self.health = health
        self.rect.y = self.y_pos = random.randint(0, 4) * 180 + 130
        self.clock = pygame.time.Clock()
        self.center = [1730, self.rect.y]

    def update1(self):
        self.x_pos += -0.9
        self.rect.center = (self.x_pos, self.y_pos + 90)
        if self.rect.x <= 20:
            self.kill()

    def update(self):
        if pygame.sprite.spritecollideany(self, bullets):
            self.health -= 25
            print(self.health)
            if self.health <= 0:
                self.kill()
        if pygame.sprite.spritecollideany(self, peases) or pygame.sprite.spritecollideany(self, sunflowers) \
                or pygame.sprite.spritecollideany(self, nuts):
            pass
        else:
            self.update1()


class Zombi1(Zombi):
    def __init__(self):
        super().__init__(load_image("zombi_1.png"), 50)


class Zombi2(Zombi):
    def __init__(self):
        super().__init__(load_image("zombi_2.png"), 100)


class Zombi3(Zombi):
    def __init__(self):
        super().__init__(load_image("zombi_3.png"), 150)


class Plant(pygame.sprite.Sprite):
    def __init__(self, group, image, x, y, health):
        super().__init__(group)
        self.health = health
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clock = pygame.time.Clock()
        self.ti = 0

    def update(self):
        self.rect = self.rect.move(0, 0)
        if pygame.sprite.spritecollideany(self, zombis):
            self.ti += clock.tick()
            if self.ti >= 300:
                self.health -= 50
                self.ti = 0
            if self.health <= 0:
                self.kill()


class Peas(Plant):
    def __init__(self, x, y):
        super().__init__(peases, load_image("re.png"), x, y, 200)


class Sunflower(Plant):
    def __init__(self, x, y):
        super().__init__(sunflowers, load_image("sn.png"), x, y, 200)


class Nut(Plant):
    def __init__(self, x, y):
        super().__init__(nuts, load_image("cu.png"), x, y, 1000)


class Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(button)
        self.image = load_image("clan.png", colorkey="white")
        self.rect = self.image.get_rect()
        self.rect.x = 1800
        self.rect.y = 10

    def update(self):
        self.rect = self.rect.move(0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(player)
        self.image = load_image("player.png", colorkey="white")
        self.rect = self.image.get_rect()
        print(1)
        self.rect.x = 380
        self.rect.y = 130

    def update(self, a):
        if pygame.sprite.spritecollideany(self, walls):
            print(2)
            self.kill()
        if a != 3:
            if a == 1:
                self.rect = self.rect.move(0, 180)
            elif a == 2:
                self.rect = self.rect.move(0, -180)


class Wall(pygame.sprite.Sprite):
    imo = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(walls)
        self.image = load_image("wall.png", colorkey="white")
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = random.randint(0, 2) * 180 + 130

    def update(self):
        self.rect.x -= 1.5
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(bullets)
        self.image = load_image("bullet.png", colorkey="white")
        self.rect = self.image.get_rect()
        self.rect.x = y
        self.rect.y = x
        self.speedy = 10
        self.clock = pygame.time.Clock()
        self.ti = 0

    def update(self):
        self.rect.x += self.speedy
        if self.rect.x >= 1730 or pygame.sprite.spritecollideany(self, zombis):
            self.ti += clock.tick()
            if self.ti >= 100:
                self.kill()
                self.ti = 0


if __name__ == '__main__':
    image = load_image("grass.png")
    image2 = load_image("grass2.png")
    zombis = pygame.sprite.Group()
    sunflowers = pygame.sprite.Group()
    peases = pygame.sprite.Group()
    nuts = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    button = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    player = pygame.sprite.Group()
    suns = pygame.sprite.Group()
    typ = 0
    money = 0
    board = Board(10, 5)
    board1 = Board(10, 3)
    d = 0
    running = True
    ti3 = 0
    ti2 = 0
    clock2 = pygame.time.Clock()
    ti = 0
    ti4 = 0
    i = 0
    clock = pygame.time.Clock()
    clock4 = pygame.time.Clock()
    clock3 = pygame.time.Clock()
    while running:
        if i == 0:
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
                        x, y = event.pos
                        if typ == 1 and money >= 100:
                            x_p = (board.get_cell(event.pos)[0]) * 180 + 20
                            y_p = (board.get_cell(event.pos)[1]) * 180 + 130
                            Peas(x=x_p, y=y_p)
                            money -= 100
                            typ = 0
                        elif typ == 2 and money >= 50:
                            x_p = (board.get_cell(event.pos)[0]) * 180 + 20
                            y_p = (board.get_cell(event.pos)[1]) * 180 + 130
                            Sunflower(x=x_p, y=y_p)
                            money -= 50
                            typ = 0
                        elif typ == 3 and money >= 50:
                            x_p = (board.get_cell(event.pos)[0]) * 180 + 20
                            y_p = (board.get_cell(event.pos)[1]) * 180 + 130
                            Nut(x=x_p, y=y_p)
                            money -= 50
                            typ = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for sun in suns:
                        if sun.rect.collidepoint(event.pos):
                            sun.update()
                            money += 25
                    for but in button:
                        if but.rect.collidepoint(event.pos):
                            running = False
            ti += clock.tick()
            ti2 += clock2.tick()
            ti3 += clock3.tick()
            ti4 += clock4.tick()
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
            Button()
            if len(peases) > 0:
                if ti3 >= 8000:
                    for peas in peases:
                        y_pe, x_pe, d, c = peas.rect
                        Bullet(x=x_pe, y=y_pe)
                        ti3 = 0
            if len(sunflowers) > 0:
                if ti4 >= 5000:
                    for sunflower in sunflowers:
                        money += 25
                        ti4 = 0
            if len(zombis) > 0:
                for zombi in zombis:
                    x_pe, y_pe, d, c = zombi.rect
                    if x_pe == 25:
                        i = 1
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
            screen.fill((0, 0, 0))
            text(str(f'{money}'), (225, 225, 225), (0, 0, 0), 300, 50, 20)
            x = 0
            y = 0
            for op in range(5):
                if y % 2 == 0:
                    x = 0
                    y += 1
                else:
                    x = 1
                    y += 1
                for t in range(10):
                    if x % 2 == 0:
                        x += 1
                        screen.blit(image, (20 + 180 * t, 130 + 180 * op))
                    else:
                        x += 1
                        screen.blit(image2, (20 + 180 * t, 130 + 180 * op))
            if typ == 1:
                pygame.draw.rect(screen, (0, 0, 225), (5, 5, 83, 120), width=0)
            elif typ == 2:
                pygame.draw.rect(screen, (0, 0, 225), (5 + 86, 5, 83, 120), width=0)
            elif typ == 3:
                pygame.draw.rect(screen, (0, 0, 225), (5 + 172, 5, 83, 120), width=0)
            board.render(screen)
            suns.draw(screen)
            zombis.draw(screen)
            bullets.draw(screen)
            button.draw(screen)
            all_sprites.draw(screen)
            peases.draw(screen)
            sunflowers.draw(screen)
            nuts.draw(screen)
            peases.update()
            sunflowers.update()
            button.update()
            nuts.update()
            zombis.update()
            bullets.update()
            pygame.display.flip()
        else:
            break
    screen.fill((0, 0, 0))
    running = True
    Player()
    m = 1
    clock5 = pygame.time.Clock()
    ti5 = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and m < 3 :
                    player.update(a=1)
                    m += 1
                elif event.key == pygame.K_w and m > 1:
                    player.update(a=2)
                    m -= 1
        ti5 += clock.tick()
        if len(player) == 0:
            break
        if ti5 > 3000:
            Wall()
            ti5 = 0
        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(a=3)
        walls.draw(screen)
        walls.update()
        board1.render(screen)
        pygame.display.flip()
    pygame.quit()
