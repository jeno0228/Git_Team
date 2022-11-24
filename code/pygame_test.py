import pygame 
import random
import time
from datetime import datetime
#아이템, 이동방향(4), 목표물 4면
pygame.init()
size = [900,900]
screen = pygame.display.set_mode(size)

#게임창 옵션 설정
title = "My Game"
pygame.display.set_caption(title)

# 게임 내 필요한 설정
clock = pygame.time.Clock()

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

panda = obj()
panda.put_img("ss.png")
panda.change_size(50,50)
bullets = []
enemies = []
spawn = []
for i in range(size[1]):
    spawn.append((0,i))
    spawn.append((size[0],i))
for i in range(size[0]):
    spawn.append((i,0))
    spawn.append((i,size[1]))




panda.x = (size[0]-panda.sx)//2
panda.y = (size[1]-panda.sy)//2
panda.mv = 5    #이속증가 템 추가


left_go = False
right_go = False
up_go = False
down_go = False
shooting = False
color = (0,0,0)
killed = 0
font = pygame.font.Font("bold_pw.ttf",20)

start_time = datetime.now()
SB = 0
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
        elif event.type == pygame.MOUSEBUTTONUP:
            shooting = False


    if panda.x > 0 and left_go:
        panda.x -= panda.mv
    if (panda.x+panda.sx)<size[0] and right_go:
        panda.x += panda.mv
    if panda.y > 0 and up_go:
        panda.y -= panda.mv
    if (panda.y+panda.sy)<size[1] and down_go:
        panda.y += panda.mv
    if shooting:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet = obj()
            bullet.put_img("bullet.jpg")
            bullet.change_size(5,5)
            bullet.mv = 8
            bullet.mv_x = ((bullet.mv**2)*(mouse_x-panda.x-panda.sx//2)**2//((mouse_x-panda.x-panda.sx//2)**2+(mouse_y-panda.y-panda.sy//2)**2))**(1/2)
            bullet.mv_y = ((bullet.mv**2)*(mouse_y-panda.y-panda.sy//2)**2//((mouse_x-panda.x-panda.sx//2)**2+(mouse_y-panda.y-panda.sy//2)**2))**(1/2)
            if mouse_x < panda.x:
                bullet.mv_x = -bullet.mv_x
            if mouse_y < panda.y:
                bullet.mv_y = -bullet.mv_y
            bullet.x = panda.x+panda.sx//2
            bullet.y = panda.y+panda.sy//2
            bullets.append(bullet)
    dm_bullets = []
    dm_enemies = []
    for i in range(len(bullets)):
        bullet = bullets[i]
        bullet.x += bullet.mv_x
        bullet.y += bullet.mv_y
        if bullet.y <= -bullet.sy or bullet.x <= -bullet.sx or bullet.x > size[0] or bullet.y > size[1]:
            dm_bullets.append(i)
    
    if random.random() > 0.98:
        enemy = obj()
        enemy.put_img("aa.png")
        enemy.change_size(15,15)
        enemy.x, enemy.y = random.choice(spawn)
        enemy.mv = 4
        enemies.append(enemy)

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
                dm_enemies.append(i)
                dm_bullets.append(j)
                killed += 1
    for enemy in enemies:
        if crash(enemy, panda):
            lose = font.render("GAME OVER", True, (255,0,0))
            screen.blit(lose, (400,400))
            pygame.display.flip()
            SB = 1
            time.sleep(1)
    now_time = datetime.now()
    delta_time = (now_time-start_time).total_seconds()
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
    
    text = font.render("killed : {}, time : {}".format(killed, delta_time), True, (255,255,255))
    screen.blit(text, (10,5))
    
    #update
    pygame.display.flip()

pygame.quit()