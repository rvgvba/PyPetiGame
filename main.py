import pygame
import random
from treats_obj import TreatObj
from player_obj import PlayerObj

pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

game_running = True
peti_img = pygame.image.load('cat.png')
peti_img_H, peti_img_W = 60, 60
peti_img = pygame.transform.scale(peti_img, (peti_img_H, peti_img_W))
peti_img.convert()
peti_rect = peti_img.get_rect()

rand_x = random.randint(0, 400)
rand_y = random.randint(0, 400)

RED = (255, 0, 0)

pos_x = 250
pos_y = 470

velocity = 10
cat_box_offset = 20
pygame.draw.rect(screen, (52, 106, 107), peti_rect, 1)

trit = TreatObj()
vplayer = PlayerObj()
font = pygame.font.SysFont('comicsans', 25, 1)


def show_score():
    score = font.render(f'Score: {vplayer.points-1}', 1, (255, 255, 255))
    screen.blit(score, (7, 7))


def catuna(x, y):
    peti_rect.center = x, y
    screen.blit(peti_img, peti_rect)


while game_running:
    screen.fill((52, 106, 107))
    catuna(pos_x, pos_y)
    trit.spawn()

    show_score()

    for event in pygame.event.get():
        if event == pygame.QUIT:
            game_running = False

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_UP]:
        if pos_y-cat_box_offset > velocity:
            pos_y -= velocity

    if key_pressed[pygame.K_DOWN]:
        if pos_y-cat_box_offset*2 < (500 - peti_img_H - velocity):
            pos_y += velocity

    if key_pressed[pygame.K_LEFT]:
        if pos_x-cat_box_offset > velocity:
            pos_x -= 10

    if key_pressed[pygame.K_RIGHT]:
        if pos_x-cat_box_offset*2 < (500 - peti_img_H - velocity):
            pos_x += 10

    if peti_rect.colliderect(trit):
        trit.rand_move()
        vplayer.add_point()
        show_score()

    # print(pos_x, pos_y)

    screen.blit(trit.img, trit.rect)
    pygame.draw.rect(screen, (52, 106, 107), trit.rect, 1)

    pygame.display.update()
    clock.tick(60)


pygame.quit()