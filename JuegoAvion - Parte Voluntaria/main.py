from pygame import color

if __name__ == '__main__':
    # Importamos el modulo de pygame
    import pygame
    # Importamos random para numeros aleatorios
    import random
    #Importamos time para poder usar el .sleep
    import time

    import os

    import sqlite3

    from sqlite3 import Error

    archivo = os.path.dirname(__file__)
  

    # Import pygame.locals for easier access to key coordinates
    # Updated to conform to flake8 and black standards
    from pygame.locals import (
        K_UP,
        K_w,
        K_a,
        K_d,
        K_s,
        K_p,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        RLEACCEL,
        QUIT
    )

    
    # Iniciamos el sonido
    pygame.mixer.init(44100, 16, 2, 4096)
    

    #Creamos varables para guardar los sonidos
    move_up_sound = pygame.mixer.Sound(os.path.join(archivo, "resources/Rising_putter.wav"))
    move_down_sound = pygame.mixer.Sound(os.path.join(archivo, "resources/Falling_putter.wav"))
    collision_sound = pygame.mixer.Sound(os.path.join(archivo, "resources/Collision.wav"))

    #Le subimos el volumen a la colisión (Aun que creo que no sirve)
    collision_sound.set_volume(2.5)
    
    #Creamos 3 variables de colores para poder usarlas más tarde
    BLANCO = (255, 255, 255)
    AZUL =  (140, 206, 250)
    NEGRO = (0,0,0)

    #Cremos 2 variables globales para el marcador y el nivel
    global marcador
    marcador = 0

    global nivel
    nivel = 1 

    carpeta = os.path.dirname(__file__)

    
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
            if pressed_keys [K_p]:
                continuar = False

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
            #Le ponemos la velocidad a los misiles con un random y dependiendo del nivel 
            self.speed = random.randint(2*nivel, 10+3*nivel)


    #Hacemos el update de la clase enemy
        def update(self):
            global marcador
            global nivel
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                for a in enemies:
                    if a.rect.right <= 1:
                        marcador +=10
                        if marcador%500==0:
                            nivel += 1
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
    class item (pygame.sprite.Sprite):
        def __init__(self):
            super(item, self).__init__()
            self.surf = pygame.image.load("resources/item.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                    random.randint(0, SCREEN_HEIGHT),
                )
            )
            #A el item le ponemos una velocidad fija
            self.speed = 15


    
        def update(self):
            global marcador
            global nivel
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                for a in items:
                    if a.rect.right <= 1:
                        marcador +=100
                        if marcador%500==0:
                            nivel += 1
                self.kill()




    def conectar():
    
        try:

            con = sqlite3.connect('p_max.db')

            return con

        except Error:

            print(Error)



    def añadir(con):

        cObj = con.cursor()

        cObj.execute("CREATE TABLE IF NOT EXISTS scores (puntos integer PRIMARY KEY)")

        con.commit()    

    con = conectar()



    añadir(con)
# Definimos las constantes de la altura y la anchura 
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    
    # Inicializamos el juego


    pygame.init()


    def leer(conexion):
        sql = "SELECT * FROM scores;"
        p = 0

        cursor = conexion.cursor()
        cursor.execute(sql)
        puntuacion = cursor.fetchall()
        list(puntuacion)

        for i in puntuacion:
            p = i[0]
        return p

    max_punt = leer (con)


#Añadimos la musica al juego
    pygame.mixer.music.load("resources/Apoxode_-_Electric_1.wav")
    pygame.mixer.music.play(loops=-1)


    dianoche = True
    colorpantalla = AZUL
    

    operaciondif = 100 + (450 - 50 * nivel)


    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a custom event for adding a new enemy
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, operaciondif)
   

    # Añadimos las nubes al juego
    ADDCLOUD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCLOUD, 1000)

    #Creamos un evento para que cambia de dia a noche
    DiaNoche = pygame.USEREVENT + 3
    pygame.time.set_timer(DiaNoche, 8000)
    
    #Creamos el evento para que salga el objeto por 
    ADDITEM = pygame.USEREVENT + 4
    pygame.time.set_timer(ADDITEM, 10000)

    # Instantiate player. Right now, this is just a rectangle.
    player = Player()

    
    # Create groups to hold enemy sprites and all sprites
    # - enemies is used for collision detection and position updates
    # - all_sprites is used for rendering
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    items = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Variable to keep the main loop running
   
    running = True
    continuar = True
    final = True

# Creamos la variable clock para inicializarla
    clock = pygame.time.Clock()
    
    #Bucle que contiene la pantalla de inicio
    while continuar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill((0, 0, 0))

        fuente = pygame.font.Font(None, 30)
        bienvenido = fuente.render("Bienvenido a JuegoAvion", 1, (255,0,0))
        screen.blit (bienvenido,(273, 250))

        
        p = fuente.render("Pulsa P para empezar", 1, (255,0,0))
        screen.blit(p,(290, 300))

       
        ranking = fuente.render("Record: " +str (max_punt), 1, (255,0,0))
        screen.blit(ranking,(20, 30))
        
        boton = pygame.key.get_pressed()

        if boton[pygame.K_p]:
            continuar = False
        pygame.display.update()

    #Bucle del juego
    while running:
        
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

            elif event.type == DiaNoche:
                #Añadimos la nuve al grupo de sprite
                if dianoche == True:
                    colorpantalla = NEGRO
                    dianoche = False
                else:
                    colorpantalla = AZUL
                    dianoche = True

            elif event.type == ADDITEM:
                #Añadimos la nuve al grupo de sprite
                new_item = item()
                items.add(new_item)
                all_sprites.add(new_item)
            
       
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

        #Actualizamos el item

        items.update()


        player.update(pressed_keys)

        # Ponemos el fondo azul
        screen.fill((colorpantalla))
       

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

        #Cuando player colisione con un item se elimina item
        if pygame.sprite.spritecollide(player, items, True):

            for i in enemies:
                i.kill()

        fuente = pygame.font.Font(None, 30)
        mensaje = fuente.render("Marcador: " +str(marcador),1, (255,0,0))
        screen.blit(mensaje, (15, 10))

        fuente = pygame.font.Font(None, 30)
        mensaje2 = fuente.render("Nivel: " +str(nivel),1, (255,0,0))
        screen.blit(mensaje2, (15, 30))

        pygame.display.flip()
    
        #Configuramos el reloj a 50
        clock.tick(50)
    #Bucle para la pantalla del final
    while final:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill((0, 0, 0))

        fuente = pygame.font.Font(None, 30)
        perdido = fuente.render("Has perdido, bien jugado!", 1, (255,0,0))
        screen.blit (perdido,(273, 250))

        
        q = fuente.render("Pulsa Q para salir", 1, (255,0,0))
        screen.blit(q,(290, 300))

       
        puntuacion = fuente.render("Marcador: " +str(marcador),1, (255,0,0))
        screen.blit(puntuacion,(20, 30))
        #Nos dice si hemos hecho record
        if marcador < max_punt:
            record = fuente.render ("Enhorabuena, nuevo record! ",1, (0,0,0))
            screen.blit(record, (290, 320))

        
        boton2 = pygame.key.get_pressed()

        
        if boton2[pygame.K_q]:
            final = False
        pygame.display.update()

        


    pygame.mixer.music.stop()

    pygame.mixer.quit()

    if (marcador > max_punt):

        try:
            sqliteCon= sqlite3.connect('p_max.db')
            cursor = sqliteCon.cursor()
            print("Connected to SQLite")

            sqlite_insert_with_param = """INSERT INTO scores
                                (puntos) 
                                VALUES (?);"""

            data_tuple = (marcador, )
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteCon.commit()
            print("Variables insertadas con éxito (puntos)")

            cursor.close()

        except sqlite3.Error as error:
            print("Error al importar las tablas", error)
        finally:
            if sqliteCon:
                sqliteCon.close()
                print("Conexión con SQLite finalizada")
            
