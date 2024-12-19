import pygame
import math

pygame.display.init()

# ref lista a tupla obtida a partir da função get_desktop_sizes 
ref = list(pygame.display.get_desktop_sizes()[0])
# permitindo a manipulação indiviudal dos valores por indice 
tela = pygame.display.set_mode((ref[0], ref[1]), pygame.RESIZABLE)
clock = pygame.time.Clock()
FPS = 50    

Preto = (0,0,0)
Branco = (255,255,255)
Azul = (0,0,255)
centro_tabuleiro = pygame.math.Vector2(ref[0]/2, ref[1]/2.2)


def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        tela.fill((255,255,255))
        

        

        for i in range (10):
            pygame.draw.circle(tela, Preto, centro_tabuleiro, 30*i, 1)

        
        construir_linhas(tela, Azul, centro_tabuleiro, 24, 300)
        construir_linhas(tela, Preto, centro_tabuleiro, 12, 300)
        
            

        pygame.display.update()
        clock.tick(FPS)

def construir_linhas(tela, cor, posicao_inicial, indice, raio):
    for i in range(indice):
            # o loop for interará para criar os valores dos angulos baseados nessa formula
            # extraindo o valor dos graus e convertendo para radianos
            angulo = (i * 360 / indice) * (math.pi / 180) 

            # depois disso é calculado os angulos finais utilizando seno e cosseno do angulo
            x = centro_tabuleiro.x + (raio - 30) * math.cos(angulo)
            y = centro_tabuleiro.y + (raio - 30) * math.sin(angulo)

            # criada a tupla, podemos adiciona-la no parametro final da função draw
            ponto_final = (x,y)
            pygame.draw.line(tela, cor, posicao_inicial, ponto_final)

game()
print(centro_tabuleiro)
pygame.quit()
