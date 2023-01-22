import pygame
import api_caller
from datetime import datetime

WIDTH = 960
HEIGHT = 960
DARK_MODE = True
PRIMARY_BACKGROUND = (118, 204, 185)
SECONDARY_BACKGROUND = (255, 225, 107)
PRIMARY_COLOR = (230, 255, 235)
SECONDARY_COLOR = (22, 18, 63)

def get_current_temperature(temperature):
    current_time = datetime.now()
    hour = current_time.hour
    if current_time.minute >= 30:
        hour += 1
    return temperature[hour]

#Get api
weather = api_caller.get_weather()
temperature = weather['temperature']
min_temperature = weather['min_temperature']
max_temperature = weather['max_temperature']
min_temperature_text = f'Min Temperature: {min_temperature}'
max_temperature_text = f'Max Temperature: {max_temperature}'
temperature_text = f'Current Temperature: {get_current_temperature(temperature)}'

def main():
    #Init pygame
    pygame.init()
    #pygame logo
    logo = pygame.image.load('images/logo.png')
    pygame.display.set_icon(logo)
    #pygame title
    pygame.display.set_caption('Weather Forecast')
    #create screen for pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    #is the program running or not
    running = True
    draw(screen)
    while running:
        #if user click the close button then stop the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

def draw(screen):
    if DARK_MODE:
        global PRIMARY_BACKGROUND
        PRIMARY_BACKGROUND = (30, 51, 46)
        global SECONDARY_BACKGROUND
        SECONDARY_BACKGROUND = (102, 90, 42)
        global PRIMARY_COLOR
        PRIMARY_COLOR = (62, 69, 64)
        global SECONDARY_COLOR
        SECONDARY_COLOR = (67, 55, 191)
    screen.fill(PRIMARY_BACKGROUND)
    draw_text(screen, min_temperature_text, 200, 0, PRIMARY_COLOR, None, 32)
    draw_text(screen, max_temperature_text, 200, 100, PRIMARY_COLOR, None, 32)
    draw_text(screen, temperature_text, 200, 200, PRIMARY_COLOR, None, 32)

def draw_text(screen, text, x, y, color, background, fontsize):
    font = pygame.font.SysFont(None, fontsize)
    text = font.render(text, True, color, background)
    screen.blit(text, (x, y))

if __name__ == "__main__":
    main()
