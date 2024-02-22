import pygame
import random

class ghost:
    def __init__(self, tilesize, color):
        self.pos = [[10,10]]
        self.tilesize = tilesize
        self.color = color
        self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.offsetX = 0
        self.offsetY = 0
        
        
    def draw(self, screen):
        for elt in self.pos:
            pygame.draw.circle(screen, self.color, [elt[0] * self.tilesize + self.tilesize // 2 + self.offsetX, elt[1] * self.tilesize + self.tilesize // 2 + self.offsetY], 15)
            
    def update_position(self, laby):
        new_x, new_y = self.pos[0][0], self.pos[0][1]

        if self.direction == 'UP':
            new_y -= 1
        elif self.direction == 'DOWN':
            new_y += 1
        elif self.direction == 'LEFT':
            new_x -= 1
        elif self.direction == 'RIGHT':
            new_x += 1


        # Check for collision with walls
        if not laby.hit_box(new_x, new_y):
            self.pos[0][0], self.pos[0][1] = new_x, new_y
        # elif not laby.hit_water(new_x, new_y):
        #     self.pos[0][0], self.pos[0][1] = new_x, new_y
        else:
            # Change direction if colliding with a wall
            self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
            
        
            
    def check_collision_with_player(self, player_pos):
        alien_rect = pygame.Rect(self.pos[0][0] * self.tilesize, self.pos[0][1] * self.tilesize, self.tilesize, self.tilesize)
        player_rect = pygame.Rect(player_pos.x * self.tilesize, player_pos.y * self.tilesize, self.tilesize, self.tilesize)

        if alien_rect.colliderect(player_rect):
            print("Touché!")
            # Handle collision with player
            self.direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
            
    def change_origin(self, X, Y):
        self.offsetX = X
        self.offsetY = Y