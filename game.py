import pygame
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

        self.velocity = 10
        self.score_value = 0

        self.game.init()

    def get_score(self):
        font = self.game.font.SysFont('comicsans', 25, 1)
        score_line = font.render(f'Score: {self.score_value}', True, (255, 255, 255))
        self.screen.blit(score_line, (7, 7))

    def run_game(self):

        self.cat.set_graph()
        self.treat.set_graph()

        while self.game_running:
            self.screen.fill((52, 106, 107))
            self.screen.blit(self.cat.catimg, self.cat.catrect)
            self.screen.blit(self.treat.treatimg, self.treat.treatrect)
            self.get_score()

            self.cat.spawn()
            self.treat.spawn()

            for event in pygame.event.get():
                if event == pygame.QUIT:
                    self.game_running = False

            key_pressed = pygame.key.get_pressed()
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



            self.game.display.update()
            self.clock.tick(60)

        self.game.quit()
