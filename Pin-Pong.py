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

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        display.update()
        clock.tick(FPS)