# Script: main.py
# Author: Andrew Smith
# Date: December 2024
# Description: Irn-Bru and Caramel Wafer project

import pygame

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

# RGB
# 0, 163, 232

# Set background colour of water
background_colour = (0, 163, 232)

# Load game character
gameCharacter_img = pygame.image.load("images/character.jpg").convert()

# Grass floor image 
standard_GridSquare_img = pygame.image.load("images/floortile01.jpg").convert()
block_GridSquare_img = pygame.image.load("images/wall01.jpg").convert()

sandfloor_img = pygame.image.load("images/sand_img.jpg").convert()
shrub_img = pygame.image.load("images/shrub_img.jpg").convert()

# Load Irn-Bru can image 
irnBruCan = pygame.image.load("images/irnbrucan.jpg").convert()

# Load Wafer image 
wafer_img = pygame.image.load("images/wafer_img.jpg").convert()

# Background image 
background_img = pygame.image.load("images/background_img.jpg").convert()

floorlight_img = pygame.image.load("images/floortile01b.jpg").convert()

# Scale down the grass floor image 
standard_GridSquare_img = pygame.transform.scale(standard_GridSquare_img, (50,50))
block_GridSquare_img = pygame.transform.scale(block_GridSquare_img, (100,100))
# shrub_img = pygame.transform.scale(shrub_img, (50,50))
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
    
    
    

# Function: create_grid
# Description: This function is going to be used to create the grid 
def create_grid(posxin, posyin, widthin, heightin):
    global standard_GridSquare_img 
    global sandfloor_img
    
    griddata = [] # Stores all grid data
    
    # Get start position to start creating GridSquare objects (horizontal)
    startposx = posxin
    
    # Get start position to start creating GridSquare objects (vertical)
    startposy = posyin
    
    # Set increment value for hotizontal placing...
    horizIncrementValue = sandfloor_img.get_width()
    
    # Set vertical increment value 
    vertIncrementValue = sandfloor_img.get_height()

    # Algothithm to create gaming grid 
    xCounter = 0
    yCounter = 0
    while yCounter < heightin:
        while xCounter < widthin:
            griddata.append([pygame.Rect(startposx,startposy,(widthin*sandfloor_img.get_width()),(heightin*sandfloor_img.get_height())),0])
            startposx = (startposx+horizIncrementValue)
            xCounter = xCounter + 1
        # Reset values
        xCounter = 0
        startposx = posxin 
    
        startposy = (startposy+vertIncrementValue)
        yCounter = yCounter + 1

    return griddata
    
    
    
    

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

    
# Create Game Grid
room1data = create_grid(100,100,10,10)
# Setup game grid
setGameWorld()
print(screenX)
print(screenY)
print(len(room1data))


while(dead==False):
    # Fill screen with the background colour 
    screen.fill(background_colour)    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
            
        if event.type == pygame.KEYDOWN:
            # Check to see if the Escape key has been pressed
            if event.key == pygame.K_ESCAPE:
                dead = True

    

    
    screen.blit(background_img, (0,0))
    draw_grid(room1data,screen)    
    screen.blit(irnBruCan, (1200, 100))
    screen.blit(wafer_img, (1450, 150))
    

    pygame.display.flip()
    clock.tick(clock_tick_rate)
pygame.quit()



