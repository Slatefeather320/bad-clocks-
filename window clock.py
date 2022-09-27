# this clock uses the lenght of the window it is in to show how many minutes have passed in an hour and the width to show seconds in a minute. Trust me it makes a lot more sense when you run it.
import pygame, datetime, time
x = 500; y = 500
window = pygame.display.set_mode((x,y))
pygame.init()
pygame.display.set_caption("Window Clock")

font = pygame.font.Font("freesansbold.ttf",100) #C:\Windows\Fonts\comic.ttf
text = font.render("00:00:00 AM", True, (255,255,255))

def drawFrame():
     global text, x, y
     window.fill((0,0,0))
     window.blit(text, ((x/2)-100,(y/2)-50))
     pygame.display.update()

def shinanigans():
    global text, x, y

    now = datetime.datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour
    if hour >12:
        hour -= 12
        text = font.render(str(hour) + "pm", True, (255,255,255))
    else:
        text = font.render(str(hour) + "am", True, (255,255,255))

    x = (second-30)*10 + 500
    y = (minute-30)*10 + 500


    window = pygame.display.set_mode((x,y))


#active loop 
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
    

   #maingameloop
   time.sleep(1)
   shinanigans()
   drawFrame()
   
