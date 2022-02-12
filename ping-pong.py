from pygame import *

win_widht = 700
win_height = 500
display.set_caption('Ping-pong')
window = display.set_mode((700,500))
background = transform.scale(image.load('fon.jpg'),(win_widht, win_height))

finish = False 

game = True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

        display.update()
    time.delay(50)





































