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

left_player = Player("red.jpg", 5, 180, 15 , 100, 6)
right_player = Player("blue.png", 680, 180, 15, 100, 6)
boll = GameSprite("boll.png", 300, 195, 85, 85, 6)

font.init()
font1 = font.Font(None, 35)
lont1 = font1.render('КРАСНЫЙ ПРОИГРАЛ!', True, (180, 0, 0))
lont2 = font1.render('СИНИЙ ПРОИГРАЛ!', True, (180, 0, 0))


speed_x = 5
speed_y = 5

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        boll.update()
        left_player.update2()
        right_player.update1()
        left_player.reset()
        right_player.reset()
        boll.reset()
        boll.rect.x += speed_x
        boll.rect.y += speed_y
    if boll.rect.y > win_height-50 or boll.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(right_player, boll) or sprite.collide_rect(left_player, boll):
        speed_x *= -1
    if boll.rect.x < -20:
        finish = True
        window.blit(lont1, (200, 200))
    if boll.rect.x > win_wigth:
        finish = True
        window.blit(lont2, (200, 200))
    display.update()
    clock.tick(FPS)