import pygame

pygame.display.init()

# ref lista a tupla obtida a partir da função get_desktop_sizes 
ref = list(pygame.display.get_desktop_sizes()[0])
# permitindo a manipulação indiviudal dos valores por indice 
tela = pygame.display.set_mode((ref[0], ref[1]), pygame.RESIZABLE)
clock = pygame.time.Clock()
FPS = 50    

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        tela.fill((255,255,255))
        pygame.display.update()
        clock.tick(FPS)


game()
print(ref)
pygame.quit()
