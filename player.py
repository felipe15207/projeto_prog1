import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.hp = 200

        image = pygame.image.load(r"assets/player/player_frente0.png").convert_alpha()
        image = pygame.transform.scale(image,(image.get_width()*4,image.get_height()*4))
        self.image = image

        self.rect = image.get_rect(topleft=pos)

        self.andar = 0
        self.fase = [(350,130), (1250,650)]

    def move(self, obstaculos, interativo):
        teclas = pygame.key.get_pressed()
        dx,dy = 0,0
        passo = 5
        if teclas[pygame.K_w]:
            dy = -passo
        elif teclas[pygame.K_s]:
            dy = passo
        elif teclas[pygame.K_a]:
            dx = -passo
        elif teclas[pygame.K_d]:
            dx = passo

        mov_x, mov_y = dx,dy
    
        self.rect.x += dx

        for objeto in pygame.sprite.spritecollide(self, obstaculos, False):
            mov_x = 0
            if dx > 0:
                self.rect.right = objeto.rect.left
            elif dx < 0:
                self.rect.left = objeto.rect.right

        self.rect.y += dy

        for objeto in pygame.sprite.spritecollide(self, obstaculos, False):
            mov_y = 0
            if dy > 0:
                self.rect.bottom = objeto.rect.top
            elif dy < 0:
                self.rect.top = objeto.rect.bottom

        colisao = pygame.sprite.spritecollide(self, interativo, False)
        if colisao:
            objeto = colisao[0]
            if teclas[pygame.K_e]:
                objeto.interacao()
                if objeto.tipo == "ec" and 0 < self.andar:
                    self.andar -= 1
                    self.rect.x, self.rect.y = self.fase[1]
                elif objeto.tipo == "eb" and self.andar < 3:
                    self.andar += 1
                    self.rect.x, self.rect.y = self.fase[0]
                print(self.andar)

            if objeto.tipo == "inimigo":
                self.hp -= 1



        return (mov_x, mov_y)