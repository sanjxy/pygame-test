import pygame
import os

WIDTH, HEIGHT = 1900, 1030
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("first app hehe")
FPS=60
SPACESHIP_HEIGHT,SPACESHIP_WIDTH=70,60

YELLOW_SPACESHIP=pygame.image.load(os.path.join('assets','spaceship_yellow.png'))
YELLOW_SPACESHIP_RESIZE=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP,(SPACESHIP_HEIGHT,SPACESHIP_WIDTH)),90)
RED_SPACESHIP=pygame.image.load(os.path.join('assets','spaceship_red.png'))
RED_SPACESHIP_RESIZE=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP,(SPACESHIP_HEIGHT,SPACESHIP_WIDTH)),270)



def draw(yellow,red):
    WIN.fill((100,0,0))
    WIN.blit(YELLOW_SPACESHIP_RESIZE,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP_RESIZE,(red.x,red.y))
    pygame.display.update()

def main():
    red=pygame.Rect(100,500,SPACESHIP_HEIGHT,SPACESHIP_WIDTH)
    yellow=pygame.Rect(1800,500,SPACESHIP_HEIGHT,SPACESHIP_WIDTH)
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:

        draw(red,yellow)
    pygame.quit

if __name__=="__main__":
    main()