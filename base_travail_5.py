# Example file showing a circle moving on screen
import pygame 
import random
from labyrinthe import Labyrinthe
from grid import Grid
from utils import Pos
from read_colors import read_color_parameters

# pygame setup
pygame.init()

#constantes
tilesize = 32 # taille d'une tuile IG
size = (15, 20) # taille du monde
fps = 30 # fps du jeu
player_speed = 300 # vitesse du joueur
next_move = 0 #tic avant déplacement
score = 0
font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 50)

# color
read = read_color_parameters()
read.readColors("color.ini")
color = read.c

level = "data/laby-01.dat"

laby = Labyrinthe(size[0], size[1])
laby.load_from_file(level)
laby.set_color(color["wall_color"])

grid = Grid(size[1], size[1],tilesize)
grid.set_color(color["grid_color"])

screen = pygame.display.set_mode((size[0]*tilesize, size[1]*tilesize))
clock = pygame.time.Clock()
running = True
dt = 0

show_grid = True
show_pos = False

keys= { "UP":0 , "DOWN":0, "LEFT":0, "RIGHT":0 }

player_pos = Pos(7,7)
direction_player = (0, 0)

#tour de boucle, pour chaque FPS
while running:

    #
    #   Gestion des I/O  
    #
    
    #   lecture clavier / souris
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                direction_player = (0, -1)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                direction_player = (0, 1)
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                direction_player = (-1, 0)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                direction_player = (1, 0)


            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_g:
                show_grid = not show_grid
            if event.key == pygame.K_p:
                show_pos = not show_pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print("mouse_pos:", pos)

    #
    # gestion des déplacements
    #

    next_move += dt
    if next_move> 1000 / fps:
        new_x, new_y = player_pos.x, player_pos.y
        if direction_player == (0, -1):
            new_y -=1
        elif direction_player == (0, 1):
            new_y += 1
        elif direction_player == (-1, 0):
            new_x -=1
        elif direction_player == (1, 0):
            new_x += 1

        # vérification du déplacement du joueur                                    
        if not laby.hit_box(new_x, new_y):
            player_pos.x, player_pos.y = new_x, new_y
            next_move -= player_speed

        if show_pos:
            print("pos: ",player_pos)

    #
    # affichage des différents composants graphique
    #
    screen.fill(color["ground_color"])

    laby.draw(screen, tilesize)

    if show_grid:
        grid.draw(screen)

    # Dessiner le joueur (cercle)
    player_radius = tilesize // 2  # Le rayon du cercle est la moitié de la taille d'une tuile
    player_center = (player_pos.x * tilesize + player_radius, player_pos.y * tilesize + player_radius)
    pygame.draw.circle(screen, color["player_color"], player_center, player_radius)

    # affichage des modification du screen_view
    pygame.display.flip()
    # gestion fps
    dt = clock.tick(fps)

pygame.quit()