import pygame
from tile import Tile


class Interativo(Tile):
    def __init__(self, image, pos, tipo):
        super().__init__(image, pos)
        self.n = 1

        self.tipo = tipo


    def interacao(self):
        print("Você interagiu com este objeto! ", self.n)
        self.n += 1