import pygame

class item:
    def __init__(self, tilesize, color):
        self.item = [[5,7]]
        self.tilesize = tilesize
        self.color = color
        self.offsetX = 0
        self.offsetY = 0
        
        
    def draw(self, screen):
        for elt in self.item:
            pygame.draw.polygon(screen,self.color,((elt[0]*self.tilesize + (self.tilesize/2), elt[1]*self.tilesize), (elt[0]*self.tilesize, elt[1]*self.tilesize  + (self.tilesize/2)), (elt[0]*self.tilesize + (self.tilesize/2), elt[1]*self.tilesize  + self.tilesize),  (elt[0]*self.tilesize + self.tilesize, elt[1]*self.tilesize + (self.tilesize/2))) )


    def get_item(self, player_x, player_y):
        for elt in self.item:
            if (player_x, player_y) == (elt[0], elt[1]):
                self.item.remove(elt)
                return True
        return False
    
    def change_origin(self, X, Y):
        self.offsetX = X
        self.offsetY = Y
