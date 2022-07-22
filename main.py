import pygame
import sys

pl_x=300-36
pl_y=700
b1_x=[0]*5
b1_y=[0]*5
b1_c=[False]*5
b1_tmr=0

imgPlayer1 = pygame.image.load("neko1.png")
imgPlayer2 = pygame.image.load("neko2.png")
imgBullet1 = pygame.image.load("Bullet01_16x16.png")

def draw_battle(bg):
    bg.fill((0,0,0))
    bg.blit(imgPlayer1, [pl_x,pl_y])
    bg.blit(imgPlayer2, [300-36,100])
    for idx in range(5):
        if b1_c[idx]==True:
            bg.blit(imgBullet1,[b1_x[idx],b1_y[idx]],(0,0,16,16))


def move_player():
    global pl_x,pl_y
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] == 1:
        if pl_y>0:pl_y-=5
    if key[pygame.K_DOWN] == 1:
        if pl_y<800-72:pl_y+=5
    if key[pygame.K_LEFT] == 1:
        if pl_x>0:pl_x-=5
    if key[pygame.K_RIGHT] == 1:
        if pl_x<600-72:pl_x+=5

def create_bullet1():
    global pl_x,pl_y,b1_tmr
    if b1_tmr>0:b1_tmr-=1
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == 1:
        if b1_tmr==0:
            for idx in range(5):
                if b1_c[idx]==False:
                    b1_c[idx]=True
                    b1_x[idx]=pl_x+32
                    b1_y[idx]=pl_y
                    b1_tmr=20
                    break






def main():
    pygame.init()
    pygame.display.set_caption("試作")
    screen = pygame.display.set_mode((600, 800))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        move_player()
        create_bullet1()
        draw_battle(screen)
        pygame.display.update()
        clock.tick(60)



if __name__=='__main__':
    main()
