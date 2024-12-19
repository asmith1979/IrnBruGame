# Script: main.py
# Author: Andrew Smith
# Date: June 2022
# Description: Experimentation project

import pygame

# Screen size settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Background image position values
backimg_x = 0
backimg_y = 0

animation_increment=10
clock_tick_rate=20

pygame.init()

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
grassfloor_img = pygame.transform.scale(grassfloor_img, (100,100))
floorlight_img = pygame.transform.scale(floorlight_img, (100,100))

# Load in texture for concrete floor 
concretefloor_img = pygame.image.load("images/concretefloor.jpg").convert()

# Scale down the concrete floor image 
concretefloor_img = pygame.transform.scale(concretefloor_img, (100,100))


# Load the Bridge image 
bridge_img = pygame.image.load("images/bridgefloor.jpg").convert()

# Scale down the bridge image 
bridge_img = pygame.transform.scale(bridge_img, (100,100))



pygame.display.set_caption("Test Project001")

dead=False

clock = pygame.time.Clock()

# Function: create_grid
# Description: This function is going to be used to create the grid 
def create_grid(posxin, posyin, widthin, heightin):
    global grassfloor_img 
    global floorlight_img
    
    griddata = [] # Stores all grid data
    
    # Calculate actual width
    widthtotal = ((widthin) * grassfloor_img.get_width()) # 100 px
    heighttotal = ((heightin+1) * grassfloor_img.get_height()) # 100 px 
    
    startposx = posxin

    while posyin < heighttotal:        
        while posxin < widthtotal:
            # Store first grid square 
            griddata.append(pygame.Rect(posxin,posyin,(widthin*grassfloor_img.get_width()),(heightin*grassfloor_img.get_height())))
            posxin = posxin + grassfloor_img.get_width()
        griddata.append(pygame.Rect(posxin,posyin,(widthin*grassfloor_img.get_width()),(heightin*grassfloor_img.get_height())))
        posyin = posyin + grassfloor_img.get_height()        
        posxin = startposx
        # Store first grid square 
        
        
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


    
# Create room 1
room1data = create_grid(100,100,10,10)



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

    
    # draw_grid(100,100,10,10, screen)
    
    # screen.blit(grassfloor_img, (100,100))
    
    # Output graphics to the screen (Island one)
    '''
    screen.blit(concretefloor_img, (100,400))
    screen.blit(concretefloor_img, (100,500))
    screen.blit(concretefloor_img, (100,600))
    
    screen.blit(concretefloor_img, (100,700))
    screen.blit(concretefloor_img, (200,700))
    screen.blit(concretefloor_img, (300,700))
    
    screen.blit(concretefloor_img, (100,300))
    screen.blit(concretefloor_img, (200,300))
    screen.blit(concretefloor_img, (300,300))
    '''
    
    draw_grid(room1data,screen)
    screen.blit(gameCharacter_img, (200,200))
        
        
    #screen.blit(grassfloor_img, (200,500))
    #screen.blit(grassfloor_img, (300,400))
    #screen.blit(grassfloor_img, (300,500))
    #screen.blit(grassfloor_img, (200,600))
    #screen.blit(grassfloor_img, (300,600))
    
    # Output the bridge for the island
    # screen.blit(bridge_img, (400,500))
    
    
    
    
    pygame.display.flip()
    clock.tick(clock_tick_rate)
pygame.quit()



