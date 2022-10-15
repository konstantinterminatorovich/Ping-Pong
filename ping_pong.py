from pygame import *
import time as t
from random import randint
window = display.set_mode((1000, 700))
display.set_caption('Ping Pong')
clock = time.Clock()
galaxy = transform.scale(image.load('galaxy.jpg'),(1000, 700))

mixer.init()
kick_sound = mixer.Sound('kick.ogg')
font.init()
font1= font.SysFont('Arial', 36, bold=1)

class GameSprite(sprite.Sprite):
    def __init__(self, img, width, height, player_x, player_y, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self): #вывести на экран
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move_platform_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < (600 - self.speed):
            self.rect.y += self.speed
    def move_platform_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < (600 - self.speed):
            self.rect.y += self.speed
        


platform_right = GameSprite("ufo_right.png", 50, 100, 940, 300, 10)
platform_left = GameSprite("ufo_left.png", 50, 100, 10, 570, 10)
ball = GameSprite("meteorite2.png", 40, 40, 250, 10, 5)
win =  transform.scale(image.load('winwin.jpg'),(1000, 700))
lose = transform.scale(image.load('youlose.jpg'),(1000, 700))

right_goals=0
left_goals=0
speed_x=4
speed_y=4
wait=360


run=True
finish=False
right_win=True

while run:
    window.blit(galaxy, (0,0))
    if wait>=0:
        text_rules=font1.render('Пинг понг', 1, (0, 0, 255))
        window.blit(text_rules, (20, 0))
        text_rules2=font1.render('Игра до 3 голов' ,1, (255, 0, 0))
        window.blit(text_rules2, (20, 30))
        text_rules3=font1.render('Управление правым игром: стрелки вверх, вниз' ,1, (255, 255, 255))
        window.blit(text_rules3, (20, 60))
        text_rules4=font1.render('Управление левым игром: кнопки W - вверх, S - вниз', 1, (255, 255, 255))
        window.blit(text_rules4, (20, 90))
        wait-=1
    else:
        text_score = font1.render(str(left_goals)+' : '+str(right_goals), 1, (255, 255, 255))
        window.blit(text_score, (470, 30))
    for e in event.get():
        if e.type == QUIT:
            run = False
    if wait<0:
        if not finish:
            ball.rect.x+=speed_x
            ball.rect.y+=speed_y
            if ball.rect.y <=0 or ball.rect.y>=660:
                kick_sound.play()
                speed_y *=-1

            if sprite.collide_rect(platform_right, ball) or sprite.collide_rect(platform_left, ball):
                kick_sound.play()
                speed_x *=-1
            platform_left.reset()
            platform_right.reset()
            ball.reset()
            platform_left.move_platform_left()
            platform_right.move_platform_right()
            if ball.rect.x<=0:
                right_goals+=1
                ball.rect.x=250
                ball.rect.y=10
            if ball.rect.x>=1000:
                left_goals+=1
                ball.rect.x=250
                ball.rect.y=10
            if right_goals>=3:
                finish=True
            if left_goals>=3:
                finish=True

        
        else:
            if right_win:
                window.blit(win,(0,0))
                text_right_win=font1.render('Right', 1, (255, 0, 0))
                window.blit(text_right_win, (490, 0))
            else:
                window.blit(win,(0,0))
                text_left_win=font1.render('Left', 1, (255, 0, 0))
                window.blit(text_left_win, (490, 0))
    display.update()
    clock.tick(60)