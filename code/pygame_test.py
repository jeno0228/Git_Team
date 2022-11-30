import pygame
import os
import random
import time
from datetime import datetime
#아이템, 이동방향(4), 목표물 4면
pygame.init()
size = [900,700]
screen = pygame.display.set_mode(size)

#게임창 옵션 설정
title = "My Game"
pygame.display.set_caption(title)

# 게임 내 필요한 설정
clock = pygame.time.Clock()

background_music = pygame.mixer.Sound('code/sci-fi_theme.mp3')
background_music.play(-1)

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.mv = 0
        self.mv_x = 0
        self.mv_y = 0
    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx,sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))
def crash(obj1, obj2):
    if obj1 != 0 and obj2 != 0:
        if obj1.x-obj2.sx <= obj2.x and obj2.x <= obj1.x+obj1.sx:
            if obj1.y-obj2.sy <= obj2.y and obj2.y <= obj1.y+obj1.sy:
                return True
    return False


shoot_sound = pygame.mixer.Sound('code/laserfire01.ogg')
explosion_sound_1 = pygame.mixer.Sound('code/explosion.wav')
explosion_sound_2 = pygame.mixer.Sound('code/DeathFlash.flac')


panda = obj()
panda.put_img("code/ss.png")
panda.change_size(50,50)
bullets = []
enemies = []
items = []
bullet_items = []
spawn = []
lives = [] # 목숨 리스트
for i in range(size[1]):
    spawn.append((0,i))
    spawn.append((size[0],i))
for i in range(size[0]):
    spawn.append((i,0))
    spawn.append((i,size[1]))



panda.x = (size[0]-panda.sx)//2
panda.y = (size[1]-panda.sy)//2
panda.mv = 5    #이속증가 템 추가

# 목숨 이미지, 화면 왼쪽 아래에 나오게 위치 설정
# for 문의 range의 인자는 목숨의 갯수를 의미함
for i in range(5):
    life = obj()
    life.put_img("code/ss.png")
    life.change_size(30, 30)
    life.x, life.y = 15 + i*(life.sx + life.sx/2), size[1] - life.sy - 10
    lives.append(life)


left_go = False
right_go = False
up_go = False
down_go = False
shooting = False
color = (0,0,0)
white = (255, 255, 255)
killed = 0
level = 0
bullet_size = 5
font = pygame.font.Font("code/bold_pw.ttf",20)

# start
SB = 0
ST = 0
while ST == 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ST = 1
            SB = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (mouse_x >= 400) & (mouse_x <= 500):
                if (mouse_y >= 400) & (mouse_y <= 500):
                    ST = 1
    text = font.render("Game Start", True, white)
    rect = text.get_rect()
    rect.center = (450, 450)
    screen.fill(color)
    screen.blit(text, rect)
    pygame.display.flip()

start_time = datetime.now()
delay = 0
# main
while SB == 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                left_go = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                right_go = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                up_go = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                down_go = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                left_go = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                right_go = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                up_go = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                down_go = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            shooting = True
            delay = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            shooting = False
            delay = 1

    if level >= 18:
        level = 18
    if panda.x > 0 and left_go:
        panda.x -= panda.mv
    if (panda.x+panda.sx)<size[0] and right_go:
        panda.x += panda.mv
    if panda.y > 0 and up_go:
        panda.y -= panda.mv
    if (panda.y+panda.sy)<size[1] and down_go:
        panda.y += panda.mv
    if shooting & (delay % (10-level//2) == 0):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            shoot_sound.play()
            bullet = obj()
            bullet.put_img("code/bullet.jpg")
            bullet.change_size(bullet_size, bullet_size)
            bullet.mv = 20
            bullet.mv_x = ((bullet.mv**2)*(mouse_x-panda.x-panda.sx//2)**2//((mouse_x-panda.x-panda.sx//2)**2+(mouse_y-panda.y-panda.sy//2)**2))**(1/2)
            bullet.mv_y = ((bullet.mv**2)*(mouse_y-panda.y-panda.sy//2)**2//((mouse_x-panda.x-panda.sx//2)**2+(mouse_y-panda.y-panda.sy//2)**2))**(1/2)
            if mouse_x < panda.x:
                bullet.mv_x = -bullet.mv_x
            if mouse_y < panda.y:
                bullet.mv_y = -bullet.mv_y
            bullet.x = panda.x+panda.sx//2
            bullet.y = panda.y+panda.sy//2
            bullets.append(bullet)
    delay +=1
            
    dm_bullets = []
    dm_enemies = []
    dm_items = []
    dm_bullet_items = []
    dm_lives = []

    for i in range(len(bullets)):
        bullet = bullets[i]
        bullet.x += bullet.mv_x
        bullet.y += bullet.mv_y
        if bullet.y <= -bullet.sy or bullet.x <= -bullet.sx or bullet.x > size[0] or bullet.y > size[1]:
            dm_bullets.append(i)
    
    if random.random() > (0.98-0.01*level):
        enemy = obj()
        enemy.put_img("code/aa.png")
        enemy.change_size(30,30)
        enemy.x, enemy.y = random.choice(spawn)
        enemy.mv = 4
        enemies.append(enemy)

    if (random.random() > 0.9999 and len(items) < 3):
        item = obj()
        item.put_img("code/item.png")
        item.change_size(15,15)
        item.x = random.randint(0,size[0]-15)
        item.y = random.randint(0,size[1]-15)
        items.append(item)
    if (random.random() > 0.9999 and len(bullet_items) < 3):
        item = obj()
        item.put_img("code/item_bullet.png")
        item.change_size(15,15)
        item.x = random.randint(0,size[0]-15)
        item.y = random.randint(0,size[1]-15)
        bullet_items.append(item)


    for i in range(len(enemies)):
        enemy = enemies[i]
        enemy.mv_x = ((enemy.mv**2)*(panda.x+panda.sx//2-enemy.x-enemy.sx//2)**2//((panda.x+panda.sx//2-enemy.x-enemy.sx//2)**2+(panda.y+panda.sy//2-enemy.y-enemy.sy//2)**2))**(1/2)
        enemy.mv_y = ((enemy.mv**2)*(panda.y+panda.sy//2-enemy.y-enemy.sy//2)**2//((panda.x+panda.sx//2-enemy.x-enemy.sx//2)**2+(panda.y+panda.sy//2-enemy.y-enemy.sy//2)**2))**(1/2)
        if panda.x < enemy.x:
            enemy.mv_x = -enemy.mv_x
        if panda.y < enemy.y:
            enemy.mv_y = -enemy.mv_y
        enemy.x += enemy.mv_x
        enemy.y += enemy.mv_y
    

    for i in range(len(enemies)):
        enemy = enemies[i]
        for j in range(len(bullets)):
            bullet = bullets[j]
            if crash(enemy, bullet):
                explosion_sound_1.play()
                dm_enemies.append(i)
                dm_bullets.append(j)
                killed += 1
    
    for i in range(len(items)):
        item = items[i]
        if crash(item, panda):
            panda.mv += 0.1
            dm_items.append(i)

    for i in range(len(bullet_items)):
        item = bullet_items[i]
        if crash(item, panda):
            bullet_size += 0.2
            dm_bullet_items.append(i)

    for i in range(len(enemies)):
        enemy = enemies[i]
        if crash(enemy, panda):
            dm_enemies.append(i)
            dm_lives.append(len(lives) - 1 )
    

    now_time = datetime.now()
    delta_time = round((now_time-start_time).total_seconds())
    level = delta_time//60
    screen.fill(color)

    panda.show()
    new_bullets = []
    for i in range(len(bullets)):
        bullet = bullets[i]
        if i not in dm_bullets:
            new_bullets.append(bullet)
            bullet.show()
    bullets = new_bullets[:]




    new_enemies = []
    for i in range(len(enemies)):
        enemy = enemies[i]
        if i not in dm_enemies:
            new_enemies.append(enemy)
            enemy.show()
    enemies = new_enemies[:]
    
    new_items = []
    for i in range(len(items)):
        item = items[i]
        if i not in dm_items:
            new_items.append(item)
            item.show()
    items = new_items[:]

    new_items = []
    for i in range(len(bullet_items)):
        item = bullet_items[i]
        if i not in dm_bullet_items:
            new_items.append(item)
            item.show()
    bullet_items = new_items[:]

    
    new_lives = []
    for i in range(len(lives)):
        life = lives[i]
        if i not in dm_lives:
            new_lives.append(life)
            life.show()
    lives = new_lives[:]

    # 목숨이 0일때 게임 종료
    if len(lives) == 0:
        explosion_sound_2.play()
        lose = font.render("GAME OVER", True, (255,0,0))
        screen.blit(lose, (400,400))
        pygame.display.flip()
        SB = 1
        time.sleep(4)

    text = font.render("killed : {}, time : {}, score : {}".format(killed, delta_time, killed+delta_time//10), True, (255,255,255))
    screen.blit(text, (10,5))
    
    #update
    pygame.display.flip()

pygame.quit()