import pygame
import random

class TreatObj:
    def __init__(self):
        self.pos_x = random.randint(0, 400)
        self.pos_y =  random.randint(0, 400)
        self.treatimg = None
        self.treatrect = None

        # self.set_graph()

    def set_graph(self):
        treats_img = pygame.image.load('treats.jpg')
        treats_img = pygame.transform.scale(treats_img, (30, 30))
        treats_img.convert()
        treats_rect = treats_img.get_rect()

        self.treatimg = treats_img
        self.treatrect = treats_rect

    def rand_move(self):
        self.pos_x = random.randint(0, 400)
        self.pos_y = random.randint(0, 400)

    def spawn(self):
        self.treatrect.center = self.pos_x, self.pos_y



