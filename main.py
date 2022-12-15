import sys
import os
import random

import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.boar = []
        for i in range(self.height):
            self.ds = []
            for h in range(self.width):
                if h < 10:
                    self.ds.append("3")
                else:
                    self.ds.append(str(random.randint(0, 2)))
            self.boar.append(self.ds)
        self.left = 20
        self.top = 130
        self.cell_size = 18
        self.ty = 0
        self.car1 = 1
        self.car2 = 1
        self.car3 = 1
        self.car4 = 1
        self.car5 = 1
        for jo in range(5):
            for ko in range(5):
                self.boar[3 + jo * 10][3 + self.ty] = "gy"
                self.boar[4 + jo * 10][3 + self.ty] = "gy"
                self.boar[5 + jo * 10][3 + self.ty] = "gy"
                self.boar[6 + jo * 10][3 + self.ty] = "gy"
                self.ty += 1
            self.ty = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, scree):
        self.color = [(68, 148, 74), (168, 228, 160), (30, 89, 69)]
        for y in range(self.height):
            for x in range(self.width):
                if self.boar[y][x] == "gy":
                    pygame.draw.rect(scree, pygame.Color(225, 225, 0), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 0)
                elif self.boar[y][x] == "3":
                    pygame.draw.rect(scree, pygame.Color(32, 178, 170), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 0)
                    pygame.draw.rect(scree, pygame.Color(225, 225, 225), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 1)
                    for gg in range(self.height // 10):
                        for g in range(self.width // 10):
                            pygame.draw.rect(scree, pygame.Color(225, 225, 225), (
                                g * 180 + self.left, gg * 180 + self.top, 180,
                                180), 3)
                elif self.boar[y][x] == "z_st":
                    pygame.draw.rect(scree, pygame.Color(225, 0, 0), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 0)
                else:
                    if self.boar[y][x] == "0":
                        pygame.draw.rect(scree, pygame.Color(self.color[0]), (
                            x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                            self.cell_size), 0)
                    elif self.boar[y][x] == "1":
                        pygame.draw.rect(scree, pygame.Color(self.color[1]), (
                            x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                            self.cell_size), 0)
                    elif self.boar[y][x] == "2":
                        pygame.draw.rect(scree, pygame.Color(self.color[2]), (
                            x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                            self.cell_size), 0)
                    pygame.draw.rect(scree, pygame.Color(225, 225, 225), (
                        x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                        self.cell_size), 1)

    def on_click(self, cell):
        pass

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def car1_move(self):
        for oi in range(len(self.boar[0:9])):
            for om in range(len(self.boar[0 + oi])):
                if self.boar[oi][om] == "gy":
                    if om != 98:
                        self.boar[oi][om + 1] = "gy"
                        self.boar[oi][om] = str(random.randint(0, 2))
                    else:
                        self.boar[oi][om + 1] = str(random.randint(0, 2))
                        self.boar[oi][om] = str(random.randint(0, 2))

    def car2_move(self):
        for oi in range(len(self.boar[9:19])):
            for om in range(len(self.boar[9 + oi])):
                if self.boar[oi + 9][om] == "gy":
                    if om != 98:
                        self.boar[oi + 9][om + 1] = "gy"
                        self.boar[oi + 9][om] = str(random.randint(0, 2))
                    else:
                        self.boar[oi + 9][om + 1] = str(random.randint(0, 2))
                        self.boar[oi + 9][om] = str(random.randint(0, 2))

    def car3_move(self):
        for oi in range(len(self.boar[19:29])):
            for om in range(len(self.boar[19 + oi])):
                if self.boar[oi + 19][om] == "gy":
                    if om != 98:
                        self.boar[oi + 19][om + 1] = "gy"
                        self.boar[oi + 19][om] = str(random.randint(0, 2))
                    else:
                        self.boar[oi + 19][om + 1] = str(random.randint(0, 2))
                        self.boar[oi + 19][om] = str(random.randint(0, 2))

    def car4_move(self):
        for oi in range(len(self.boar[29:39])):
            for om in range(len(self.boar[29 + oi])):
                if self.boar[oi + 29][om] == "gy":
                    if om != 98:
                        self.boar[oi + 29][om + 1] = "gy"
                        self.boar[oi + 29][om] = str(random.randint(0, 2))
                    else:
                        self.boar[oi + 29][om + 1] = str(random.randint(0, 2))
                        self.boar[oi + 29][om] = str(random.randint(0, 2))

    def car5_move(self):
        for oi in range(len(self.boar[39:49])):
            for om in range(len(self.boar[39 + oi])):
                if self.boar[oi + 39][om] == "gy":
                    if om != 98:
                        self.boar[oi + 39][om + 1] = "gy"
                        self.boar[oi + 39][om] = str(random.randint(0, 2))
                    else:
                        self.boar[oi + 39][om + 1] = str(random.randint(0, 2))
                        self.boar[oi + 39][om] = str(random.randint(0, 2))

    def zombi_move(self, pose_y, pose_x):
        if 9 < pose_y <= 19 and pose_x == 9:
            if self.car2 == 1:
                self.car2 = 0
                self.car2_move()
        if pose_y <= 9 and pose_x == 9:
            if self.car1 == 1:
                self.car1 = 0
                self.car1_move()
        if 19 < pose_y <= 29 and pose_x == 9:
            if self.car3 == 1:
                self.car3 = 0
                self.car3_move()
        if 29 < pose_y <= 39 and pose_x == 9:
            if self.car4 == 1:
                self.car4 = 0
                self.car4_move()
        if 39 < pose_y <= 49 and pose_x == 9:
            if self.car5 == 1:
                self.car5 = 0
                self.car5_move()

        if pose_x != 1 and self.boar[pose_y][pose_x - 1] != "gy":
            self.boar[pose_y][pose_x - 1] = "z_st"
            if pose_x * 18 <= 162 and self.boar[pose_y][pose_x - 1] != "gy":
                self.boar[pose_y][pose_x] = "3"
            elif self.boar[pose_y][pose_x - 1] != "gy":
                self.boar[pose_y][pose_x] = str(random.randint(0, 2))
        else:
            self.boar[pose_y][pose_x - 1] = "3"
            self.boar[pose_y][pose_x] = "3"

    def zombi_spawn(self):
        if random.randint(1, 5) == 1:
            self.boar[4][99] = "z_st"
            self.boar[3][99] = "z_st"
            self.boar[5][99] = "z_st"
            self.boar[6][99] = "z_st"
        elif random.randint(1, 5) == 2:
            self.boar[14][99] = "z_st"
            self.boar[13][99] = "z_st"
            self.boar[15][99] = "z_st"
            self.boar[16][99] = "z_st"
        elif random.randint(1, 5) == 3:
            self.boar[24][99] = "z_st"
            self.boar[23][99] = "z_st"
            self.boar[25][99] = "z_st"
            self.boar[26][99] = "z_st"
        elif random.randint(1, 5) == 4:
            self.boar[34][99] = "z_st"
            self.boar[33][99] = "z_st"
            self.boar[35][99] = "z_st"
            self.boar[36][99] = "z_st"
        elif random.randint(1, 5) == 5:
            self.boar[44][99] = "z_st"
            self.boar[43][99] = "z_st"
            self.boar[45][99] = "z_st"
            self.boar[46][99] = "z_st"


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    pygame.init()
    time = 0
    time2 = 0

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

    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    board = Board(100, 50)
    running = True
    clock = pygame.time.Clock()
    clock2 = pygame.time.Clock()
    all_sprites.draw(screen)
    pygame.display.flip()
    board.render(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        time += clock.tick()
        time2 += clock2.tick()
        if time >= 15000:
            board.zombi_spawn()
            time = 0
        if time2 >= 200:
            for mo in range(len(board.boar)):
                for io in range(len(board.boar[mo])):
                    if board.boar[mo][io] == "z_st":
                        board.zombi_move(mo, io)
                        time2 = 0

        board.render(screen)
        pygame.display.flip()
    pygame.quit()
