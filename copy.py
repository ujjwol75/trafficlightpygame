import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 300))
rect_width = 70
rect_height = 200
color = (255, 255, 255)
bus_x = 690
bus_y = 80
bus_vel_x = -16

def rectangle():
    rec = pygame.draw.rect(screen, (200,200,200), (20, 20, rect_width, rect_height))


def draw_first_circle():
    cir = pygame.draw.circle(screen, color, (55, 55), 25)


def draw_second_circle():
    cir = pygame.draw.circle(screen, color, (55, 110), 25)


def draw_third_circle():
    cir = pygame.draw.circle(screen, color, (55, 165), 25)


def draw_bus(bus_x, bus_y):
    busimg = pygame.image.load("bus.png")
    busimg = pygame.transform.scale(busimg, (100, 100))
    screen.blit(busimg, (bus_x,bus_y))
        
# def move_bus(bus_x):
#     vel_x = -5
#     bus_x = bus_x + vel_x
    

def draw_line():  
    line = pygame.draw.line(screen, (255,255,255), (240,20), (240, 220), 6)
    

game = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                bus_x = bus_x + bus_vel_x
                screen.fill((0,0,0))
                draw_bus(bus_x, bus_y)
                
    

    rectangle()
    draw_first_circle()
    draw_second_circle()
    draw_third_circle()
    draw_line()
    # move_bus(bus_x)
    
    pygame.display.update()
        

