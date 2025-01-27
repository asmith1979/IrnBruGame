# Script: main.py
# Author: Andrew Smith
# Date: December 2024
# Description: Irn-Bru and Caramel Wafer project

import pygame
import pygame.freetype

# Initialise PyGame
pygame.init()

# Background image position values
backimg_x = 0
backimg_y = 0

# animation_increment=10
clock_tick_rate=20

# getScreenMode 
# This function will set the screen mode 2 modes below the current one
# for screen size convenience / compatibility
def getScreenMode():
    
    # Get all available screen modes 
    available_screen_modes = pygame.display.list_modes()
    
    # Get current display setup
    current_display_mode = pygame.display.Info()
    
    # Set a default screen mode until determination is reached
    selectedScreenMode = available_screen_modes[1]
    
    # Set index counter
    indexCounter = 0
    
    # Set index value 
    indexValue = 0
    
    # Search for screen mode currently selected by default
    for screen_mode in available_screen_modes:
        widthValue = screen_mode[0]
        heightValue = screen_mode[1]
        
        # If found, get the index value of the screen setting which is found 
        if widthValue == current_display_mode.current_w and heightValue == current_display_mode.current_h:
            indexValue = indexCounter 
            
        indexCounter = indexCounter + 1        
   
    # Get how long the list of available screen modes is 
    screenModeListLength = len(available_screen_modes)
    
    # Formula to calculate 
    if (indexValue+2) <= (screenModeListLength-1):
        selectedScreenMode = available_screen_modes[indexValue+2]
        
    return selectedScreenMode

# Set and get screen mode 
screenMode = getScreenMode()
screen = pygame.display.set_mode(screenMode)

# Get centre of screen values 
screenX = (screen.get_width() / 2) - 300
screenY = (screen.get_height() / 2) - 300

player_x_pos = 300
player_y_pos = 300

# Load a font to use for the game 
GAME_FONT = pygame.freetype.Font("font/typewriter.ttf", 72)

transcolour = (0,255,33)

# Irn Bru can object
irnBruObj_img = pygame.image.load("images/irnbruobj.png").convert()

# Basic direction images (Front,back,left,right)
characterFront_img = pygame.image.load("images/charfront.png").convert()
characterBack_img = pygame.image.load("images/charback.png").convert()
characterLeft_img = pygame.image.load("images/charleft.png").convert()
characterRight_img = pygame.image.load("images/charright.png").convert()

# Front walking images 
characterFront01_img = pygame.image.load("images/charfront01.png").convert()
characterFront02_img = pygame.image.load("images/charfront02.png").convert()

# Back walking images 
characterBack01_img = pygame.image.load("images/charback01.png").convert()
characterBack02_img = pygame.image.load("images/charback02.png").convert()

# Left walking images 
characterLeft01_img = pygame.image.load("images/charleft01.png").convert()
characterLeft02_img = pygame.image.load("images/charleft02.png").convert()

# Right walking images
characterRight01_img = pygame.image.load("images/charright01.png").convert()
characterRight02_img = pygame.image.load("images/charright02.png").convert()

screen.set_colorkey(transcolour)
characterFront_img.set_colorkey(transcolour)
characterBack_img.set_colorkey(transcolour)
characterLeft_img.set_colorkey(transcolour)
characterRight_img.set_colorkey(transcolour)
characterFront01_img.set_colorkey(transcolour)
characterFront02_img.set_colorkey(transcolour)
characterBack01_img.set_colorkey(transcolour)
characterBack02_img.set_colorkey(transcolour)
characterLeft01_img.set_colorkey(transcolour)
characterLeft02_img.set_colorkey(transcolour)
characterRight01_img.set_colorkey(transcolour)
characterRight02_img.set_colorkey(transcolour)

irnBruObj_img.set_colorkey(transcolour)

# Load the Game Grid image
game_grid = pygame.image.load("images/gamegrid.jpg").convert()

# Load Irn-Bru can image 
irnBruCan = pygame.image.load("images/irnbrucan.png").convert()
irnBruCan.set_colorkey(transcolour)

# Load Wafer image 
wafer_img = pygame.image.load("images/wafer_img.jpg").convert()

wafer_obj = wafer_img 

wafer_obj = pygame.transform.scale(wafer_obj, (50,25))

# Background image 
background_img = pygame.image.load("images/background_img.jpg").convert()

# Scale down the grass floor image 
characterFront_img = pygame.transform.scale(characterFront_img, (50,50))
characterBack_img = pygame.transform.scale(characterBack_img, (50,50))
characterLeft_img = pygame.transform.scale(characterLeft_img, (50,50))
characterRight_img = pygame.transform.scale(characterRight_img, (50,50))
characterFront01_img = pygame.transform.scale(characterFront01_img, (50,50))
characterFront02_img = pygame.transform.scale(characterFront02_img, (50,50))
characterBack01_img = pygame.transform.scale(characterBack01_img, (50,50))
characterBack02_img = pygame.transform.scale(characterBack02_img, (50,50))
characterLeft01_img = pygame.transform.scale(characterLeft01_img, (50,50))
characterLeft02_img = pygame.transform.scale(characterLeft02_img, (50,50))
characterRight01_img = pygame.transform.scale(characterRight01_img, (50,50))
characterRight02_img = pygame.transform.scale(characterRight02_img, (50,50))

irnBruObj_img = pygame.transform.scale(irnBruObj_img, (30,50))

background_img = pygame.transform.scale(background_img, screenMode)

pygame.display.set_caption("Irn-Bru Project")

dead=False

clock = pygame.time.Clock()

def setGameWorld():
    global room1data
    
    # Set L block square 
    room1data[21][1] = 1
    room1data[31][1] = 1
    room1data[41][1] = 1
    room1data[42][1] = 1
    room1data[43][1] = 1
    
    # Set 2nd block square 
    room1data[46][1] = 1
    room1data[47][1] = 1
    room1data[48][1] = 1
    room1data[58][1] = 1
    room1data[68][1] = 1
    
    # Create Rectangle square block 
    room1data[63][1] = 1
    room1data[73][1] = 1
    room1data[64][1] = 1
    room1data[74][1] = 1
    room1data[65][1] = 1
    room1data[75][1] = 1


# Function: draw_grid
# Description: This function is used to draw a grid (room) at
#               a specified position and width and height
def draw_grid(gridDataIn, screenIn):
    # Include the texture    
    global standard_GridSquare_img
    global sandfloor_img
    global shrub_img
    
    for gridTile in gridDataIn:
        if gridTile[1] == 0:
            screenIn.blit(sandfloor_img, gridTile[0])
        if gridTile[1] == 1:
            screenIn.blit(shrub_img, gridTile[0])

    
screen.blit(background_img, (0,0))
screen.blit(game_grid, (100,100))
screen.blit(irnBruCan, (1200, 100))
screen.blit(wafer_img, (1450, 150))
screen.blit(characterFront_img, (player_x_pos,player_y_pos))
directionIndicator = 0 # Front facing (down direction)

# Animation stages
leftStage = 0
rightStage = 0
upStage = 0
downStage = 0

player_speed = 8

irnbruobj_x_pos = 500
irnbruobj_y_pos = 500
canActive = True

waferobj_x_pos = 600
waferobj_y_pos = 600

irnBruScore = 0
waferScore = 0

while(dead==False):    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
            
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            # Check to see if the Escape key has been pressed (exit's the game program)
            if event.key == pygame.K_ESCAPE:
                dead = True
                
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_x_pos = player_x_pos + player_speed
        rightStage = rightStage + 1
        directionIndicator = 2
        
    if keys[pygame.K_LEFT]:
        player_x_pos = player_x_pos - player_speed
        leftStage = leftStage + 1
        directionIndicator = 3
        
    if keys[pygame.K_UP]:
        player_y_pos = player_y_pos - player_speed
        upStage = upStage + 1
        directionIndicator = 1
        
    if keys[pygame.K_DOWN]:
         player_y_pos = player_y_pos + player_speed
         downStage = downStage + 1
         directionIndicator = 0

    screen.blit(background_img, (0,0))
    screen.blit(game_grid, (100,100))   
    screen.blit(irnBruCan, (1200, 100))
    screen.blit(wafer_img, (1450, 150))
    
    text_surface, rect = GAME_FONT.render(str(irnBruScore), (0, 255, 33))
    screen.blit(text_surface, (1350, 150))
    
    waferscore, rect = GAME_FONT.render(str(waferScore), (0,255,33))
    screen.blit(waferscore, (1850,150))
    
    timelimit, rect = GAME_FONT.render("TIME - ", (0,255,33))
    screen.blit(timelimit, (600,25))
    
    timelimitvalue, rect = GAME_FONT.render("0:00", (0,255,33))
    screen.blit(timelimitvalue, (900,25))
    
    # Output objects on game grid 
    if canActive == True:
        screen.blit(irnBruObj_img, (irnbruobj_x_pos,irnbruobj_y_pos))
    
    screen.blit(wafer_obj, (waferobj_x_pos,waferobj_y_pos))  

    if player_x_pos >= irnbruobj_x_pos and player_x_pos <= (irnbruobj_x_pos+30) and player_y_pos >= irnbruobj_y_pos and player_y_pos <= (irnbruobj_y_pos+50) and canActive == True:
        irnBruScore = irnBruScore + 2
        canActive = False 
    
    
    if directionIndicator == 0: # Travelling Down
        if downStage == 0:
            screen.blit(characterFront01_img, (player_x_pos,player_y_pos))
            pygame.time.delay(50)
            
        if downStage == 1:
            screen.blit(characterFront_img, (player_x_pos,player_y_pos))
            pygame.time.delay(50)
            
        if downStage == 2:
            screen.blit(characterFront02_img, (player_x_pos, player_y_pos))
            downStage = 0
            pygame.time.delay(50)
            
        
        
    if directionIndicator == 1: # Travelling Up
        if upStage == 0:
            screen.blit(characterBack01_img, (player_x_pos,player_y_pos))
            pygame.time.delay(50)
            
        if upStage == 1:
            screen.blit(characterBack_img, (player_x_pos,player_y_pos))
            pygame.time.delay(50)
            
        if upStage == 2:
            screen.blit(characterBack02_img, (player_x_pos,player_y_pos))
            upStage = 0
            pygame.time.delay(50)
        
    if directionIndicator == 2: # Travelling Right 
        if rightStage == 0:
            screen.blit(characterRight01_img, (player_x_pos,player_y_pos))
            pygame.time.delay(50)
            
        if rightStage == 1:
            screen.blit(characterRight_img, (player_x_pos,player_y_pos))
            pygame.time.delay(50)
            
        if rightStage == 2:
            screen.blit(characterRight02_img, (player_x_pos,player_y_pos))
            rightStage = 0
            pygame.time.delay(50)
        
    if directionIndicator == 3: # Travelling Left
        if leftStage == 0:
            screen.blit(characterLeft01_img, (player_x_pos,player_y_pos))
            pygame.time.delay(50)
            
        if leftStage == 1:
            screen.blit(characterLeft_img, (player_x_pos,player_y_pos))
            pygame.time.delay(50)
            
        if leftStage == 2:
            screen.blit(characterLeft02_img, (player_x_pos,player_y_pos))
            leftStage = 0
            pygame.time.delay(50)
    

    pygame.display.flip()
    clock.tick(clock_tick_rate)
pygame.quit()



