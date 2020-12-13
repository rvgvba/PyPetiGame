import pygame
import time

from petun_obj import PetunaObj
from treats_obj import TreatObj
from player_obj import PlayerObj


class PetunaGame:
    def __init__(self):
        self.game = pygame
        self.game_running = 1

        self.wndw_h = 500
        self.wndw_w = 500
        self.clock = self.game.time.Clock()
        self.screen = self.game.display.set_mode([self.wndw_h, self.wndw_w])

        self.cat = PetunaObj()
        self.treat = TreatObj()
        self.player = PlayerObj()

        self.timer = 37

        self.velocity = 10
        self.score_value = 0

        self.game.init()

    def draw_info(self, text_line=None, x=None, y=None):
        font = self.game.font.SysFont('comicsans', 25, 1)
        if text_line is None and x is None and y is None:
            render = font.render(f'Score: {self.score_value}', True, (255, 255, 255))
            self.screen.blit(render, (7, 7))
        else:
            render = font.render(text_line, True, (255, 255, 255))
            self.screen.blit(render, (x, y))

    def drawing(self):
        self.draw_info()
        self.draw_info(f'Player: {self.player.player_name}', 390, 10)

    def run_timmer(self):
        if self.timer > 0:
            self.timer -= 0.01
        else:
            return 0

    def game_over_screen(self):
        self.screen.fill((0, 0, 0))


    def run_game(self):

        self.cat.set_graph()
        self.treat.set_graph()

        starting_time = self.clock.tick()

        while self.game_running:
            self.screen.fill((52, 106, 107))
            self.screen.blit(self.cat.catimg, self.cat.catrect)
            self.screen.blit(self.treat.treatimg, self.treat.treatrect)
            self.drawing()

            self.draw_info(f'Time: {str(int(self.timer))}', 390, 30)

            self.cat.spawn()
            self.treat.spawn()

            for event in pygame.event.get():
                if event == pygame.QUIT:
                    self.game_running = False


            key_pressed = pygame.key.get_pressed()

            if key_pressed[pygame.K_ESCAPE]:
                self.player.reset_points()

            if key_pressed[pygame.K_UP]:
                if self.cat.pos_y - self.cat.catbox_offset > self.velocity:
                    self.cat.pos_y -= self.velocity

            if key_pressed[pygame.K_DOWN]:
                if self.cat.pos_y - self.cat.catbox_offset * 2 < (500 - self.cat.cat_H - self.velocity):
                    self.cat.pos_y += self.velocity

            if key_pressed[pygame.K_LEFT]:
                if self.cat.pos_x - self.cat.catbox_offset > self.velocity:
                    self.cat.pos_x -= 10

            if key_pressed[pygame.K_RIGHT]:
                if self.cat.pos_x - self.cat.catbox_offset * 2 < (500 - self.cat.cat_H - self.velocity):
                    self.cat.pos_x += 10

            if self.cat.catrect.colliderect(self.treat.treatrect):
                self.treat.rand_move()
                self.player.add_point()
                self.score_value = self.player.points

            # print(self.cat.pos_x, self.cat.pos_y)
            tmr = self.run_timmer()


            if tmr == 0:
                self.draw_info(f'Final Score: {self.player.points}', 190, 170)

            self.game.display.update()
            self.clock.tick(60)

        self.game.quit()
