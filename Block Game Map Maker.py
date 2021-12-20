#Controls

print('Block Game Map Maker\n\n-------------------------\nControls\n\nMove Cursor: Arrow Keys\nDraw/Erase: Space Bar\nClear Screen: Esc\nChange Material: 0-9\n-------------------------\nMaterial List\n\n[1]Black - Character Spawnpoint(Start here, 1 per map)\n[2]Red - Radioactive Block(Harmful block)\n[3]Green - Grass(Solid block)\n[4]Blue - Water(SWIM!!!)\n[5]Yellow - Key(Opens door, 1 per map)\n[6]Orange - Door(Get here to win, 1 per map)\n[7]Brown - Dirt(Solid block)\n[8]Purple - Disapering Platform(POOF!!!)\n[9]Pink - Decoration(2 stacked = tree, 1 = shrub, 2 beside each other = bush)\n[0]White - Air(aka Eraser)\n-------------------------')

#imports

import pygame, pickle as pic, os, sys

if os.path.exists('WorldList.pickle'):
    WorldOpen = open('WorldList.pickle','rb')
    WorldList = pic.load(WorldOpen)
else:
    WorldList = [0] * 750
    WorldPickle = open('WorldList.pickle','wb')
    pic.dump(WorldList,WorldPickle,2)
    WorldPickle.close()
Icon = pygame.image.load("icon.png")

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
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Block Game Map Maker')
pygame.display.set_icon(Icon)
block = pygame.Surface((20,20))
block.fill(black)
cursor = pygame.Surface((20,20))
cursor.fill(black)
cursor.set_alpha(0)
base = pygame.Surface((600,100))
base.fill(deepblue)
whiteS = pygame.Surface((40,60))
whiteS.fill(white)
pinkS = pygame.Surface((40,60))
pinkS.fill(pink)
purpleS = pygame.Surface((40,60))
purpleS.fill(purple)
brownS = pygame.Surface((40,60))
brownS.fill(brown)
orangeS = pygame.Surface((40,60))
orangeS.fill(orange)
yellowS = pygame.Surface((40,60))
yellowS.fill(yellow)
blueS = pygame.Surface((40,60))
blueS.fill(blue)
greenS = pygame.Surface((40,60))
greenS.fill(green)
redS = pygame.Surface((40,60))
redS.fill(red)
blackS = pygame.Surface((40,60))
blackS.fill(black)
border = pygame.Surface((80,80))
border.fill(gold)
colorSquare = pygame.Surface((60,60))
Font = pygame.font.SysFont("None",int(20))
text1 = Font.render('1',True,white)
text2 = Font.render('2',True,black)
text3 = Font.render('3',True,black)
text4 = Font.render('4',True,black)
text5 = Font.render('5',True,black)
text6 = Font.render('6',True,black)
text7 = Font.render('7',True,black)
text8 = Font.render('8',True,black)
text9 = Font.render('9',True,black)
text0 = Font.render('0',True,black)
cX = 300
cY = 240
cXc = 0
cYc = 0
color = black
colorID = 1
clock = pygame.time.Clock()
FPS = 60
counter = 0
valIndex = 375
space = False

#Game Loop

while True:

    #Event Check

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    WorldPickle = open('WorldList.pickle','wb')
                    pic.dump(WorldList,WorldPickle,2)
                    WorldPickle.close()
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        cXc -= 20
                    if event.key == pygame.K_RIGHT:
                        cXc += 20
                    if event.key == pygame.K_UP:
                        cYc -= 20
                    if event.key == pygame.K_DOWN:
                        cYc += 20
                    if event.key == pygame.K_SPACE:
                        if colorID == 1:
                            if 1 in WorldList:
                                bIndex = WorldList.index(1)
                                WorldList[bIndex] = 0
                        elif colorID == 5:
                            if 5 in WorldList:
                                yIndex = WorldList.index(5)
                                WorldList[yIndex] = 0
                        elif colorID == 6:
                            if 6 in WorldList:
                                oIndex = WorldList.index(6)
                                WorldList[oIndex] = 0
                        WorldList[valIndex] = colorID
                        space = True
                    if event.key == pygame.K_ESCAPE:
                        cWindex = 0
                        for i in WorldList:
                            WorldList[cWindex] = 0
                            cWindex += 1
                    if event.key == pygame.K_1:
                        color = black
                        colorID = 1
                    if event.key == pygame.K_2:
                        color = red
                        colorID = 2
                    if event.key == pygame.K_3:
                        color = green
                        colorID = 3
                    if event.key == pygame.K_4:
                        color = blue
                        colorID = 4
                    if event.key == pygame.K_5:
                        color = yellow
                        colorID = 5
                    if event.key == pygame.K_6:
                        color = orange
                        colorID = 6
                    if event.key == pygame.K_7:
                        color = brown
                        colorID = 7
                    if event.key == pygame.K_8:
                        color = purple
                        colorID = 8
                    if event.key == pygame.K_9:
                        color = pink
                        colorID = 9
                    if event.key == pygame.K_0:
                        color = white
                        colorID = 0
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        cXc = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        cYc = 0
                    if event.key == pygame.K_SPACE:
                        space = False

    #Movement

    if space == True and valIndex != paval:
        if colorID == 1:
            if 1 in WorldList:
                bIndex = WorldList.index(1)
                WorldList[bIndex] = 0
        elif colorID == 5:
            if 5 in WorldList:
                yIndex = WorldList.index(5)
                WorldList[yIndex] = 0
        elif colorID == 6:
            if 6 in WorldList:
                oIndex = WorldList.index(6)
                WorldList[oIndex] = 0
        WorldList[valIndex] = colorID
    x = 0
    y = 0

    indexID = 0
    if counter%12==0:
        cX += cXc
        cY += cYc
    if cX < 0:
        cX = 0
    if cX >= screenWidth:
        cX = 580
    if cY < 0:
        cY = 0
    if cY >= 500:
        cY = 480

    screen.fill(white)
    paval = valIndex

    for blockID in WorldList:
        if x == 600:
            x = 0
            y += 20
        if blockID == 1:
            block.fill(black)
            screen.blit(block,(x,y))
        elif blockID == 2:
            block.fill(red)
            screen.blit(block,(x,y))
        elif blockID == 3:
            block.fill(green)
            screen.blit(block,(x,y))
        elif blockID == 4:
            block.fill(blue)
            screen.blit(block,(x,y))
        elif blockID == 5:
            block.fill(yellow)
            screen.blit(block,(x,y))
        elif blockID == 6:
            block.fill(orange)
            screen.blit(block,(x,y))
        elif blockID == 7:
            block.fill(brown)
            screen.blit(block,(x,y))
        elif blockID == 8:
            block.fill(purple)
            screen.blit(block,(x,y))
        elif blockID == 9:
            block.fill(pink)
            screen.blit(block,(x,y))
        if cX == x and cY == y:
            valIndex = indexID
        x += 20
        indexID += 1

    colorSquare.fill(color)

    screen.blit(base,(0,500))
    screen.blit(whiteS,(550,520))
    screen.blit(pinkS,(500,520))
    screen.blit(purpleS,(450,520))
    screen.blit(brownS,(400,520))
    screen.blit(orangeS,(350,520))
    screen.blit(yellowS,(300,520))
    screen.blit(blueS,(250,520))
    screen.blit(greenS,(200,520))
    screen.blit(redS,(150,520))
    screen.blit(blackS,(100,520))
    screen.blit(border,(10,510))
    screen.blit(colorSquare,(20,520))
    screen.blit(text1,(100,520))
    screen.blit(text2,(150,520))
    screen.blit(text3,(200,520))
    screen.blit(text4,(250,520))
    screen.blit(text5,(300,520))
    screen.blit(text6,(350,520))
    screen.blit(text7,(400,520))
    screen.blit(text8,(450,520))
    screen.blit(text9,(500,520))
    screen.blit(text0,(550,520))

    #Cursor

    screen.blit(cursor,(cX,cY))
    pygame.draw.circle(screen,gray,(cX+10,cY+10),7)

    #Display Update

    pygame.display.update()
    clock.tick(FPS)
    counter+=1
    if counter == 60:
        counter = 0