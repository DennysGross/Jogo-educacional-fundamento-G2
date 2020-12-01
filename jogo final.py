# pip instalal pygame
#importar as bibliotecas
import random
import time
import pygame

# informar nome e e-mail e gravar no .txt
nome = input("Insira seu nome: ")
email = input("Insira seu E-mail: ")
historico = open("historico.txt", "a")
historico.write("Nome: "+nome+", E-mail: "+email+"\n")
historico.close()

# inicializando o pygame, inicializando a tela com determinada largura e altura
pygame.init()
relogio = pygame.time.Clock()
largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))

# subindo os arquivos para o programa, backgrud, etiquetas, silhuetas, final e seta
#background
background = pygame.image.load("assets/fundo.png")

efruta1 = pygame.image.load("assets/ebanana.png")
efruta2 = pygame.image.load("assets/elaranja.png")
efruta3 = pygame.image.load("assets/emaca.png")
efruta4 = pygame.image.load("assets/epera.png")

sfruta1 = pygame.image.load("assets/sbanana.png")
sfruta2 = pygame.image.load("assets/slaranja.png")
sfruta3 = pygame.image.load("assets/smaca.png")
sfruta4 = pygame.image.load("assets/spera.png")

ffruta1 = pygame.image.load("assets/fbanana.png")
ffruta2 = pygame.image.load("assets/flaranja.png")
ffruta3 = pygame.image.load("assets/fmaca.png")
ffruta4 = pygame.image.load("assets/fpera.png")

seta = pygame.image.load("assets/seta.png")

#definindo algumas variaveis
posicaoX = 400
posicaoY = 10
movimentoX = 0
movimentoY = 0

aleatorio = 1
frutanahora = sfruta1

# definindo função acerto
def acerto(acerto):
    font = pygame.font.SysFont(None, 100)
    texto = font.render("Certo!", True, (0, 0, 0))
    return texto

# definindo funcao erro
def erro(erro):
    font = pygame.font.SysFont(None, 100)
    texto = font.render("Errado!", True, (0, 0, 0))
    return texto

while True:
    # iniciando os arquivos, em 
    display.fill((0, 255, 255))
    display.blit(background, (0, 0))

    display.blit(efruta1, (0, 500))
    display.blit(efruta2, (200, 500))
    display.blit(efruta3, (400, 500))
    display.blit(efruta4, (600, 500))

    display.blit(seta, (posicaoX, posicaoY )) 

    display.blit(frutanahora, (0,0)) 


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimentoX = -5
            elif evento.key == pygame.K_RIGHT:
                movimentoX = 5
            elif evento.key == pygame.K_UP:
                movimentoY = -5
            elif evento.key == pygame.K_DOWN:
                movimentoY = 5
        if evento.type == pygame.KEYUP:
            movimentoX = 0
            movimentoY = 0
    
    posicaoX = posicaoX + movimentoX
    posicaoY = posicaoY + movimentoY

    if posicaoX < 0 :
        posicaoX = 0
    elif posicaoX > largura - 10:
        posicaoX = largura - 10
    elif posicaoY < 0:
        posicaoY = 0

    if posicaoY > 500:
        if aleatorio == 1:
            if posicaoX > 0 and posicaoX < 200:
                display.blit(ffruta1, (0,0))
                texto = acerto(acerto)
                display.blit(texto, (350, 200))
                pygame.display.update()
                time.sleep(2)
            else:
                texto = erro(erro)
                display.blit(texto, (300, 300))
                pygame.display.update()
                time.sleep(0.5)      
     
        elif aleatorio == 2:
            if posicaoX > 200 and posicaoX < 400: 
                display.blit(ffruta2, (0,0))
                texto = acerto(acerto)
                display.blit(texto, (300, 300))
                pygame.display.update()
                time.sleep(2)
            else:
                texto = erro(erro)
                display.blit(texto, (300, 300))
                pygame.display.update()
                time.sleep(0.5)
    
        elif aleatorio == 3:
            if posicaoX > 400 and posicaoX < 600:
                display.blit(ffruta3, (0,0))
                texto = acerto(acerto)
                display.blit(texto, (300, 300))
                pygame.display.update()
                time.sleep(2)
            else:
                texto = erro(erro)
                display.blit(texto, (300, 300))
                pygame.display.update()
                time.sleep(0.5)
     
        elif aleatorio == 4:
            if posicaoX > 600 and posicaoX < 800:
                display.blit(ffruta4, (0,0))
                texto = acerto(acerto)
                display.blit(texto, (3000, 300))
                pygame.display.update()
                time.sleep(2)
            else:
                texto = erro()
                display.blit(texto, (400, 300))
                pygame.display.update()
                time.sleep(0.5)

    if posicaoY > 500:
        aleatorio = random.randrange(1, 5)
        if aleatorio == 1:
            frutanahora = sfruta1
        elif aleatorio == 2:
            frutanahora = sfruta2
        elif aleatorio == 3:
            frutanahora = sfruta3
        elif aleatorio == 4:
            frutanahora = sfruta4
        
        posicaoX = 400
        posicaoY = 10 
    

    pygame.display.update()
    relogio.tick(60)
    