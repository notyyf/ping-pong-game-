from pygame import *
# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((700, 500))
background = transform.scale(image.load("fon.jpg"), (win_width, win_height))
 

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
 
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
 
speed_x = 3 
speed_y = 3
 
racket1 = Player("racket.png", 5, 100, 30, 100, 5)
racket2 = Player("racket.png", 665, 100, 30, 100, 5)
ball = Player("ball.png", 200, 200, 30, 30, 0)


clock = time.Clock()
fps = 50

font.init()
font1 = font.Font(None,35)
lose1 = font1.render('PLAYER 1 LOSE!', True,(180,0,0))
lose2 = font1.render('PLAYER 2 LOSE!', True,(255,0,0))


# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
# Основной цикл игры:
game = True # флаг сбрасывается кнопкой закрытия окна
while game:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 470 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1

    if ball.rect.x < 0: 
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x > 700: 
            finish = True
            window.blit(lose2, (200, 200))
    

    window.blit(background, (0,0))
    racket1.reset()
    racket1.update_l()
    racket2.reset()
    racket2.update_r()
    ball.reset()
    # событие нажатия на кнопку Закрыть
    
 
 
    display.update()
    # цикл срабатывает каждую 0.05 секунд
    clock.tick(fps)



