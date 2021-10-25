if __name__ == '__main__':
    # Importamos el modulo de pygame
    import pygame
    # Importamos random para numeros aleatorios
    import random
    #Importamos time para poder usar el .sleep
    import time

    # Import pygame.locals for easier access to key coordinates
    # Updated to conform to flake8 and black standards
    from pygame.locals import (
        K_UP,
        K_w,
        K_a,
        K_d,
        K_s,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        RLEACCEL,
        QUIT
    )

    
    # Iniciamos el sonido
    pygame.mixer.init()

    #Creamos varables para guardar los sonidos
    move_up_sound = pygame.mixer.Sound("resources/Rising_putter.ogg")
    move_down_sound = pygame.mixer.Sound("resources/Falling_putter.ogg")
    collision_sound = pygame.mixer.Sound("resources/Collision.ogg")
    #Le subimos el volumen a la colisión (Aun que creo que no sirve)
    collision_sound.set_volume(2.5)

    

    # Define a Player object by extending pygame.sprite.Sprite
    # The surface drawn on the screen is now an attribute of 'player'
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            # Create a surface and pass in a tuple containing its length and width
            self.surf = pygame.image.load("resources/jet.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()

        # Hacemos todos los ifs para que cuando presione cierta tecla se mueva el jugador
        def update(self, pressed_keys):
            if pressed_keys[K_UP] or pressed_keys [K_w]:
                self.rect.move_ip(0, -5)
                move_up_sound.play()
            if pressed_keys[K_DOWN] or pressed_keys [K_s]:
                self.rect.move_ip(0, 5)
                move_down_sound.play()
            if pressed_keys[K_LEFT] or pressed_keys [K_a]:
                self.rect.move_ip(-5, 0)
            if pressed_keys[K_RIGHT] or pressed_keys [K_d]:
                self.rect.move_ip(5, 0)

            # Estos ifs sirven para que el jugador no se salga de la pantalla
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    # Cremos la clase enemigo con la imagen del misil
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.image.load("resources/missile.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT),
                )
            )
            self.speed = random.randint(5, 20)

        def update(self):
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                self.kill()

    # Creamos la clase nube con la imagen de la nube
    class Cloud(pygame.sprite.Sprite):
        def __init__(self):
            super(Cloud, self).__init__()
            self.surf = pygame.image.load("resources/cloud.png").convert()
            self.surf.set_colorkey((0, 0 , 0), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT),
                )
            )

        def update(self):
            self.rect.move_ip(-5, 0)
            if self.rect.right < 0:
                self.kill()
           

        # Move the sprite based on speed
        # Remove the sprite when it passes the left edge of the screen
        
# Definimos las constantes de la altura y la anchura 
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600


    

    # Inicializamos el juego


    pygame.init()


#Añadimos la musica al juego
    pygame.mixer.music.load("resources/Apoxode_-_Electric_1.ogg")
    pygame.mixer.music.play(loops=-1)


    
    

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a custom event for adding a new enemy
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)

    # Añadimos las nubes al juego
    ADDCLOUD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCLOUD, 1000)

    # Instantiate player. Right now, this is just a rectangle.
    player = Player()

    # Create groups to hold enemy sprites and all sprites
    # - enemies is used for collision detection and position updates
    # - all_sprites is used for rendering
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Variable to keep the main loop running
    running = True

# Creamos la variable clock para inicializarla
    clock = pygame.time.Clock()

    # Main loop
    while running:
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    running = False
            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                running = False
            # Add a new enemy?
            elif event.type == ADDENEMY:
                # Create the new enemy and add it to sprite groups
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDCLOUD:
                #Añadimos la nuve al grupo de sprite
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        # Update enemy position
        enemies.update()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)

        # Actualizamos las nubes
        clouds.update()

        player.update(pressed_keys)

        # Ponemos el fondo azul
        screen.fill((140, 206, 250))

        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        

        # Sirve para saber si el jugador colisiona con algun enemigo
        if pygame.sprite.spritecollideany(player, enemies):
            # Si colisiona, hacemos que suene el sonido de la colisión, que espere 5 segundos, que mate al jugador y que termine la partida
            collision_sound.play()
            time.sleep (0.5)
            player.kill()
            running = False

        pygame.display.flip()
    
        #Configuramos el reloj a 50
        clock.tick(50)


    pygame.mixer.music.stop()

    pygame.mixer.quit()
        
      


