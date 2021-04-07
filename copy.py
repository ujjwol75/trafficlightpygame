import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800, 300))
rect_width = 40
rect_height = 150
color = (0, 0, 0)
bus_x = 690
bus_y = 211
bus_vel_x = -3
#vertical line variables
zebraline_x = 150
zebraline_y = 200
#road 
road_x = 0
road_y = 225
#stand variables
stand_width = 10
stand_height = 68

FPS = 80
#color variables
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
#horizontal line variables(for road)
first_hr_lineX1 = 0
first_hr_lineY1 = 235
first_hr_lineX2 = 800
first_hr_lineY2 = 235

second_hr_lineX1 = 0
second_hr_lineY1 = 290
second_hr_lineX2 = 800
second_hr_lineY2 = 290

def trafficLightStand():
    light_stand = pygame.draw.rect(screen, (0,191,255), (26, 170, stand_width, stand_height))


def draw_road():
    roadimg = pygame.image.load("road.jpg")
    roadimg = pygame.transform.scale(roadimg, (800, 70))
    screen.blit(roadimg, (road_x, road_y))

# draw a traffic light rectangle
def rectangle(color):
    rec = pygame.draw.rect(screen, color, (10, 20, rect_width, rect_height))


# draw a traffic light color (circle)
def draw_first_circle(color):
    cir = pygame.draw.circle(screen, color, (30, 50), 18)


def draw_second_circle(color):
    cir = pygame.draw.circle(screen, color, (30, 95), 18)


def draw_third_circle(color):
    cir = pygame.draw.circle(screen, color, (30, 140), 18)


# load a bus image
def draw_bus(bus_x, bus_y):
    busimg = pygame.image.load("bus.png")
    busimg = pygame.transform.scale(busimg, (130, 120))
    screen.blit(busimg, (bus_x, bus_y))


# draw a white straight line
def draw_zebraCross():
    zebraCrossimg = pygame.image.load("zebracross.png")
    zebraCrossimg = pygame.transform.scale(zebraCrossimg, (90, 120))
    screen.blit(zebraCrossimg, (zebraline_x, zebraline_y))


def check_light_color(a, b, c):
    lights = [a, b, c]
    random_light = random.randrange(1, len(lights)+1)
    if random_light == 1:
        draw_first_circle(a)

    elif random_light == 2:
        draw_second_circle(b)

    else:
        draw_third_circle(c)
    return random_light


# main game loop
game = True
running = True
while game == True:
    fpsClock = pygame.time.Clock()
    
    bus_x = bus_x + bus_vel_x

    screen.fill((0, 0, 0))

    rectangle((255, 255, 255))
    trafficLightStand()
    draw_first_circle(color)
    draw_second_circle(color)
    draw_third_circle(color)
    draw_road()
    draw_zebraCross()
    draw_bus(bus_x, bus_y)

    mid_line = int(zebraline_x + zebraline_y)/2
    if abs(bus_x - mid_line) < 70:
        while running == True:
            temp = check_light_color((255, 0, 0), (0, 255, 0), (255, 255, 0))
            print(temp)
            if temp == 1:
                bus_vel_x = 0
                bus_x += bus_vel_x

            elif temp == 2:
                bus_vel_x = -3
                bus_x += bus_vel_x
            else:
                bus_vel_x = 0
                bus_x += bus_vel_x

            running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            
                

     # check if bus is near to line
    # check_bus()

    
    # draw_hrLines()
   
    pygame.display.update()
    fpsClock.tick(FPS)
