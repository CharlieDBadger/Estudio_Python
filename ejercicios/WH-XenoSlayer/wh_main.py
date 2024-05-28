import os
import pygame
import random
import math
from pygame import mixer

# Obtén la ruta del directorio actual (donde se encuentra tu archivo wh_main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Vidas del jugador
player_lives = 3


class Ship:
    def __init__(self, image, coordinate_x, coordinate_y, speed):
        self.image = image
        self.speed = speed
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.direction_x = 0
        self.direction_y = 0

    def move(self):
        self.coordinate_x += self.speed * self.direction_x
        self.coordinate_y += self.speed * self.direction_y

    def show(self, screen):
        screen.blit(self.image, (self.coordinate_x, self.coordinate_y))


class PlayerShip(Ship):
    def __init__(self, image, coordinate_x, coordinate_y, speed):
        super().__init__(image, coordinate_x, coordinate_y, speed)

    def limit_position(self):
        if self.coordinate_x <= 10:
            self.coordinate_x = 10
        elif self.coordinate_x >= 740:
            self.coordinate_x = 740
        if self.coordinate_y <= 10:
            self.coordinate_y = 10
        elif self.coordinate_y >= 500:
            self.coordinate_y = 500

    def update_direction(self, ship_player_direction_x, ship_player_direction_y):
        self.direction_x = ship_player_direction_x
        self.direction_y = ship_player_direction_y


class EnemyShip(Ship):
    def __init__(self, image, coordinate_x, coordinate_y, speed):
        super().__init__(image, coordinate_x, coordinate_y, speed)
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

    def update_direction(self):
        if self.coordinate_x <= 10 or self.coordinate_x >= 740:
            self.direction_x *= -1
        if self.coordinate_y <= 10 or self.coordinate_y >= 500:
            self.direction_y *= -1

    def respawn(self):
        self.coordinate_x = random.randint(20, 736)
        self.coordinate_y = random.randint(20, 500)
        self.direction_x = random.choice([-1, 1])  # Nueva dirección aleatoria en el eje x
        self.direction_y = random.choice([-1, 1])  # Nueva dirección aleatoria en el eje y


class Beam:
    def __init__(self, image, coordinate_x, coordinate_y, speed, active):
        self.active = active
        self.image = image
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.speed = speed
        self.beam_active = active

    def fire(self, coordinate_x, coordinate_y):
        if not self.active:
            self.coordinate_x = coordinate_x
            self.coordinate_y = coordinate_y
            self.active = True

    def move(self):
        if self.active:
            self.coordinate_y -= self.speed
            if self.coordinate_y <= -40:
                self.active = False  # Aquí simplemente desactivamos el rayo cuando sale de la pantalla

    def show(self, screen):
        if self.active:
            screen.blit(self.image, (self.coordinate_x + 14, self.coordinate_y - 40))


class Animation:
    def __init__(self, path, file_name, num_images, size, coordinate_x, coordinate_y, speed):
        self.images = self.import_and_scale_images(path, file_name, num_images, size)
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.speed = speed
        self.current_image = 0

    def import_and_scale_images(self, path, file_name, num_images, size):
        images = []
        for i in range(1, num_images + 1):
            image_path = os.path.join(path, f'{file_name}{i}.png')
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (size, size))
            images.append(image)
        return images

    def update(self):
        self.current_image += self.speed
        if self.current_image >= len(self.images):
            self.current_image = 0
            return False
        return True

    def show(self, screen):
        screen.blit(self.images[int(self.current_image)], (self.coordinate_x, self.coordinate_y))


def show_lives(lives, x, y):
    lives_text = font.render("Vidas : " + str(lives), True, (255, 255, 255))
    game_screen.blit(lives_text, (x, y))


def show_game_over():
    game_over_font = pygame.font.Font(font_path, 72)  # Define the font for the game over text
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    game_screen.blit(game_over_text, (200, 250))  # Display the game over text at the center of the screen


def import_pygame_image(image_name, new_width):
    # Carga la imagen desde el directorio de recursos
    image = pygame.image.load(os.path.join(current_dir, 'resources', image_name))

    # Obtiene las dimensiones originales de la imagen
    original_width, original_height = image.get_size()

    # Calcula la relación de aspecto de la imagen
    aspect_ratio = original_height / original_width

    # Calcula la nueva altura de la imagen manteniendo la misma relación de aspecto
    new_height = int(new_width * aspect_ratio)

    # Redimensiona la imagen a las nuevas dimensiones y la devuelve
    return pygame.transform.scale(image, (new_width, new_height))


def import_pygame_soundtrack(sound_name, volume=1.0):
    mixer.music.load(os.path.join(current_dir, 'resources', sound_name))
    mixer.music.set_volume(volume)
    mixer.music.play(-1)


def import_pygame_sound(sound_name, volume=1.0):
    sound = mixer.Sound(os.path.join(current_dir, 'resources', sound_name))
    sound.set_volume(volume)
    return sound


def formula_collision(x1, y1, x2, y2, collision_distance):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distance < collision_distance:
        return True
    return False


explosions = []
respawns_animation = []


def beam_impact(beam, player_ship, enemy_ship):
    global score  # Declaramos score como global
    if formula_collision(beam.coordinate_x, beam.coordinate_y, enemy_ship.coordinate_x, enemy_ship.coordinate_y,
                         35):
        collision_sound.play()
        beam.coordinate_y = player_ship.coordinate_y
        beam.active = False
        score += 1
        print(score)
        # Animación de la explosión
        beam_explosion = Animation(os.path.join(current_dir, 'resources'), 'explosion-', 8, 100,
                                   ship_xenos.coordinate_x, ship_xenos.coordinate_y, 0.2)
        # Agregar la animación a la lista de explosiones
        explosions.append(beam_explosion)
        # Respawn de la nave enemiga en una posición aleatoria
        enemy_ship.respawn()
        # Animation respawn
        respawn_enemy = Animation(os.path.join(current_dir, 'resources'), 'respawn-', 8, 70,
                                  ship_xenos.coordinate_x, ship_xenos.coordinate_y, 0.2)
        # Agregar la animación a la lista de respawns
        respawns_animation.append(respawn_enemy)
        if score % 10 == 0 and score != 0:
            ship_xenos.speed += 2


def ships_impact(player_ship, enemy_ship):
    global player_lives  # Declaramos player_lives como global
    if formula_collision(player_ship.coordinate_x, player_ship.coordinate_y, enemy_ship.coordinate_x,
                         enemy_ship.coordinate_y, 35):
        collision_sound.play()
        if player_lives != 1:
            # Restar una vida al jugador
            player_lives -= 1
            print("¡Colisión entre el jugador y el enemigo! Vidas restantes: ", player_lives)

            # Mostrar una animación de explosión
            ship_explosion = Animation(os.path.join(current_dir, 'resources'), 'explosion-', 8, 100,
                                       player_ship.coordinate_x, player_ship.coordinate_y, 0.2)
            # Agregar la animación a la lista de explosiones
            explosions.append(ship_explosion)

            # Respawn de la nave enemiga en una posición aleatoria
            enemy_ship.respawn()
            # Animation respawn
            respawn_enemy = Animation(os.path.join(current_dir, 'resources'), 'respawn-', 8, 70,
                                      ship_xenos.coordinate_x, ship_xenos.coordinate_y, 0.2)
            # Agregar la animación a la lista de respawns
            respawns_animation.append(respawn_enemy)
        else:
            show_game_over()
            pygame.display.flip()
            pygame.time.delay(3000)
            pygame.quit()

def show_score(game_score, x, y):
    score_text = font.render("Score : " + str(game_score), True, (255, 255, 255))
    game_screen.blit(score_text, (x, y))


# Inicializar Pygame
pygame.init()

# Establecer el tamaño de la ventana
game_screen = pygame.display.set_mode((800, 600))

# TITTLE AND ICON
pygame.display.set_caption("Warhammer 40K: XenoSlayer")
icon = import_pygame_image('icon.png', 32)
pygame.display.set_icon(icon)

# IMAGE BACKGROUND
background = import_pygame_image('background.png', 800)

# IMAGE INTERFACE
interface = import_pygame_image('interface.png', 800)

# MUSICA DE FONDO
import_pygame_soundtrack('Danimal Cannon & Zef - The Lunar Whale.mp3', 0.3)

# BEAM SOUND
beam_sound = import_pygame_sound('beam.mp3', 0.5)

# COLLISION SOUND
collision_sound = import_pygame_sound('collision.mp3', 0.5)

# SCORE
score = 0
font_path = os.path.join(current_dir, 'resources', 'Pokemon Emerald Latin FC.ttf')
font_size = 12
font = pygame.font.Font(font_path, font_size)
texto_x = 25
texto_y = 528

# JUGADOR
ship_player_image = import_pygame_image('ship.png', 50)
ship_player = PlayerShip(ship_player_image, 380, 490, 10)

# XENOS
ship_xenos_image = import_pygame_image('necron_ship.png', 25)
ship_xenos = EnemyShip(ship_xenos_image, 380, 100, 5)

# Rayo Jugador
beam_player_image = import_pygame_image('ship_beam.png', 20)
beam_player = Beam(beam_player_image, 0, 480, 20, False)

# Bucle principal del juego
running = True
while running:

    # Rellenar la pantalla con color
    game_screen.blit(background, (0, 0))

    # Eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Eventos de teclado
        if event.type == pygame.KEYDOWN:
            # Movimiento del jugador
            if event.key == pygame.K_LEFT:
                ship_player.update_direction(-1, ship_player.direction_y)
            if event.key == pygame.K_RIGHT:
                ship_player.update_direction(1, ship_player.direction_y)
            if event.key == pygame.K_UP:
                ship_player.update_direction(ship_player.direction_x, -1)
            if event.key == pygame.K_DOWN:
                ship_player.update_direction(ship_player.direction_x, 1)
            # Disparar el rayo
            if event.key == pygame.K_SPACE:
                beam_sound.play()
                beam_player.fire(ship_player.coordinate_x, ship_player.coordinate_y)
        if event.type == pygame.KEYUP:
            # Detener el movimiento del jugador
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                keys = pygame.key.get_pressed()
                direction_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
                direction_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
                ship_player.update_direction(direction_x, direction_y)

    # Actualizar y Limitar la posición del jugador.
    ship_player.move()
    ship_player.limit_position()

    # Actualizar y Limitar la posición del enemigo y cambiar de dirección si llega a un borde.
    ship_xenos.move()
    ship_xenos.update_direction()

    # Colisión entre el rayo y el enemigo
    beam_impact(beam_player, ship_player, ship_xenos)
    ships_impact(ship_player, ship_xenos)

    # Actualizar la posición del rayo
    beam_player.move()



    # Actualizar y mostrar todas las animaciones de respawn
    for respawn in respawns_animation[:]:
        if not respawn.update():
            # Si la animación ha terminado, la eliminamos de la lista
            respawns_animation.remove(respawn)
        else:
            respawn.show(game_screen)

    # Mostrar elementos en pantalla
    game_screen.blit(interface, (0, 0))
    show_score(score, 25, 528)
    show_lives(player_lives, 25, 500)  # Ajusta las coordenadas según tus necesidades
    ship_player.show(game_screen)
    ship_xenos.show(game_screen)
    beam_player.show(game_screen)

    # Actualizar y mostrar todas las animaciones de explosión
    for explosion in explosions[:]:
        if not explosion.update():
            # Si la animación ha terminado, la eliminamos de la lista
            explosions.remove(explosion)
        else:
            explosion.show(game_screen)

    # Actualizar la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
