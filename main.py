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

shrubScale = 25

# Game Grid image position 
gamegrid_xpos = 100
gamegrid_ypos = 100
gamegrid_wall_width = 25

# Shrub wall 1 (L-Block)
shrubLBlock_01 = []
shrubLBlock_01.append([(gamegrid_xpos+gamegrid_wall_width+50),(gamegrid_ypos+gamegrid_wall_width+50)])
shrubLBlock_01.append([(shrubLBlock_01[0][0]+shrubScale),(gamegrid_ypos+gamegrid_wall_width+50)])
shrubLBlock_01.append([(shrubLBlock_01[1][0]+shrubScale),(gamegrid_ypos+gamegrid_wall_width+50)])    
shrubLBlock_01.append([(gamegrid_xpos+gamegrid_wall_width+50),(shrubLBlock_01[2][1]+shrubScale)])
shrubLBlock_01.append([(gamegrid_xpos+gamegrid_wall_width+50),(shrubLBlock_01[3][1]+shrubScale)])

# Shrub wall 2 (6-block)
shrub6Block_02 = []    
shrub6Block_02.append([(gamegrid_xpos+gamegrid_wall_width+300),(gamegrid_ypos+gamegrid_wall_width+150)])
shrub6Block_02.append([(shrub6Block_02[0][0]+shrubScale),(shrub6Block_02[0][1])])
shrub6Block_02.append([(shrub6Block_02[1][0]+shrubScale),(shrub6Block_02[1][1])])
shrub6Block_02.append([shrub6Block_02[0][0],(shrub6Block_02[1][1]+shrubScale)])
shrub6Block_02.append([(shrub6Block_02[0][0]+shrubScale),(shrub6Block_02[3][1])])
shrub6Block_02.append([(shrub6Block_02[1][0]+shrubScale),(shrub6Block_02[3][1])])

# Shrub wall 3 (6-block)
shrub6Block_03 = []    
shrub6Block_03.append([(gamegrid_xpos+gamegrid_wall_width+100),(gamegrid_ypos+gamegrid_wall_width+300)])
shrub6Block_03.append([(shrub6Block_03[0][0]+shrubScale),(shrub6Block_03[0][1])])
shrub6Block_03.append([(shrub6Block_03[1][0]+shrubScale),(shrub6Block_03[1][1])])
shrub6Block_03.append([(shrub6Block_03[0][0]),(shrub6Block_03[2][1]+shrubScale)])
shrub6Block_03.append([(shrub6Block_03[1][0]),(shrub6Block_03[3][1])])
shrub6Block_03.append([(shrub6Block_03[2][0]),(shrub6Block_03[3][1])])

# Irn-Bru object structure 
irnBruObjStruct = []
irnBruObjStruct.append([(gamegrid_xpos+400),(gamegrid_ypos+400),True])
irnBruObjStruct.append([(gamegrid_xpos+300),(gamegrid_ypos+300),True])
irnBruObjStruct.append([(gamegrid_xpos+100),(gamegrid_ypos+450),True]) # 100, 450
irnBruObjStruct.append([(gamegrid_xpos+300),(gamegrid_ypos+100),True]) # 300, 100
irnBruObjStruct.append([(gamegrid_xpos+50),(gamegrid_ypos+300),True]) # 50,300
irnBruObjStruct.append([(gamegrid_xpos+200),(gamegrid_ypos+200),True]) # 200, 200
irnBruObjStruct.append([(gamegrid_xpos+300),(gamegrid_ypos+450),True]) # 300, 450
irnBruObjStruct.append([(gamegrid_xpos+100),(gamegrid_ypos+200),True]) # 100,200

# Wafer object structure 
waferObjStruct = []
waferObjStruct.append([(gamegrid_xpos+450),(gamegrid_ypos+25),True]) # 450, 25
waferObjStruct.append([(gamegrid_xpos+150),(gamegrid_ypos+300),True]) # 150,300
waferObjStruct.append([(gamegrid_xpos+300),(gamegrid_ypos+400),True]) # 300,400
waferObjStruct.append([(gamegrid_xpos+400),(gamegrid_ypos+300),True]) # 400,300

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
irnBruVertLength = 25 # 40 pixels (irn-bru object image)
irnBruHorizLength = 15 # 30 pixels (irb-bru object image)
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

timerMinValue = 5
timesUp = False

dead=False # Used to terminate the game loop 

#############################
## Screen Resolution Setup ##
#############################

# Set and get screen mode 
screenMode = (1366,768)
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
wafer_obj = wafer_img 

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

characterScaleSize = 25

# Image scale down from 100x100 to 50x50px
characterFront_img = pygame.transform.scale(characterFront_img, (characterScaleSize,characterScaleSize))
characterBack_img = pygame.transform.scale(characterBack_img, (characterScaleSize,characterScaleSize))
characterLeft_img = pygame.transform.scale(characterLeft_img, (characterScaleSize,characterScaleSize))
characterRight_img = pygame.transform.scale(characterRight_img, (characterScaleSize,characterScaleSize))
characterFront01_img = pygame.transform.scale(characterFront01_img, (characterScaleSize,characterScaleSize))
characterFront02_img = pygame.transform.scale(characterFront02_img, (characterScaleSize,characterScaleSize))
characterBack01_img = pygame.transform.scale(characterBack01_img, (characterScaleSize,characterScaleSize))
characterBack02_img = pygame.transform.scale(characterBack02_img, (characterScaleSize,characterScaleSize))
characterLeft01_img = pygame.transform.scale(characterLeft01_img, (characterScaleSize,characterScaleSize))
characterLeft02_img = pygame.transform.scale(characterLeft02_img, (characterScaleSize,characterScaleSize))
characterRight01_img = pygame.transform.scale(characterRight01_img, (characterScaleSize,characterScaleSize))
characterRight02_img = pygame.transform.scale(characterRight02_img, (characterScaleSize,characterScaleSize))

# Scale shrub image 
shrubScale = 25
shrub_img = pygame.transform.scale(shrub_img, (shrubScale,shrubScale))

# Specific scale downs
wafer_obj = pygame.transform.scale(wafer_obj, (25,14))
irnBruObj_img = pygame.transform.scale(irnBruObj_img, (15,25))
information_board = pygame.transform.scale(information_board, (400,250))
background_img = pygame.transform.scale(background_img, screenMode)

# Resize the game grid
game_grid = pygame.transform.scale(game_grid, (500,500))

##############################################
## Shrub Wall Collision Detection Functions ##
##############################################

# Collistion Detection for 3rd shrub wall 
def detectShrub_03_Collision(x_pos,y_pos):
    global directionIndicator
    global shrub6Block_03
    global player_speed
    
    if directionIndicator == 0 and y_pos > (shrub6Block_03[0][1]-characterScaleSize) and y_pos < (shrub6Block_03[3][1]+characterScaleSize) and x_pos > (shrub6Block_03[0][0]-characterScaleSize) and x_pos < (shrub6Block_03[2][0]+characterScaleSize):
        y_pos = y_pos - player_speed
        
    if directionIndicator == 2 and x_pos > (shrub6Block_03[0][0]-characterScaleSize) and x_pos < (shrub6Block_03[2][0]+characterScaleSize) and y_pos > (shrub6Block_03[0][1]-characterScaleSize) and y_pos < (shrub6Block_03[3][1]+characterScaleSize):
        x_pos = x_pos - player_speed
        
    # Up direction 
    if directionIndicator == 1 and y_pos < (shrub6Block_03[3][1]+characterScaleSize) and y_pos > (shrub6Block_03[0][1]-characterScaleSize) and x_pos > (shrub6Block_03[0][0]-characterScaleSize) and x_pos < (shrub6Block_03[2][0]+characterScaleSize):
        y_pos = y_pos + player_speed
        
    # Left direction 
    if directionIndicator == 3 and x_pos < (shrub6Block_03[2][0]+characterScaleSize) and x_pos > (shrub6Block_03[0][0]-characterScaleSize) and y_pos > (shrub6Block_03[2][1]-characterScaleSize) and y_pos < (shrub6Block_03[5][1]+characterScaleSize):
        x_pos = x_pos + player_speed
        
    return x_pos, y_pos

# Collision Detection for 2nd shrub wall 
def detectShrub_02_Collision(x_pos,y_pos):
    global directionIndicator
    global shrub6Block_02
    global player_speed
    
    if directionIndicator == 0 and y_pos > (shrub6Block_02[0][1]-characterScaleSize) and y_pos < (shrub6Block_02[3][1]+characterScaleSize) and x_pos > (shrub6Block_02[0][0]-characterScaleSize) and x_pos < (shrub6Block_02[2][0]+characterScaleSize):
        y_pos = y_pos - player_speed
        
    if directionIndicator == 2 and x_pos > (shrub6Block_02[0][0]-characterScaleSize) and x_pos < (shrub6Block_02[2][0]+characterScaleSize) and y_pos > (shrub6Block_02[0][1]-characterScaleSize) and y_pos < (shrub6Block_02[3][1]+characterScaleSize):
        x_pos = x_pos - player_speed
        
    # Up direction 
    if directionIndicator == 1 and y_pos < (shrub6Block_02[3][1]+characterScaleSize) and y_pos > (shrub6Block_02[0][1]-characterScaleSize) and x_pos > (shrub6Block_02[0][0]-characterScaleSize) and x_pos < (shrub6Block_02[2][0]+characterScaleSize):
        y_pos = y_pos + player_speed
        
    # Left direction 
    if directionIndicator == 3 and x_pos < (shrub6Block_02[2][0]+characterScaleSize) and x_pos > (shrub6Block_02[0][0]-characterScaleSize) and y_pos > (shrub6Block_02[2][1]-characterScaleSize) and y_pos < (shrub6Block_02[5][1]+characterScaleSize):
        x_pos = x_pos + player_speed
        
    return x_pos, y_pos

# Collision Detection for 1st shrub wall 
def detectShrub_01_Collision(x_pos,y_pos):
    global directionIndicator
    global shrubLBlock_01
    global player_speed
    
    # Collision detection for first L-block (down direction)
    
    if directionIndicator == 0 and y_pos > (shrubLBlock_01[0][1]-characterScaleSize) and y_pos < (shrubLBlock_01[0][1]+characterScaleSize) and x_pos > (shrubLBlock_01[0][0]-characterScaleSize) and x_pos < (shrubLBlock_01[2][0]+characterScaleSize):
        y_pos = y_pos - player_speed
        
    # Collision detection for first L-block (right direction)
    
    if directionIndicator == 2 and x_pos > (shrubLBlock_01[0][0]-characterScaleSize) and x_pos < (shrubLBlock_01[0][0]+characterScaleSize) and y_pos > (shrubLBlock_01[0][1]-characterScaleSize) and y_pos < (shrubLBlock_01[4][1]+characterScaleSize):
        x_pos = x_pos - player_speed
        
    # Collision detection for first L-block (left direction)
    
    if directionIndicator == 3:
        
        if x_pos < (shrubLBlock_01[2][0]+characterScaleSize) and x_pos > (shrubLBlock_01[0][0]-characterScaleSize) and y_pos > (shrubLBlock_01[2][1]-characterScaleSize) and y_pos < (shrubLBlock_01[2][1]+characterScaleSize):
            x_pos = x_pos + player_speed
            
        if x_pos < (shrubLBlock_01[3][0]+characterScaleSize) and x_pos > (shrubLBlock_01[3][0]-characterScaleSize) and y_pos > (shrubLBlock_01[3][1]-characterScaleSize) and y_pos < (shrubLBlock_01[4][1]+characterScaleSize):
            x_pos = x_pos + player_speed
    
    # Collision detection for first L-block (up direction)
    
    if directionIndicator == 1:
        
        if y_pos < (shrubLBlock_01[4][1]+characterScaleSize) and y_pos > (shrubLBlock_01[0][1]-characterScaleSize) and x_pos > (shrubLBlock_01[4][0]-characterScaleSize) and x_pos < (shrubLBlock_01[4][0]+characterScaleSize):
            y_pos = y_pos + player_speed
            
        if y_pos < (shrubLBlock_01[1][1]+characterScaleSize) and y_pos > (shrubLBlock_01[1][1]-characterScaleSize) and x_pos > (shrubLBlock_01[1][0]) and x_pos < (shrubLBlock_01[2][0]+characterScaleSize):
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
        if player_x_pos <= (game_grid.get_width()+gamegrid_xpos-(gamegrid_wall_width*2)):
            player_x_pos = player_x_pos + player_speed
        rightStage = rightStage + 1
        directionIndicator = 2
        
    if keys[pygame.K_LEFT]:
        rightStage = 0
        upStage = 0
        downStage = 0
        if player_x_pos >= (gamegrid_xpos+gamegrid_wall_width):
            player_x_pos = player_x_pos - player_speed
        leftStage = leftStage + 1
        directionIndicator = 3
        
    if keys[pygame.K_UP]:
        downStage = 0
        rightStage = 0
        leftStage = 0
        if player_y_pos >= (gamegrid_ypos+gamegrid_wall_width):
            player_y_pos = player_y_pos - player_speed
        upStage = upStage + 1
        directionIndicator = 1
        
    if keys[pygame.K_DOWN]:        
        upStage = 0
        rightStage = 0
        leftStage = 0
        if player_y_pos <= (game_grid.get_height()+gamegrid_ypos-(gamegrid_wall_width*2)):
            player_y_pos = player_y_pos + player_speed
        downStage = downStage + 1
        directionIndicator = 0

    ################################
    ## Display Game Screen Layout ##
    ################################
    
    screen.blit(background_img, (0,0))
    screen.blit(game_grid, (gamegrid_xpos,gamegrid_ypos))   
    
    # Game Score Irn Bru image 
    screen.blit(irnBruCan, (gamegrid_xpos+550, gamegrid_ypos))
    
    # Game Score wafer image 
    screen.blit(wafer_img, (gamegrid_xpos+780, gamegrid_ypos+50))
    
    # Display information board relative position to game grid
    screen.blit(information_board, (gamegrid_xpos+550,gamegrid_ypos+250))
    
    text_surface, rect = GAME_FONT.render(str(irnBruScore), (0, 255, 33))
    screen.blit(text_surface, (gamegrid_xpos+700, gamegrid_ypos+50))
    
    waferscore, rect = GAME_FONT.render(str(waferScore), (0,255,33))
    screen.blit(waferscore, (gamegrid_xpos+1170,gamegrid_ypos+50))
    
    timelimit, rect = GAME_FONT.render("TIME - ", (0,255,33))
    screen.blit(timelimit, (gamegrid_xpos+300,gamegrid_ypos-80))
    
    # Handle 0's with number of digits showing
    if timerMinValue < 10:
        timelimitvalue, rect = GAME_FONT.render("0" + str(timerMinValue) + ":", (0,255,33))
        
    if timerMinValue >= 10:
        timelimitvalue, rect = GAME_FONT.render(str(timerMinValue) + ":", (0,255,33))
    
    screen.blit(timelimitvalue, (gamegrid_xpos+600,gamegrid_ypos-80))
    
    if int(text) < 10:
        timlimit, rect = GAME_FONT.render("0"+text, (0,255,33))
        
    if int(text) >= 10:    
        timlimit, rect = GAME_FONT.render(text, (0,255,33))
    
    screen.blit(timlimit, (gamegrid_xpos+690,gamegrid_ypos-80))

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



