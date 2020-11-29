import pygame
from pygame.locals import *

# main
# initialize pygame
pygame.init()
gameDisplay = pygame.display.set_mode((860,500))
pygame.display.set_caption('SampleA')

clock = pygame.time.Clock()


# create images
font = pygame.font.Font('freesansbold.ttf', 30) 


# make text
spanish = font.render('Spanish', True, (0,0,0))
french = font.render('French', True, (0,0,0))

# create variables to check which lanuage check box are pressed
spanishOn = False
frenchOn = False

# create checkboxes 
spanishCheck = Rect(180, 95, 20, 20)
frenchCheck = Rect(550, 95, 20, 20)





# create color ovals
# color tuple, number, location
class color:
    def __init__(self, name, color,  TargetLocation, TargetSurface, rectx, recty, errorTimeConst = 30):
        self.errorTimeConst = errorTimeConst
        self.errorTime = 0
        self.TargetLocation = TargetLocation
        self.name = name
        self.TargetSurface = TargetSurface
        self.rectx = rectx
        self.recty = recty
        self.surface = pygame.Surface((rectx, recty))
        if (name != "white"):
            self.surface.fill((255,255,255))
        

        pygame.draw.ellipse(self.surface, color, Rect(0, 0, rectx, recty))
        font = pygame.font.Font('freesansbold.ttf', 30) 
        if (name != "black"):
            word = font.render(name, True, (0,0,0))
        else:
            word = font.render(name, True, (255, 255, 255))
        # blit word to the center of the image
        self.surface.blit(word, (rectx //2 - word.get_width() // 2, recty//2 - word.get_height() // 2 ))


    def paste(self):
        self.TargetSurface.blit(self.surface, self.TargetLocation)
        if (self.errorTime > 0):
            self.errorTime -= 1
            gameDisplay.blit(self.error, (280, 51))
        elif (self.errorTime <= 0):
            self.error = font.render('', True, (0,0,0))
            gameDisplay.blit(self.error, (280, 51))

    def clicked(self, point, spanishOn, frenchOn):
        testRect = Rect(self.TargetLocation, (self.rectx, self.recty))
        if (testRect.collidepoint(point)):
            if (spanishOn and frenchOn):
                # spanishOn true and frenchOn true

                # create error message


                self.errorTime = self.errorTimeConst
                self.error = font.render('Only select one language!', True, (0,0,0))
                print("Only select one language!")

            elif(not spanishOn and not frenchOn):
                # spanishOn false and frenchOn false



                self.errorTime = self.errorTimeConst
                self.error = font.render('Select your language!', True, (0,0,0))
                print("Select your language!")
            else:
                if(spanishOn):
                    pygame.mixer.music.load('SoundEffects/' + self.name + '-spanish.mp3')
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load('SoundEffects/' + self.name + '-french.mp3')
                    pygame.mixer.music.play()

colorNameList = [('black' , (0,0,0)), ('red', (255,0,0)), ('green', (0,255,0)), ('pink', (255,192,203)), ('yellow', (255,255,0)), ('orange', (255,165,0)), ('blue', (0,0,255)), ('brown', (165,42,42)), ('white',(255, 255, 255))]

ovalList = []
counter = 0
# for i in colorNameList:
#     counter += 1
#     ovalList.append(color(i[0], i[1], (ovalx, ovaly), gameDisplay))
#     ovalx += 100
#     if (counter % 3 ==0):
#         ovaly += 50

# Nested Loop
rectx = 150
recty = 100
ovaly = 150
for j in range(3):
    ovalx = 207
    for i in range(3):
        ovalList.append(color(colorNameList[j*3 + i][0], colorNameList[j*3 + i][1], (ovalx, ovaly), gameDisplay, rectx, recty))
        ovalx += rectx
    ovaly += recty
    
    

# go code
crashed = False
while not crashed:
    for event in pygame.event.get():
        gameDisplay.fill((255,255,255))



        

        # display text
        gameDisplay.blit(spanish, (207, 91))
        gameDisplay.blit(french, (575, 91))

        
        if event.type == pygame.QUIT or \
            (event.type == KEYDOWN and event.key == K_ESCAPE):
            crashed = True

        if event.type == MOUSEBUTTONDOWN: 
            
            x, y = event.pos
            # check if checkboxes were clicked
            if (spanishCheck.collidepoint(x, y)):
                spanishOn = not spanishOn
            if (frenchCheck.collidepoint(x, y)):
                frenchOn = not frenchOn

            for i in ovalList:
                # check colors clicked
                i.clicked((x, y), spanishOn, frenchOn)

        
        # draw checkboxes based on if they have been checked or not
        if (frenchOn):
            pygame.draw.rect(gameDisplay, (0,0,0), frenchCheck)
        else:
            pygame.draw.rect(gameDisplay, (0,0,0), frenchCheck, 3)
        if (spanishOn):
            pygame.draw.rect(gameDisplay, (0,0,0), spanishCheck)
        else:
            pygame.draw.rect(gameDisplay, (0,0,0), spanishCheck, 3)

        
        for i in ovalList:
            # display colors
            i.paste()

            # check if clicked


        

        # verbose
        
        # print(event)


    
    pygame.display.update()

    # 60 fps
    clock.tick(60)
    

# end program
pygame.quit()
quit()