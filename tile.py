import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        ampliacao = 4
        image = pygame.image.load(image).convert_alpha()
        image = pygame.transform.scale(image,(image.get_width()*ampliacao,image.get_height()*ampliacao))
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)