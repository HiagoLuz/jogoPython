
import pygame
from random import randint

pygame.init()
x = 380
y = 100
pos_x = 526
pos_y = 1200
pos_y_a = 800
pos_y_c = 2000
timer = 0
tempo_segundo = 0
velocidade = 10
velocidade_outros= 12
fundo = pygame.image.load('fundo_mar1.png')
peixe = pygame.image.load('dori1.png')
tubarao = pygame.image.load('tubarao.png')
tubarao1 = pygame.image.load('tubarao.png')
tubarao2 = pygame.image.load('tubarao.png')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo: ",True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center= (65,50)

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_RIGHT] and x <= 520:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >=230:
        x -= velocidade

    if ((x + 60 > pos_x and y + 60 > pos_y)):
        y = 1200

    if ((x - 60 < pos_x - 300 and y + 60 > pos_y_a)):
        y = 1200

    if ((x + 60 > pos_x - 136 and y + 60 > pos_y_c)) and ((x - 60 < pos_x - 136 and y + 60 > pos_y_c)):
        y = 1200

    if (pos_y <= -80):
        pos_y = randint(800,1000)

    if ((pos_y_a <= -80)):
        pos_y_a = randint(1200,2000)

    if ((pos_y_c <= -80)):
        pos_y_c = randint(2200,3000)

    if (timer <20):
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255,255,255), (0,0,0))
        timer = 0

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +2
    pos_y_c -= velocidade_outros +10

    janela.blit(fundo, (0,0))
    janela.blit(peixe, (x,y))
    janela.blit(tubarao, (pos_x, pos_y))
    janela.blit(tubarao1, (pos_x - 300, pos_y_a))
    janela.blit(tubarao2, (pos_x - 136, pos_y_c))
    janela.blit(texto, pos_texto)
    pygame.display.update()

pygame.quit()
