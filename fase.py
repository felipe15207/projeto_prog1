import pygame

from tile import Tile
from interativo import Interativo

class Fase:
    def __init__(self, visiveis, obstaculos, interativos, mapa):
        self.mapa = mapa
        self.visiveis = visiveis
        self.obstaculos = obstaculos
        self.interativos = interativos
        self.TILESIZE = 32 * 4
        self.construir(0)


    def construir(self, andar):
        for y, y_elemento in enumerate(self.mapa[andar]):
            for x, x_elemento in enumerate(y_elemento):
                if x_elemento == ' ':
                    tile = Tile(image="assets/mapa_sprites/chao_tipo1.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.visiveis.add(tile)
                elif x_elemento == 'p':
                    tile = Tile(image="assets/mapa_sprites/parede_isolada.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.obstaculos.add(tile)
                elif x_elemento == 'pld':
                    tile = Tile(image="assets/mapa_sprites/parede_lateral_direita.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.obstaculos.add(tile)
                elif x_elemento == 'ple':
                    tile = Tile(image="assets/mapa_sprites/parede_lateral_esquerda.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.obstaculos.add(tile)
                elif x_elemento == 'ph':
                    tile = Tile(image="assets/mapa_sprites/parede_horizontal.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.obstaculos.add(tile)
                elif x_elemento == 'phu':
                    tile = Tile(image="assets/mapa_sprites/parede_ligacao_para_cima.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.obstaculos.add(tile)
                elif x_elemento == 'phd':
                    tile = Tile(image="assets/mapa_sprites/parede_lado_direito.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.obstaculos.add(tile)
                elif x_elemento == 'phe':
                    tile = Tile(image="assets/mapa_sprites/parede_lado_esquerdo.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.obstaculos.add(tile)
                elif x_elemento == 'cs':
                    tile = Tile(image="assets/mapa_sprites/chao_sombra_parede.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.visiveis.add(tile)
                elif x_elemento == 'cp1':
                    tile = Tile(image="assets/mapa_sprites/chao_tipo2.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.visiveis.add(tile)
                elif x_elemento == 'cp2':
                    tile = Tile(image="assets/mapa_sprites/chao_tipo3.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.obstaculos.add(tile)
                elif x_elemento == 'cp3':
                    tile = Tile(image="assets/mapa_sprites/chao_tipo4.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.obstaculos.add(tile)
                elif x_elemento == 'ec':
                    tile = Interativo(image="assets/mapa_sprites/escadaria_cima.png", pos=(x*self.TILESIZE,y*self.TILESIZE), tipo="ec")
                    self.interativos.add(tile)
                elif x_elemento == 'eb':
                    tile = Interativo(image="assets/mapa_sprites/escadaria_baixo.png", pos=(x*self.TILESIZE,y*self.TILESIZE), tipo="eb")
                    self.interativos.add(tile)
                elif x_elemento == 't':
                    tile = Tile(image="assets/mapa_sprites/chao_com_tocha1.png", pos=(x*self.TILESIZE,y*self.TILESIZE))
                    self.obstaculos.add(tile)
                elif x_elemento == 'b':
                    tile = Interativo(image="assets/mapa_sprites/chao_com_bau1.png", pos=(x*self.TILESIZE,y*self.TILESIZE), tipo="bau")
                    self.interativos.add(tile)
                elif x_elemento == 'x':
                    tile = Interativo(image="assets/mapa_sprites/demon1.png", pos=(x*self.TILESIZE,y*self.TILESIZE), tipo="inimigo")
                    self.interativos.add(tile)
                elif x_elemento == 'z':
                    tile = Interativo(image="assets/mapa_sprites/demon2.png", pos=(x*self.TILESIZE,y*self.TILESIZE), tipo="inimigo")
                    self.interativos.add(tile)


    def trocar_fase(self, andar):
        self.visiveis.empty()
        self.obstaculos.empty()
        self.interativos.empty()
        self.construir(andar)