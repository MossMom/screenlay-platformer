# Import libraries and levels and initialize the game engine
import pygame
from level0 import GameMap as lvl0
from level1 import GameMap as lvl1
from level2 import GameMap as lvl2
from level3 import GameMap as lvl3
from level4 import GameMap as lvl4
from level5 import GameMap as lvl5
from level6 import GameMap as lvl6
from level7 import GameMap as lvl7
from level8 import GameMap as lvl8
from level9 import GameMap as lvl9

pygame.init()

# Open new window, caption it "Platformer"
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Platformer")

# Game loop variable
doExit = False

# Controls how fast the screen updates, also the counter variable for interval changes
clock = pygame.time.Clock()
counter = 0
counterFlip = 0

# Level & Map variables
GameMap = lvl0
level = 0
color = 150,150,150 # Yellow - 238,175,97 | 244,159,97 | Orange - 251,144,98 | 244,118,103 | Red - 238,93,108 | 222,83,127 | Pink - 206,73,147 | 156,43,139 | Purple - 106,13,131
enterX = 50
enterY = 575
exitX = 150
exitY = 100

# WASD icons
wPic = pygame.image.load("W.png")
wRect = wPic.get_rect(topleft=(0,625))
aPic = pygame.image.load("A.png")
aRect = aPic.get_rect(topleft=(75,625))
sPic = pygame.image.load("S.png")
sRect = sPic.get_rect(topleft=(150,625))
dPic = pygame.image.load("D.png")
dRect = dPic.get_rect(topleft=(225,625))
# ARROW icons
upPic = pygame.image.load("UP.png")
upRect = upPic.get_rect(topleft=(0,625))
leftPic = pygame.image.load("LEFT.png")
leftRect = leftPic.get_rect(topleft=(75,625))
downPic = pygame.image.load("DOWN.png")
downRect = downPic.get_rect(topleft=(150,625))
rightPic = pygame.image.load("RIGHT.png")
rightRect = rightPic.get_rect(topleft=(225,625))
# SHIFT icon
shiftPic = pygame.image.load("SHIFT.png")
shiftRect = shiftPic.get_rect(topleft=(325,625))
# SPACE icon
spacePic = pygame.image.load("SPACE.png")
spaceRect = spacePic.get_rect(topleft=(500,625))
# SIGNATURE icon
signPic = pygame.image.load("SIGNATURE.png")
signRect = signPic.get_rect(topleft=(888,625))
# Entrance & exit icons PART 1
entrancePic = pygame.image.load("ENTRANCE.png")
exitPic = pygame.image.load("EXIT.png")

# Player variables
p1x = 50 # X position
p1y = 575 # Y position
p1xv = 0 # X velocity
p1yv = 0 # Y velocity
isOnGround = False # Check if touching ground
p1xd = 0 # X direction, 0 = down, 1 = up
p1yd = 0 # Y direction, 0 = left, 1 = right

while not doExit: #GAME LOOP------------------------------------------------------------

# Event queue stuff
    clock.tick(60)

# This allows the user to close the game
    for event in pygame.event.get(): # Check if user did something
        if event.type == pygame.QUIT: # Check if user clicked close
            doExit = True # Flag that we are done so we exit the game loop

# Entrance & exit icons PART 2
    entranceRect = entrancePic.get_rect(topleft=(enterX,enterY))
    exitRect = exitPic.get_rect(topleft=(exitX,exitY))

    # Game logic------------------------------------------------------------------------

# Keeps track of what keys are pressed
    keys = pygame.key.get_pressed()
# Jump controls (maybe eventually change for air stalling mechanic)
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and isOnGround == True and GameMap[int((p1y-1)/25)][int((p1x+1)/25)] != 1 and GameMap[int((p1y-1)/25)][int((p1x+24)/25)] != 1: 
        p1yv = -6
        isOnGround = False
# Walk left controls
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]): 
        p1xv = -5
# Walk right controls
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]): 
        p1xv = 5
# Make no movement with both held down
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        p1xv = 0
# Snap to grid function
    if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and (isOnGround == True):
        p1x = ((p1x+12.5)//25)*25
        p1y = ((p1y+12.5)//25)*25
# Return to "spawn" with [Space]
    if keys[pygame.K_SPACE]:
        p1x = enterX
        p1y = enterY

# Checks if facing down
    if p1yv > 0: 
        p1yd = 0
# Checks if facing up
    if p1yv < 0: 
        p1yd = 1
# Checks if facing right
    if p1xv > 0: 
        p1xd = 1
# Checks if facing left
    if p1xv < 0: 
        p1xd = 0
        
# Update current level
    if level == 0:
        GameMap = lvl0
        color = 150,150,150 # Grey
        enterX = 50
        enterY = 575
        exitX = 50
        exitY = 200
    if level == 1:
        GameMap = lvl1
        color = 238,175,97 # Yellow
        
    if level == 2:
        GameMap = lvl2
        color = 244,159,97 # Yellow-Orange
        
    if level == 3:
        GameMap = lvl3
        color = 251,144,98 # Orange
        
    if level == 4:
        GameMap = lvl4
        color = 244,118,103 # Orange-Red
        
    if level == 5:
        GameMap = lvl5
        color = 238,93,108 # Red
        
    if level == 6:
        GameMap = lvl6
        color = 222,83,127 # Red-Pink
        
    if level == 7:
        GameMap = lvl7
        color = 206,73,147 # Pink
        
    if level == 8:
        GameMap = lvl8
        color = 156,43,139 # Pink-Purple
        
    if level == 9:
        GameMap = lvl9
        color = 106,13,131 # Purple

# Change the level based on the number hit
    if keys[pygame.K_0]:
        level = 0
    if keys[pygame.K_1]:
        level = 1
    if keys[pygame.K_2]:
        level = 2
    if keys[pygame.K_3]:
        level = 3
    if keys[pygame.K_4]:
        level = 4
    if keys[pygame.K_5]:
        level = 5
    if keys[pygame.K_6]:
        level = 6
    if keys[pygame.K_7]:
        level = 7
    if keys[pygame.K_8]:
        level = 8
    if keys[pygame.K_9]:
        level = 9


# Update counter
    counter += 1
        
    # Physics---------------------------------------------------------------------------
    
# Gravity
    if isOnGround == False: 
        if p1yv < 7:
            p1yv += .3
            
# Friction
    p1xv *= .5
    
# This should solve the slight nudge after you stop moving
    if p1xv < 1 and p1xv > -1:
        p1xv = 0
    
# Check for left collisions
    if (GameMap[int((p1y+23)/25)][int((p1x-1)/25)] == 1 or GameMap[int((p1y+2)/25)][int((p1x-1)/25)] == 1): 
        if p1xv < 0:
            p1xv = 0
# Keep left side out of wall
        if GameMap[int((p1y+12.5)/25)][int((p1x)/25)] == 1:
            p1x = ((p1x+3)//25)*25
            
# Check for right collisions
    if (GameMap[int((p1y+23)/25)][int((p1x+25)/25)] == 1 or GameMap[int((p1y+2)/25)][int((p1x+25)/25)] == 1): 
        if p1xv > 0:
            p1xv = 0
# Keep right side out of wall
        if GameMap[int((p1y+12.5)/25)][int((p1x+25)/25)] == 1: 
            p1x = ((p1x+22)//25)*25
            
# Check for bottom collisions
    if (GameMap[int((p1y+25)/25)][int((p1x+2)/25)] == 1 or GameMap[int((p1y+25)/25)][int((p1x+23)/25)] == 1): 
        if p1yv > 0:
            p1yv = 0
        isOnGround = True
    else:
        isOnGround = False

# Check for top collisions
    if (GameMap[int((p1y)/25)][int((p1x+2)/25)] == 1 or GameMap[int((p1y)/25)][int((p1x+23)/25)] == 1): 
        if p1yv < 0:
            p1yv = 0
# Keep out of ceiling
        p1y = (((p1y+25)//25)*25) 

# Update p1 horizontal position
    p1x += p1xv 
# Update p1 vertical position
    p1y += p1yv 
        
# Keep out of ground
    if (GameMap[int((p1y+25)/25)][int((p1x+2)/25)] == 1 or GameMap[int((p1y+25)/25)][int((p1x+23)/25)] == 1):
        p1y = ((p1y//25)*25)
        
    # Render----------------------------------------------------------------------------

# Wipe screen black
    screen.fill((0,0,0)) 
    
# Draw the level
    for i in range(0,25,1): # Rows (height)
        for j in range (0,40,1): # Columns (width)
            if GameMap[i][j]==1:# Ground1 (this color changes)
                pygame.draw.rect(screen, (color), (j*25, i*25, 25, 25))
            if GameMap[i][j]==2:# Entrance (very very dark grey)
                pygame.draw.rect(screen, (40, 40, 40), (j*25, i*25, 25, 25))
            if GameMap[i][j]==3:# Exit (dark grey)
                pygame.draw.rect(screen, (100, 100, 100), (j*25, i*25, 25, 25))
                
# Controls at bottom of screen
    if counter < 90:
        screen.blit(wPic, wRect)
        screen.blit(aPic, aRect)
        screen.blit(sPic, sRect)
        screen.blit(dPic, dRect)
    if counter >= 90:
        screen.blit(upPic, upRect)
        screen.blit(leftPic, leftRect)
        screen.blit(downPic, downRect)
        screen.blit(rightPic, rightRect)
    if counter >= 180:
        counter = 0
    screen.blit(shiftPic, shiftRect)
    screen.blit(spacePic, spaceRect)
    screen.blit(signPic, signRect)
    screen.blit(entrancePic, entranceRect)
    screen.blit(exitPic, exitRect)

# Draw the player
    pygame.draw.rect(screen, (250, 250, 250), (p1x, p1y, 25, 25)) 
    
# Update the screen
    pygame.display.flip()


# END GAME LOOP ------------------------------------------------------------------

# When game is done close down pygame
pygame.quit() 
