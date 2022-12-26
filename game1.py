import pygame

pygame.init()

sc = pygame.display.set_mode((500 , 500), pygame.RESIZABLE)
#pygame.display.set_mode((800 , 1200), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN)
pygame.display.set_caption("Title")
pygame.display.set_icon(pygame.image.load("dig10k_penguin.bmp"))


WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255, 0, 0)

'''
pygame.draw.rect(sc, WHITE, (10,10,50,100),2)

pygame.draw.line(sc, BLUE, (200,20), (350,50),5)

pygame.draw.aaline(sc, GREEN, (250,20), (350,50))


pygame.draw.lines(sc, RED, True, [(200,150),  (250,20), (400,50)],5)

pygame.draw.aalines(sc, RED, True, [(300,150 ), (300,20), (350,50)])

pygame.draw.polygon(sc, GREEN, [[150,210], [180,250], [90,290],[30,230]])
pygame.draw.polygon(sc, GREEN, [[150,310], [180,350], [90,390],[30,330]] , 1)


pygame.draw.circle(sc, BLUE, (300,250), 25)

pygame.draw.ellipse(sc, WHITE, (300,300,100,50), 5)

pi = 3.14

pygame.draw.arc(sc, GREEN, (450,30,50,150), pi, 2*pi, 2)

pygame.display.flip()


'''
clock = pygame.time.Clock()
FPS = 60

flStartDraw = False
sp = ep = None
 
sc.fill(WHITE)
pygame.display.update()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            flStartDraw = True
            sp = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if flStartDraw:
                pos = event.pos
 
                width = pos[0] - sp[0]
                height = pos[1] - sp[1]
 
                sc.fill(WHITE)
                pygame.draw.rect(sc, RED, pygame.Rect(sp[0], sp[1], width, height))
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            flStartDraw = False
 
    clock.tick(FPS)


    '''
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка: " , event.button)
        elif event.type == pygame.MOUSEMOTION:
            print("Позиция мыши: ", event.pos)
            print("Позиция мыши: ", event.rel)
    '''

           
