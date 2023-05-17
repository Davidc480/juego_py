import pygame

def draw_player(screen, player_x, player_y):
    player_color = (255, 0, 0)  # Color rojo para el personaje
    player_rect = pygame.Rect(player_x, player_y, 50, 50)  # Rectángulo que representa al personaje
    pygame.draw.rect(screen, player_color, player_rect)

def draw_enemies(screen):
    enemy_color = (0, 0, 255)  # Color azul para los enemigos

    # Lista de coordenadas de los rectángulos de los enemigos
    enemy_rects = [
        pygame.Rect(200, 200, 50, 50),
        pygame.Rect(400, 300, 50, 50),
        pygame.Rect(600, 400, 50, 50)
    ]

    for enemy_rect in enemy_rects:
        pygame.draw.rect(screen, enemy_color, enemy_rect)

menu_color = (0, 255, 0)  # Color verde para el menú
selected_option = None

def select_option():
    global selected_option
    selected_option = "start"
    print("Opción seleccionada: start")

def check_collision(player_x, player_y):
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    enemy_rects = [
        pygame.Rect(200, 200, 50, 50),
        pygame.Rect(400, 300, 50, 50),
        pygame.Rect(600, 400, 50, 50)
    ]
    for enemy_rect in enemy_rects:
        if player_rect.colliderect(enemy_rect):
            return True
    return False

def end_game():
    pygame.time.delay(2000)
    pygame.quit()

def show_menu(screen):
    screen.fill((0, 0, 0))  # Limpiar la pantalla
    font = pygame.font.Font(None, 36)  # Fuente y tamaño del texto

    text_start = font.render("Start", True, (255, 255, 255))
    text_start_rect = text_start.get_rect(center=(400, 300))
    screen.blit(text_start, text_start_rect)

    pygame.display.flip()  # Actualizar la pantalla

def play():
    pygame.init()
    pygame.display.set_caption("play for kodland")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True
    player_x = 50
    player_y = 50
    game_over = False
    menu_active = True

    while running:
        if menu_active:
            show_menu(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if menu_active and event.key == pygame.K_RETURN:
                    select_option()
                    menu_active = False

                if not menu_active:
                    if event.key == pygame.K_UP:
                        player_y -= 10  # Mover hacia arriba
                    elif event.key == pygame.K_DOWN:
                        player_y += 10  # Mover hacia abajo
                    elif event.key == pygame.K_LEFT:
                        player_x -= 10  # Mover hacia la izquierda
                    elif event.key == pygame.K_RIGHT:
                        player_x += 10  # Mover hacia la derecha

        if not menu_active:
            screen.fill((0, 0, 0))  # Limpiar la pantalla antes de dibujar
            draw_player(screen, player_x, player_y)
            draw_enemies(screen)


        if check_collision(player_x, player_y):
            game_over = True
            print("Game over")
            end_game()

        pygame.display.flip()  # Actualizar la pantalla

    clock.tick(60)  # Limitar la velocidad de actualización a 60 FPS

pygame.quit()

play()