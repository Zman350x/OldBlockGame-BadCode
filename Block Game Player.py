#Controls

print('Block Game Player\n\n-------------------------\nControls\n\nMove: L & R arrows\nJump: Up arrow\n-------------------------\nHow to Play\n\nAvoid radioactive blocks and find the key to open the door.\nGet to the door to win!\n-------------------------')

#imports

import pygame, pickle as pic, os

if os.path.exists('WorldList.pickle'):
    WorldOpen = open('WorldList.pickle','rb')
    WorldList = pic.load(WorldOpen)
else:
    print('\nCreate Map First')
    from time import sleep
    sleep(5)
    quit()
spawnError = False
keyError = False
doorError = False
if not 1 in WorldList:
    spawnError = True
    print('\nMap Missing Spawn')
if not 5 in WorldList:
    keyError = True
    print('\nMap Missing Key')
if not 6 in WorldList:
    doorError = True
    print('\nMap Missing Door')
if doorError == True or spawnError == True or keyError == True:
    from time import sleep
    sleep(5)
    quit()
Icon = pygame.image.load("icon.png")
Pink1 = pygame.image.load("Pink1.png")
Pink2 = pygame.image.load("Pink2.png")
Pink3 = pygame.image.load("Pink3.png")
RedBlock = pygame.image.load("RedBlock.png")
GreenBlock = pygame.image.load("GreenBlock.png")
BrownBlock = pygame.image.load("BrownBlock.png")
YellowBlock = pygame.image.load("YellowBlock.png")
PurpleBlock = pygame.image.load("PurpleBlock.png")
Blue1 = pygame.image.load("Blue1.png")
Blue2 = pygame.image.load("Blue2.png")
Orange1 = pygame.image.load("Orange1.png")
Orange2 = pygame.image.load("Orange2.png")
BlackBlock = pygame.image.load("BlackBlock.png")
Cursor1 = pygame.image.load("Character1.png")
Cursor2 = pygame.image.load("Character2.png")
Cursor3 = pygame.image.load("Character3.png")
Cursor4 = pygame.image.load("Character4.png")

#colors

white = 255,255,255
black = 0,0,0
blue = 0,0,255
red = 255,0,0
green = 0,255,0
orange = 255,150,0
yellow = 255,255,0
purple = 200,0,255
pink = 255,100,180
brown = 100,40,0

deepblue = 127,127,220
gold = 220,200,50
gray = 127,127,127

# Bk R G B Y O Br P Pk W

#base info

pygame.init()
screenWidth = 600
screenHeight = 500
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Block Game Player')
pygame.display.set_icon(Icon)
block = pygame.Surface((20,20))
block.fill(black)
cursor = pygame.Surface((20,20))
cursor.fill(black)
cursor.set_alpha(0)
x = 0
y = 0
iID = 0
for i in WorldList:
    if x == 600:
        x = 0
        y += 20
    if i == 1:
        cX = x
        cY = y
        sX = x
        sY = y
        valIndex = iID
        sID = iID

    x += 20
    iID += 1

if -1 < sX > 281:
    direction = 'right'
else:
    direction = 'left'

cXc = 0
cYc = 0
left = False
right = False
color = black
colorID = 1
Door = False
clock = pygame.time.Clock()
FPS = 6
space = False
jump = False
swim = False
Jround = 0
Font = pygame.font.SysFont("None",int(100))
winTXT = Font.render('You Win!!!',True,white)
Ymove = False
Pb = 750

#Game Loop

while True:

    #Event Check

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        cXc -= 20
                        left = True
                        direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        cXc += 20
                        right = True
                        direction = 'right'
                    if event.key == pygame.K_UP:
                        if WorldList[valIndex] == 4:
                            swim = True
                        elif valIndex + 30 < 750:
                            if (WorldList[valIndex + 30] == 3 or WorldList[valIndex + 30] == 7 or WorldList[valIndex + 30] == 8) and WorldList[valIndex - 30] != 3 and WorldList[valIndex - 30] != 7 and WorldList[valIndex - 30] != 8:
                                jump = True
                                Jround = 0
                                cYc -= 20
                        Ymove = True
                        Ytimer = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        cXc += 20
                        left = False
                    if event.key == pygame.K_RIGHT:
                        cXc -= 20
                        right = False
                    if event.key == pygame.K_UP:
                        cYc = 0
                        swim = False
                        jump = False
                        Ymove = False

    #Movement

    x = 0
    y = 0

    indexID = 0

    screen.fill(white)

    for blockID in WorldList:
        if x == 600:
            x = 0
            y += 20
        if blockID == 2:
            block.set_alpha(0)
            screen.blit(block,(x,y))
            screen.blit(RedBlock,(x,y))
            block.set_alpha(255)
        elif blockID == 3:
            block.set_alpha(0)
            screen.blit(block,(x,y))
            screen.blit(GreenBlock,(x,y))
            block.set_alpha(255)
        elif blockID == 4:
            block.set_alpha(0)
            screen.blit(block,(x,y))
            if WorldList[indexID - 30] == 4:
                screen.blit(Blue2,(x,y))
            else:
                screen.blit(Blue1,(x,y))
            block.set_alpha(255)
        elif blockID == 5:
            block.set_alpha(0)
            screen.blit(block,(x,y))
            screen.blit(YellowBlock,(x,y))
            block.set_alpha(255)
        elif blockID == 6:
            block.set_alpha(0)
            screen.blit(block,(x,y))
            if Door == False:
                screen.blit(Orange1,(x,y))
            else:
                screen.blit(Orange2,(x,y))
            block.set_alpha(255)
        elif blockID == 7:
            block.set_alpha(0)
            screen.blit(block,(x,y))
            screen.blit(BrownBlock,(x,y))
            block.set_alpha(255)
        elif blockID == 8:
            block.set_alpha(0)
            screen.blit(block,(x,y))
            screen.blit(PurpleBlock,(x,y))
            block.set_alpha(255)
        elif blockID == 9:
            block.set_alpha(0)
            screen.blit(block,(x,y))
            if indexID + 30 < 750:
                if WorldList[indexID + 30] == 9:
                    screen.blit(Pink2,(x,y))
                elif WorldList[indexID + 1] == 9:
                    screen.blit(Pink3,(x,y))
                elif WorldList[indexID - 30] == 9:
                    pass
                elif WorldList[indexID - 1] == 9:
                    pass
                else:
                    screen.blit(Pink1,(x,y))
            elif indexID+1 < 750:
                if WorldList[indexID + 1] == 9:
                    screen.blit(Pink3,(x,y))
                elif WorldList[indexID - 30] == 9:
                    pass
                elif WorldList[indexID - 1] == 9:
                    pass
                else:
                    screen.blit(Pink1,(x,y))
            else:
                if WorldList[indexID - 30] == 9:
                    pass
                elif WorldList[indexID - 1] == 9:
                    pass
                else:
                    screen.blit(Pink1,(x,y))

            block.set_alpha(255)
        elif blockID == 1:
            block.set_alpha(0)
            screen.blit(block,(x,y))
            screen.blit(BlackBlock,(x,y))
            block.set_alpha(255)
        if cX == x and cY == y:
            valIndex = indexID
        x += 20
        indexID += 1

    #Cursor

    if jump == True:
        Jround += 1
        if Jround == 4:
            cYc = 0
            jump = False

    if swim == True:
        if WorldList[valIndex] == 4 and (WorldList[valIndex - 30] == 3 or WorldList[valIndex - 30] == 7 or WorldList[valIndex - 30] == 8):
            cYc = 0
        elif WorldList[valIndex] == 4:
            cYc = -20
        elif WorldList[valIndex] == 0 and WorldList[valIndex+30] == 4:
            cYc = 0
        else:
            cYc = 0
            swim = False

    if Ymove == True and jump == False and ((WorldList[valIndex + 30] == 3 or WorldList[valIndex + 30] == 7 or WorldList[valIndex + 30] == 8) and WorldList[valIndex - 30] != 3 and WorldList[valIndex - 30] != 7 and WorldList[valIndex - 30] != 8):
        Ytimer += 1
        if Ytimer == 2:
            jump = True
            Jround = 0
            cYc -= 20
            Ytimer = 0
    elif Ymove == True and swim == False and WorldList[valIndex] == 4:
        swim = True

    if WorldList[valIndex] == 2:
        cX = sX
        cY = sY
        valIndex = sID

    if valIndex + 30 < 750:
        if WorldList[valIndex + 30] != 3 and WorldList[valIndex + 30] != 7 and WorldList[valIndex + 30] != 8 and swim == False:
            cY += 20
            valIndex+=30

    if valIndex - 30 >= 0:
        if WorldList[valIndex] == 7 or WorldList[valIndex] == 3 or WorldList[valIndex] == 8:
            cY -= 20
            valIndex-=30

    if cYc == -20:
        cY += cYc
        valIndex -= 30
    elif cYc == 20:
        cY -= cYc
        valIndex += 30
    if valIndex + 30 < 750:
        if WorldList[valIndex+1] != 3 and WorldList[valIndex+1] != 7 and WorldList[valIndex + 1] != 8 and right == True:
            cX += cXc
            valIndex += 1
    if WorldList[valIndex-1] != 3 and WorldList[valIndex-1] != 7 and WorldList[valIndex-1] != 8 and left == True:
        cX += cXc
        valIndex -= 1
    if Pb < 750:
        WorldList[Pb] = 0
        Pb = 750
    if valIndex + 30 < 750:
        if WorldList[valIndex+30]==8:
            Pb = valIndex+30
    if WorldList[valIndex]==5:
        WorldList[valIndex]=0
        Door = True
    if WorldList[valIndex]==6 and Door==True:
        screen.fill(black)
        screen.blit(winTXT,((screenWidth/2 - winTXT.get_rect().width/2),(screenHeight/2 - winTXT.get_rect().height/2)))
        pygame.display.update()
        clock.tick(1)
        pygame.quit()
        quit()

    if cX < 0:
        cX = 0
    if cX >= screenWidth:
        cX = 580
    if cY < 0:
        cY = 0
    if cY >= 500:
        cY = 480

    screen.blit(cursor,(cX,cY))


    if valIndex + 30 < 750:
        if direction == 'left' and (WorldList[valIndex+30] == 4 and WorldList[valIndex] == 0):
            screen.blit(Cursor4,(cX,cY+12))
        elif direction == 'right' and (WorldList[valIndex+30] == 4 and WorldList[valIndex] == 0):
            screen.blit(Cursor3,(cX,cY+12))
        else:
            if direction == 'left' and (WorldList[valIndex+30] == 7 or WorldList[valIndex+30] == 3 or WorldList[valIndex+30] == 8):
                screen.blit(Cursor2,(cX,cY))
            elif direction == 'right' and (WorldList[valIndex+30] == 7 or WorldList[valIndex+30] == 3 or WorldList[valIndex+30] == 8):
                screen.blit(Cursor1,(cX,cY))
            elif direction == 'left' and WorldList[valIndex+30] != 7 and WorldList[valIndex+30] != 3 and WorldList[valIndex+30] != 8:
                screen.blit(Cursor4,(cX,cY))
            elif direction == 'right' and WorldList[valIndex+30] != 7 and WorldList[valIndex+30] != 3 and WorldList[valIndex+30] != 8:
                screen.blit(Cursor3,(cX,cY))
    if valIndex + 30 >= 750:
        cX = sX
        cY = sY
        valIndex = sID

    #Display Update

    pygame.display.update()
    clock.tick(FPS)