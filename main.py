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
screen = pygame.display.set_mode(getScreenMode())

screenX = (screen.get_width() / 2) - 300
screenY = (screen.get_height() / 2) - 300

# RGB
# 0, 163, 232

# Set background colour of water
background_colour = (0, 163, 232)

# Load game character
gameCharacter_img = pygame.image.load("images/character.jpg").convert()

# Grass floor image 
grassfloor_img = pygame.image.load("images/floortile01.jpg").convert()
floorlight_img = pygame.image.load("images/floortile01b.jpg").convert()

# Scale down the grass floor image 
grassfloor_img = pygame.transform.scale(grassfloor_img, (50,50))
floorlight_img = pygame.transform.scale(floorlight_img, (50,50))

# Load in texture for concrete floor 
concretefloor_img = pygame.image.load("images/concretefloor.jpg").convert()

# Scale down the concrete floor image 
concretefloor_img = pygame.transform.scale(concretefloor_img, (50,50))

pygame.display.set_caption("Irn-Bru Project")

dead=False

clock = pygame.time.Clock()

# Function: create_grid
# Description: This function is going to be used to create the grid 
def create_grid(posxin, posyin, widthin, heightin):
    global grassfloor_img 
    
    griddata = [] # Stores all grid data
    
    # Get start position to start creating GridSquare objects (horizontal)
    startposx = posxin
    
    # Get start position to start creating GridSquare objects (vertical)
    startposy = posyin
    
    # Set increment value for hotizontal placing...
    horizIncrementValue = grassfloor_img.get_width()
    
    # Set vertical increment value 
    vertIncrementValue = grassfloor_img.get_height()

    # Algothithm to create gaming grid 
    xCounter = 0
    yCounter = 0
    while yCounter < heightin:
        while xCounter < widthin:
            griddata.append(pygame.Rect(startposx,startposy,(widthin*grassfloor_img.get_width()),(heightin*grassfloor_img.get_height())))
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
    global grassfloor_img
    global floorlight_img
    
    for gridTile in gridDataIn:
        screenIn.blit(grassfloor_img, gridTile)


    
# Create Game Grid
room1data = create_grid(screenX,screenY,10,10)
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

    

    
    draw_grid(room1data,screen)
    # screen.blit(gameCharacter_img, (200,200))

    
    
    
    pygame.display.flip()
    clock.tick(clock_tick_rate)
pygame.quit()



