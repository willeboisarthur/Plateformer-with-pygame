import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Player, self).__init__()
        self.sprite_sheet = pygame.image.load('Animation personnage/frame animation.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.saut = 0
        self.saut_montee = 0
        self.saut_enbas = 5
        self.nombre_de_saut = 0
        self.sauter = False
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_possition = self.position.copy()

    def save_location(self):
        self.old_possition = self.position.copy()

    def move_right(self):
        self.position[0] += 2

    def move_left(self):
        self.position[0] -= 2

    def move_up(self):

        if self.sauter:
            if self.saut_montee >= 10:
                self.saut_enbas -= 1
                self.saut = self.saut_enbas
            else:
                self.saut_montee += 1
                self.saut = self.saut_montee
            if self.saut_enbas < 0:
                self.saut_montee = 0
                self.saut_enbas = 5
                self.sauter = False
        self.rect.y = self.rect.y - (10 * (self.saut / 2))

    def save_location(self): self.old_possition = self.position.copy()

    def update(self):
        self.rect.midbottom = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):

        self.rect.midbottom = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
