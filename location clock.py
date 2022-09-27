# this clock shows you how far away you are on the globe from somewhere where it is 12am assuming you are at the equater
import pygame, datetime
window = pygame.display.set_mode((600,200))
pygame.init()
km = 0
font = pygame.font.Font("freesansbold.ttf",100) 
fontsmall = pygame.font.Font("freesansbold.ttf",20)
pygame.display.set_caption("It is 12'o Clock, Please move here")

#active loop 
active = True

def calKM():
    global kmWestward

    #finds the seconds it has been since 12am
    now = datetime.datetime.now()
    nowseconds = (now.hour*3600) + (now.minute*60) + now.second
    
    #finds the ratio then the km of earth that is  
    ratio = nowseconds/86400
    kmWestward = 40075 * ratio

def fixKm():
    global kmWestward, km

    # converts the direction from westward to both ways. Negitive means East, Positive means West 
    if kmWestward > 20037.5:
        km = (40075 - kmWestward) * -1
    else:
        km = kmWestward

def drawFrame():
     global km
     EastWest = ""
     renderText = str(abs(round(km, 1))) + "km"
     text = font.render(renderText, True, (255,255,255))
     window.fill((0,0,0))
     window.blit(text, (0,0))
     
     pygame.draw.line(window,(255,255,255), (150,150),(450,150), 10)
     if km > 0:
         pygame.draw.line(window,(255,255,255), (150,150),(170,130), 10)
         pygame.draw.line(window,(255,255,255), (150,150),(170,170), 10)
         EastWest = "West"
     else:
         pygame.draw.line(window,(255,255,255), (450,150),(430,130), 10)
         pygame.draw.line(window,(255,255,255), (450,150),(430,170), 10)
         EastWest = "East"

     
     text2 = fontsmall.render(EastWest, True, (255,255,255))
     window.blit(text2, (260, 120))
     
     pygame.display.update()

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
    
    
   
   calKM()
   fixKm()
   drawFrame()
