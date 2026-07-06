import pygame

from fase import Fase
from tilemaps import tilemap
from player import Player

pygame.init()

TAM_TELA = (1600,900)
tela = pygame.display.set_mode(TAM_TELA)
pygame.display.set_caption("Dungeon Blitz")

FPS = 60
clock = pygame.time.Clock()

visiveis = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()
interativos = pygame.sprite.Group()
personagens = pygame.sprite.Group()

dungeon = Fase(visiveis, obstaculos, interativos, tilemap)
andar_atual = 0

jogador = Player((350,130))
personagens.add(jogador)

superficie = pygame.Surface((1600,900))

barra_hp = pygame.Surface((200,20))
barra_hp.fill((255,255,255))

executar = True
while executar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executar = False

    mov_x, mov_y = jogador.move(obstaculos, interativos)

    if andar_atual != jogador.andar:
        dungeon.trocar_fase(jogador.andar)

    tela.fill((255,255,255))
    superficie.fill((0,0,0))

    visiveis.draw(superficie)
    obstaculos.draw(superficie)
    interativos.draw(superficie)

    tela.blit(superficie, (0,0))
    personagens.draw(tela)

    tela.blit(barra_hp,(1350,850))
    hp = pygame.draw.rect(tela,(120,0,0),(1350,850,jogador.hp,20))

    clock.tick(FPS)
    pygame.display.flip()
