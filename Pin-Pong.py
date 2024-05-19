from pygame import *


win_wigth = 700
win_height = 500
window = display.set_mode((win_wigth, win_height))
display.set_caption("Pygame window")
background = transform.scale(image.load("fon.jpg"), (win_wigth, win_height))
FPS = 60
clock = time.Clock()
#mixer.init()
#mixer.music.load('')
#mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_wigth, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_wigth, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_wigth - 85:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_wigth - 85:
            self.rect.y += self.speed

left_player = Player("red.jpg", 5, 180, 15 , 100, 4)
right_player = Player("blue.png", 680, 180, 15, 100, 4)


#class Enemy(GameSprite): 



finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        left_player.update2()
        right_player.update1()
        left_player.reset()
        right_player.reset()
        display.update()
    clock.tick(FPS)