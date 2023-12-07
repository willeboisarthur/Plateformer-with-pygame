import pygame
import pytmx
import pyscroll

from player import Player

pygame.init()


class Game:
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            self.player.move_right()
        elif pressed[pygame.K_q]:
            self.player.move_left()
        elif pressed[pygame.K_SPACE]:
            self.player.sauter = True

    def update(self):
        self.group.update()

        # vérification des collisions
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back

    def run(self):
        self.screen = pygame.display.set_mode((1000, 400))
        pygame.display.set_caption("plateformer")

        # charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('Niveau/Niveau_1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        # charger tout les calques
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1

        # generer un joueur
        player_position = tmx_data.get_object_by_name("spawn_player_level_1")
        self.player = Player(player_position.x, player_position.y)

        self.walls = []
        for objet in tmx_data.objects:
            if objet.type == "collision":
                self.walls.append(pygame.Rect(objet.x, objet.y, objet.width, objet.height))

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

        clock = pygame.time.Clock()

        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(144)

    pygame.quit()
