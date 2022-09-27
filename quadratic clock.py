#in my opinion the weakest of the bad clocks i have made, this clock outputs the time as a quadratic equation with the coefficient of x being the hour and the roots being the minutes and seconds
import pygame, datetime, time
pygame.init()
window = pygame.display.set_mode((600,100))
font = pygame.font.Font("freesansbold.ttf",65) 


def makeQuad():
    now = datetime.datetime.now()
    
    hour = now.hour
    minute = now.minute
    second = now.second

    rootsSum = minute + second
    rootProduct = minute * second
    k = hour

    quad = str(k) + "x² - " + str(k*rootsSum) + "x + " + str(k*rootProduct)
    return quad 

def drawFrame(renderText):
    
    text = font.render(renderText, True, (255,255,255))
    window.fill((0,0,0))
    window.blit(text, (0,0))
    pygame.display.update()

#active loop 
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
    

   
   drawFrame(makeQuad())
   time.sleep(0.9)
