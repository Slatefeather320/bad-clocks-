#They say even a broken clock is right twice a day. They are wrong. This is the original bad clock which started me on my journey of making bad clocks. It randomly decides to add a second or minite offset to itself in such a way that when averaged over a long enough period of time, it shows the correct time, but for every instance you look at it for, it shows the wrong time. Now in glorious comic sans. 

import pygame, datetime, random
window = pygame.display.set_mode((680,130))
pygame.init()
pygame.display.set_caption("Gaslight o'Clock [PWC V0.3]")

font = pygame.font.Font("C:\Windows\Fonts\comic.ttf",100) #freesansbold.ttf
text = font.render("00:00:00 AM", True, (255,255,255))

trolling = True 
moffset = 0
soffset = 0


def drawFrame():
     global text
     window.fill((0,0,0))
     window.blit(text, (0,0))
     pygame.display.update()

def updateText():
    global text, moffset, soffset
    
    pm = False
    now = datetime.datetime.now()
    minute = now.minute
    second = now.second
    hour = now.hour
    if hour > 12:
        hour -= 12
        pm = True

    if trolling:
        if random.randint(0, 60000) == 0:
            soffset += random.randint(-10, 10)
            print("lmao, soffset", soffset)
            window = pygame.display.set_mode((680,130 + soffset))
        if random.randint(0,90000) == 0:
            moffset += random.randint(-5, 5)
            print("lmao, moffset", moffset)
            window = pygame.display.set_mode((680 + moffset,130))
    

    minute = str((now.minute + moffset)%60)
    second = str((now.second + soffset)%60)
    hour = str(hour)
    if pm:
     t = hour + ":" + minute + ":" + second + "PM"
    else:
     t = hour + ":" + minute + ":" + second + "AM"
   
    text = font.render(t, True, (255,255,255))


#active loop 
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
    

   #maingameloop
   drawFrame()
   updateText()
