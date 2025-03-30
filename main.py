# Script: main.py
# Author: Andrew Smith
# Date: December 2024
# Description: Irn-Bru and Caramel Wafer project

import pygame
import pygame.freetype
from enum import Enum 

# Initialise PyGame
pygame.init()

# Set window title 
pygame.display.set_caption("Irn-Bru Project")

# Initialise clock 
clock = pygame.time.Clock()

##########################
## Game Data Structures ##
##########################

# Shrub wall 1 (L-Block)
shrubLBlock_01 = []
shrubLBlock_01.append([200,250])
shrubLBlock_01.append([250,250])
shrubLBlock_01.append([300,250])    
shrubLBlock_01.append([200,300])
shrubLBlock_01.append([200,350])

# Shrub wall 2 (6-block)
shrub6Block_02 = []    
shrub6Block_02.append([800,400])
shrub6Block_02.append([850,400])
shrub6Block_02.append([900,400])
shrub6Block_02.append([800,450])
shrub6Block_02.append([850,450])
shrub6Block_02.append([900,450])

# Shrub wall 3 (6-block)
shrub6Block_03 = []    
shrub6Block_03.append([300,650])
shrub6Block_03.append([350,650])
shrub6Block_03.append([400,650])
shrub6Block_03.append([300,700])
shrub6Block_03.append([350,700])
shrub6Block_03.append([400,700])

# Irn-Bru object structure 
irnBruObjStruct = []
irnBruObjStruct.append([500,500,True])
irnBruObjStruct.append([400,400,True])
irnBruObjStruct.append([200,700,True])
irnBruObjStruct.append([800,200,True])
irnBruObjStruct.append([700,775,True])
irnBruObjStruct.append([300,800,True])
irnBruObjStruct.append([300,950,True])
irnBruObjStruct.append([900,600,True])

# Wafer object structure 
waferObjStruct = []
waferObjStruct.append([600,600,True])
waferObjStruct.append([700,925,True])
waferObjStruct.append([400,800,True])
waferObjStruct.append([300,400,True])

# Enumeration for direction player is facing (to be implemented)
class Direction(Enum):
    DOWN_DIRECTION = 0
    UP_DIRECTION = 1
    RIGHT_DIRECTION = 2
    LEFT_DIRECTION = 3

######################
## Global variables ##
######################

# Player Position (x and y)
player_x_pos = 150
player_y_pos = 150
# Player Speed 
player_speed = 8
directionIndicator = 0 # (To be replaced with enum)

# Irn-Bru 
irnBruScore = 0
irnBruVertLength = 40 # 40 pixels (irn-bru object image)
irnBruHorizLength = 30 # 30 pixels (irb-bru object image)
irnBruObjCounter = 0

# Caramel Wafer 
waferScore = 0
waferObjCounter = 0

# Animation stages (used for sequencing of frames)
leftStage = 0
rightStage = 0
upStage = 0
downStage = 0

# Background image position values
backimg_x = 0
backimg_y = 0

# animation_increment=10
clock_tick_rate=20

# Load a font to use for the game 
GAME_FONT = pygame.freetype.Font("font/typewriter.ttf", 72)

# The colour to exclude when loading in sprite images 
transcolour = (0,255,33)

# Font and game timer settings 
counter, text = 59, '59'
pygame.time.set_timer(pygame.USEREVENT, 1000)

timerMinValue = 0
timesUp = False

dead=False # Used to terminate the game loop 

#############################
## Screen Resolution Setup ##
#############################

# getScreenMode 
# This function will set the screen mode 2 modes below the current one (Further improvement needed)
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

###################################
## Load Images used for the game ##
###################################

# Load information board 
information_board = pygame.image.load("images/infoboard.jpg").convert()

# Load shrub image 
shrub_img = pygame.image.load("images/shrub01_img.png").convert()

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

# Load the Game Grid image
game_grid = pygame.image.load("images/gamegrid.jpg").convert()

# Load Irn-Bru can image 
irnBruCan = pygame.image.load("images/irnbrucan.png").convert()

# Load Wafer image 
wafer_img = pygame.image.load("images/wafer_img.jpg").convert()

# Background image 
background_img = pygame.image.load("images/background_img.jpg").convert()

# Copy already loaded images to use for rescaling
waferInfo_img = wafer_img 
wafer_obj = wafer_img 
irnBruInfo_img = irnBruCan

################################
## Image Transcolour settings ##
################################

# Set the colour to ignore on the images 
screen.set_colorkey(transcolour)
shrub_img.set_colorkey(transcolour)
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
irnBruCan.set_colorkey(transcolour)

###################
## Image scaling ##
###################

# Image scale down from 100x100 to 50x50px
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
shrub_img = pygame.transform.scale(shrub_img, (50,50))

# Specific scale downs
irnBruInfo_img = pygame.transform.scale(irnBruInfo_img, (52,90))
waferInfo_img = pygame.transform.scale(waferInfo_img, (170,45))
wafer_obj = pygame.transform.scale(wafer_obj, (50,25))
irnBruObj_img = pygame.transform.scale(irnBruObj_img, (30,50))
information_board = pygame.transform.scale(information_board, (800,600))
background_img = pygame.transform.scale(background_img, screenMode)

##############################################
## Shrub Wall Collision Detection Functions ##
##############################################

# Collistion Detection for 3rd shrub wall 
def detectShrub_03_Collision(x_pos,y_pos):
    global directionIndicator
    global shrub6Block_03
    global player_speed
    
    if directionIndicator == 0 and y_pos > (shrub6Block_03[0][1]-50) and y_pos < (shrub6Block_03[3][1]+50) and x_pos > (shrub6Block_03[0][0]-50) and x_pos < (shrub6Block_03[2][0]+50):
        y_pos = y_pos - player_speed
        
    if directionIndicator == 2 and x_pos > (shrub6Block_03[0][0]-50) and x_pos < (shrub6Block_03[2][0]+50) and y_pos > (shrub6Block_03[0][1]-50) and y_pos < (shrub6Block_03[3][1]+50):
        x_pos = x_pos - player_speed
        
    # Up direction 
    if directionIndicator == 1 and y_pos < (shrub6Block_03[3][1]+50) and y_pos > (shrub6Block_03[0][1]-50) and x_pos > (shrub6Block_03[0][0]-50) and x_pos < (shrub6Block_03[2][0]+50):
        y_pos = y_pos + player_speed
        
    # Left direction 
    if directionIndicator == 3 and x_pos < (shrub6Block_03[2][0]+50) and x_pos > (shrub6Block_03[0][0]-50) and y_pos > (shrub6Block_03[2][1]-50) and y_pos < (shrub6Block_03[5][1]+50):
        x_pos = x_pos + player_speed
        
    return x_pos, y_pos

# Collision Detection for 2nd shrub wall 
def detectShrub_02_Collision(x_pos,y_pos):
    global directionIndicator
    global shrub6Block_02
    global player_speed
    
    if directionIndicator == 0 and y_pos > (shrub6Block_02[0][1]-50) and y_pos < (shrub6Block_02[3][1]+50) and x_pos > (shrub6Block_02[0][0]-50) and x_pos < (shrub6Block_02[2][0]+50):
        y_pos = y_pos - player_speed
        
    if directionIndicator == 2 and x_pos > (shrub6Block_02[0][0]-50) and x_pos < (shrub6Block_02[2][0]+50) and y_pos > (shrub6Block_02[0][1]-50) and y_pos < (shrub6Block_02[3][1]+50):
        x_pos = x_pos - player_speed
        
    # Up direction 
    if directionIndicator == 1 and y_pos < (shrub6Block_02[3][1]+50) and y_pos > (shrub6Block_02[0][1]-50) and x_pos > (shrub6Block_02[0][0]-50) and x_pos < (shrub6Block_02[2][0]+50):
        y_pos = y_pos + player_speed
        
    # Left direction 
    if directionIndicator == 3 and x_pos < (shrub6Block_02[2][0]+50) and x_pos > (shrub6Block_02[0][0]-50) and y_pos > (shrub6Block_02[2][1]-50) and y_pos < (shrub6Block_02[5][1]+50):
        x_pos = x_pos + player_speed
        
    return x_pos, y_pos

# Collision Detection for 1st shrub wall 
def detectShrub_01_Collision(x_pos,y_pos):
    global directionIndicator
    global shrubLBlock_01
    global player_speed
    
    # Collision detection for first L-block (down direction)
    
    if directionIndicator == 0 and y_pos > (shrubLBlock_01[0][1]-50) and y_pos < (shrubLBlock_01[0][1]+50) and x_pos > (shrubLBlock_01[0][0]-50) and x_pos < (shrubLBlock_01[2][0]+50):
        y_pos = y_pos - player_speed
        
    # Collision detection for first L-block (right direction)
    
    if directionIndicator == 2 and x_pos > (shrubLBlock_01[0][0]-50) and x_pos < (shrubLBlock_01[0][0]+50) and y_pos > (shrubLBlock_01[0][1]-50) and y_pos < (shrubLBlock_01[4][1]+50):
        x_pos = x_pos - player_speed
        
    # Collision detection for first L-block (left direction)
    
    if directionIndicator == 3:
        
        if x_pos < (shrubLBlock_01[2][0]+50) and x_pos > (shrubLBlock_01[0][0]-50) and y_pos > (shrubLBlock_01[2][1]-50) and y_pos < (shrubLBlock_01[2][1]+50):
            x_pos = x_pos + player_speed
            
        if x_pos < (shrubLBlock_01[3][0]+50) and x_pos > (shrubLBlock_01[3][0]-50) and y_pos > (shrubLBlock_01[3][1]-50) and y_pos < (shrubLBlock_01[4][1]+50):
            x_pos = x_pos + player_speed
    
    # Collision detection for first L-block (up direction)
    
    if directionIndicator == 1:
        
        if y_pos < (shrubLBlock_01[4][1]+50) and y_pos > (shrubLBlock_01[0][1]-50) and x_pos > (shrubLBlock_01[4][0]-50) and x_pos < (shrubLBlock_01[4][0]+50):
            y_pos = y_pos + player_speed
            
        if y_pos < (shrubLBlock_01[1][1]+50) and y_pos > (shrubLBlock_01[1][1]-50) and x_pos > (shrubLBlock_01[1][0]) and x_pos < (shrubLBlock_01[2][0]+50):
            y_pos = y_pos + player_speed
            
            
    return x_pos, y_pos
    
    


######################
##  MAIN GAME LOOP  ##
######################

while(dead==False):    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
            
        if event.type == pygame.USEREVENT:            
            if timesUp == False:            
                counter-=1
                text = str(counter)
            
                if counter < 0:
                    if timerMinValue > 0:
                        timerMinValue = timerMinValue - 1
                        counter = 59
                        text = str(counter)
                        
                    if timerMinValue == 0:
                        counter = 59
                        text = str(counter)
                        timesUp = True
                
            if counter == 0 and timerMinValue == 0:
                print("*** TIME'S UP! GAME OVER ***")
                dead = True
                
            if timesUp == True:
                counter = 0
                text = str(counter)
            
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:            

            # Check to see if the Escape key has been pressed (exit's the game program)
            if event.key == pygame.K_ESCAPE:
                dead = True
                
    keys = pygame.key.get_pressed()

    ############################################################
    ## Handle diagonal entries (to prevent diagonal movement) ##
    ############################################################
    
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        player_x_pos = player_x_pos - player_speed
        player_y_pos = player_y_pos - player_speed
        
    if keys[pygame.K_LEFT] and keys [pygame.K_DOWN]:
        player_x_pos = player_x_pos + player_speed
        player_y_pos = player_y_pos - player_speed
        
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        player_x_pos = player_x_pos - player_speed
        player_y_pos = player_y_pos + player_speed
        
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        player_x_pos = player_x_pos + player_speed
        player_y_pos = player_y_pos + player_speed
    
    
    #######################################################
    ## Handle Player Directions (Left,Right,Up and Down) ##
    #######################################################    
    
    if keys[pygame.K_RIGHT]:
        leftStage = 0
        upStage = 0
        downStage = 0
        if player_x_pos <= 1000:
            player_x_pos = player_x_pos + player_speed
        rightStage = rightStage + 1
        directionIndicator = 2
        
    if keys[pygame.K_LEFT]:
        rightStage = 0
        upStage = 0
        downStage = 0
        if player_x_pos >= 125:
            player_x_pos = player_x_pos - player_speed
        leftStage = leftStage + 1
        directionIndicator = 3
        
    if keys[pygame.K_UP]:
        downStage = 0
        rightStage = 0
        leftStage = 0
        if player_y_pos >= 125:
            player_y_pos = player_y_pos - player_speed
        upStage = upStage + 1
        directionIndicator = 1
        
    if keys[pygame.K_DOWN]:        
        upStage = 0
        rightStage = 0
        leftStage = 0
        if player_y_pos <= 1000:
            player_y_pos = player_y_pos + player_speed
        downStage = downStage + 1
        directionIndicator = 0

    ################################
    ## Display Game Screen Layout ##
    ################################
    
    screen.blit(background_img, (0,0))
    screen.blit(game_grid, (100,100))   
    screen.blit(irnBruCan, (1200, 100))
    screen.blit(wafer_img, (1450, 150))
    screen.blit(information_board, (1150,300))
    screen.blit(irnBruInfo_img, (1300,450))
    screen.blit(waferInfo_img, (1250,650))
    
    text_surface, rect = GAME_FONT.render(str(irnBruScore), (0, 255, 33))
    screen.blit(text_surface, (1350, 150))
    
    waferscore, rect = GAME_FONT.render(str(waferScore), (0,255,33))
    screen.blit(waferscore, (1850,150))
    
    irnBruPointsInfo, rect = GAME_FONT.render(" = 2 POINTS", (0,255,33))
    screen.blit(irnBruPointsInfo, (1350,470))
    
    waferPointsInfo, rect = GAME_FONT.render(" = 1 POINT", (0,255,33))
    screen.blit(waferPointsInfo, (1400,650))
    
    timelimit, rect = GAME_FONT.render("TIME - ", (0,255,33))
    screen.blit(timelimit, (600,25))
    
    # Handle 0's with number of digits showing
    if timerMinValue < 10:
        timelimitvalue, rect = GAME_FONT.render("0" + str(timerMinValue) + ":", (0,255,33))
        
    if timerMinValue >= 10:
        timelimitvalue, rect = GAME_FONT.render(str(timerMinValue) + ":", (0,255,33))
    
    screen.blit(timelimitvalue, (900,25))
    
    if int(text) < 10:
        timlimit, rect = GAME_FONT.render("0"+text, (0,255,33))
        
    if int(text) >= 10:    
        timlimit, rect = GAME_FONT.render(text, (0,255,33))
    
    screen.blit(timlimit, (990,25))

    # Output shrub on screen (L-Block)
    screen.blit(shrub_img, shrubLBlock_01[0])
    screen.blit(shrub_img, shrubLBlock_01[1])
    screen.blit(shrub_img, shrubLBlock_01[2])
    screen.blit(shrub_img, shrubLBlock_01[3])
    screen.blit(shrub_img, shrubLBlock_01[4])    
    
    # Output 6-block 
    screen.blit(shrub_img, shrub6Block_02[0])
    screen.blit(shrub_img, shrub6Block_02[1])
    screen.blit(shrub_img, shrub6Block_02[2])
    screen.blit(shrub_img, shrub6Block_02[3])
    screen.blit(shrub_img, shrub6Block_02[4])
    screen.blit(shrub_img, shrub6Block_02[5])

    # Output 6-block 
    screen.blit(shrub_img, shrub6Block_03[0])
    screen.blit(shrub_img, shrub6Block_03[1])
    screen.blit(shrub_img, shrub6Block_03[2])
    screen.blit(shrub_img, shrub6Block_03[3])
    screen.blit(shrub_img, shrub6Block_03[4])
    screen.blit(shrub_img, shrub6Block_03[5])
    
    # Output objects on game grid 
    while irnBruObjCounter < len(irnBruObjStruct):
        if irnBruObjStruct[irnBruObjCounter][2] == True:
            screen.blit(irnBruObj_img, (irnBruObjStruct[irnBruObjCounter][0],irnBruObjStruct[irnBruObjCounter][1]))
        irnBruObjCounter = irnBruObjCounter + 1
    
    irnBruObjCounter = 0
    
    while waferObjCounter < len(waferObjStruct):
        if waferObjStruct[waferObjCounter][2] == True:
            screen.blit(wafer_obj, (waferObjStruct[waferObjCounter][0],waferObjStruct[waferObjCounter][1]))  
        waferObjCounter = waferObjCounter + 1
        
    waferObjCounter = 0

    # Collision detection with Irn-Bru objects on the game grid 
    
    while irnBruObjCounter < len(irnBruObjStruct):
        if player_x_pos >= (irnBruObjStruct[irnBruObjCounter][0]-irnBruHorizLength) and player_x_pos <= (irnBruObjStruct[irnBruObjCounter][0]+irnBruHorizLength) and player_y_pos >= (irnBruObjStruct[irnBruObjCounter][1]-irnBruVertLength) and player_y_pos <= (irnBruObjStruct[irnBruObjCounter][1]+irnBruVertLength) and irnBruObjStruct[irnBruObjCounter][2] == True:
            irnBruScore = irnBruScore + 2
            irnBruObjStruct[irnBruObjCounter][2] = False 
        irnBruObjCounter = irnBruObjCounter + 1
        
    irnBruObjCounter = 0
    
    # Detect collision with caramel wafer object 
    while waferObjCounter < len(waferObjStruct):
        if player_x_pos >= (waferObjStruct[waferObjCounter][0]-30) and player_x_pos <= (waferObjStruct[waferObjCounter][0]+30) and player_y_pos >= (waferObjStruct[waferObjCounter][1]-35) and player_y_pos <= (waferObjStruct[waferObjCounter][1]+35) and waferObjStruct[waferObjCounter][2] == True:
            waferScore = waferScore + 1
            waferObjStruct[waferObjCounter][2] = False      
        waferObjCounter = waferObjCounter + 1
        
    waferObjCounter = 0

    #################################################
    ## Player Collision Detection with Shrub Walls ##
    #################################################
    
    player_x_pos, player_y_pos = detectShrub_01_Collision(player_x_pos, player_y_pos)
    player_x_pos, player_y_pos = detectShrub_02_Collision(player_x_pos, player_y_pos)
    player_x_pos, player_y_pos = detectShrub_03_Collision(player_x_pos, player_y_pos)    

    ###############################
    ## Player Animation Sequence ##
    ###############################
    
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
            
    if irnBruScore == 16 and waferScore == 4:
        print("*** LEVEL COMPLETED ***")        
        dead = True 

    pygame.display.flip()
    clock.tick(clock_tick_rate)
pygame.quit()



