import pygame, sys


class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.player = pygame.Surface((100, 100))
        self.player.fill((0, 255, 0))
        pos = (100, 240)
        self.player_rect = self.player.get_rect(center = pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.player_rect.center)
        self.speed = 200

        self.main_loop()

    def move_player(self, dt):
        # to stop diagonal movement put these into seperate functions ig
        moving_to = (400, 240) #x, y
        if moving_to == self.pos:
            return
        if moving_to[0] > self.pos.x:
            self.direction.x = 1
        elif moving_to[1] < self.pos.x:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if moving_to[1] > self.pos.y:
            self.direction.y = 1
        elif moving_to[1] < self.pos.y:
            self.direction.y = -1
        else:
            self.direction.y = 0
        self.pos.x += self.direction.x * self.speed * dt
        self.player_rect.centerx = self.pos.x
        self.pos.y += self.direction.y * self.speed * dt
        self.player_rect.centery = self.pos.y
        print(f"rect_pos: {self.player_rect.x,}")
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.player, (int(self.pos.x), int(self.pos.y)))
        pygame.display.flip()

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = self.clock.tick() / 1000
            self.move_player(dt)
            self.draw()

if __name__ == '__main__':
    game = Game()