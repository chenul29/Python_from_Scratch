import math
import random
import time
import pygame
pygame.init()

width, height = 800, 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aim Game")

class target:
    max_size = 30
    growth_rate = 0.2
    color = "red"
    second_color = "white"

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.growth_rate >= self.max_size:
            self.grow = False
        
        if self.grow:
            self.size += self.growth_rate
        else:
            self.size -+ self.growth_rate
    
    def draw(self, win):
        pygame.draw.circle(window,self.color, (self.x, self.y), self.size)
        pygame.draw.circle(window,self.second_color, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(window,self.color, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(window,self.second_color, (self.x, self.y), self.size * 0.4)

def main():
    run = True 

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()

if __name__ == "__main__":
    main()