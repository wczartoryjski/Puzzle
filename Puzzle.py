
import pygame
import os
import random
import time
os.environ['SDL_VIDEO_WINDOW_POS'] ='200,150'

x1="1"
x2="2"
x3="3"
x4="4"
x5="5"
x6="6"
x7="7"
x8="8"
x9="9"
x10="10"
x11="11"
x12="12"
x13="13"
x14="14"
x15="15"
x16=" "
start_gry = -1
start_time=None
czas_gry=0

#timer
clock=pygame.time.Clock()
passed_time=0
timer_started=False

plansza = [[x1,x2,x3,x4],[x5,x6,x7,x8],[x9,x10,x11,x12],[x13,x14,x15,x16]]
lista = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16]
random.shuffle(lista)
num=16
for iter1 in range(0,4):
    for iter2 in range(0,4):
        num-=1      
        plansza[iter1][iter2]=lista[num]

pygame.init()
okno = pygame.display.set_mode([400, 450])
pygame.display.set_caption("Sort Game")
icon=pygame.image.load('cubes.png')
pygame.display.set_icon(icon)
okno.fill([0,0,0])

def display():
    if plansza[0][0]=="1":
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(1,49,98,98))
        okno.blit(napis1, [35,50])
    elif plansza[0][0]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(1,49,98,98))
        okno.blit(napis1, [35,50])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(1,49,98,98))
        if len(str(plansza[0][0]))==1:    
            okno.blit(napis1, [35,50])
        elif plansza[0][0]=="11":
            okno.blit(napis1, [25,50])
        else:
            okno.blit(napis1, [20,50])

    if plansza[0][1]=="2":
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(101,49,98,98))
        okno.blit(napis2, [135,50])
    elif plansza[0][1]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(101,49,98,98))
        okno.blit(napis2, [135,50])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(101,49,98,98))
        if len(str(plansza[0][1]))==1:
            okno.blit(napis2, [135,50])
        elif plansza[0][1]=="11":
            okno.blit(napis2, [125,50])
        else:
            okno.blit(napis2, [120,50])           

    if plansza[0][2]=="3":
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(201,49,98,98))
        okno.blit(napis3, [235,50])
    elif plansza[0][2]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(201,49,98,98))
        okno.blit(napis3, [235,50])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(201,49,98,98))
        if len(str(plansza[0][2]))==1:
            okno.blit(napis3, [235,50])
        elif plansza[0][2]=="11":
            okno.blit(napis3, [225,50])
        else:
            okno.blit(napis3, [220,50])

    if plansza[0][3]=="4":
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(301,49,98,98))
        okno.blit(napis4, [335,50])
    elif plansza[0][3]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(301,49,98,98))
        okno.blit(napis4, [335,50])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(301,49,98,98))
        if len(str(plansza[0][3]))==1:
            okno.blit(napis4, [335,50])
        elif plansza[0][3]=="11":
            okno.blit(napis4, [325,50])
        else:
            okno.blit(napis4, [320,50])

    if plansza[1][0]=="5":        
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(1,149,98,98))
        okno.blit(napis5, [35,150])
    elif plansza[1][0]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(1,149,98,98))
        okno.blit(napis5, [35,150])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(1,149,98,98))
        if len(str(plansza[1][0]))==1:
            okno.blit(napis5, [35,150])
        elif plansza[1][0]=="11":
            okno.blit(napis5, [25,150])
        else:
            okno.blit(napis5, [20,150])

    if plansza[1][1]=="6": 
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(101,149,98,98))
        okno.blit(napis6, [135,150])
    elif plansza[1][1]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(101,149,98,98))
        okno.blit(napis6, [135,150])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(101,149,98,98))
        if len(str(plansza[1][1]))==1:
            okno.blit(napis6, [135,150])
        elif plansza[1][1]=="11":
            okno.blit(napis6, [125,150])
        else:
            okno.blit(napis6, [120,150])          

    if plansza[1][2]=="7": 
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(201,149,98,98))
        okno.blit(napis7, [235,150])
    elif plansza[1][2]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(201,149,98,98))
        okno.blit(napis7, [235,150])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(201,149,98,98))
        if len(str(plansza[1][2]))==1:
            okno.blit(napis7, [235,150])
        elif plansza[1][2]=="11":
            okno.blit(napis7, [225,150])
        else:
            okno.blit(napis7, [220,150])

    if plansza[1][3]=="8": 
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(301,149,98,98))
        okno.blit(napis8, [335,150])
    elif plansza[1][3]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(301,149,98,98))
        okno.blit(napis8, [335,150])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(301,149,98,98))
        if len(str(plansza[1][3]))==1:
            okno.blit(napis8, [335,150])
        elif plansza[1][3]=="11":
            okno.blit(napis8, [325,150])
        else:
            okno.blit(napis8, [320,150])

    if plansza[2][0]=="9": 
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(1,249,98,98))
        okno.blit(napis9, [35,250])
    elif plansza[2][0]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(1,249,98,98))
        okno.blit(napis9, [35,250])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(1,249,98,98))
        if len(str(plansza[2][0]))==1:
            okno.blit(napis9, [35,250])
        elif plansza[2][0]=="11":
            okno.blit(napis9, [25,250])
        else:
            okno.blit(napis9, [20,250])

    if plansza[2][1]=="10": 
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(101,249,98,98))
        okno.blit(napis10, [120,250])
    elif plansza[2][1]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(101,249,98,98))
        okno.blit(napis10, [135,250])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(101,249,98,98))
        if len(str(plansza[2][1]))==1:
            okno.blit(napis10, [135,250])
        elif plansza[2][1]=="11":
            okno.blit(napis10, [125,250])
        else:
            okno.blit(napis10, [120,250])

    if plansza[2][2]=="11": 
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(201,249,98,98))
        okno.blit(napis11, [225,250])
    elif plansza[2][2]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(201,249,98,98))
        okno.blit(napis11, [235,250])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(201,249,98,98))
        if len(str(plansza[2][2]))==1:
            okno.blit(napis11, [235,250])
        elif plansza[2][2]=="11":
            okno.blit(napis11, [225,250])
        else:
            okno.blit(napis11, [220,250])

    if plansza[2][3]=="12": 
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(301,249,98,98))
        okno.blit(napis12, [320,250])
    elif plansza[2][3]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(301,249,98,98))
        okno.blit(napis12, [335,250])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(301,249,98,98))
        if len(str(plansza[2][3]))==1:
            okno.blit(napis12, [335,250])
        elif plansza[2][3]=="11":
            okno.blit(napis12, [325,250])
        else:
            okno.blit(napis12, [320,250])

    if plansza[3][0]=="13": 
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(1,349,98,98))
        okno.blit(napis13, [20,350])
    elif plansza[3][0]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(1,349,98,98))
        okno.blit(napis13, [35,350])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(1,349,98,98))
        if len(str(plansza[3][0]))==1:
            okno.blit(napis13, [35,350])
        elif plansza[3][0]=="11":
            okno.blit(napis13, [25,350])
        else:
            okno.blit(napis13, [20,350])

    if plansza[3][1]=="14": 
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(101,349,98,98))
        okno.blit(napis14, [120,350])
    elif plansza[3][1]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(101,349,98,98))
        okno.blit(napis14, [135,350])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(101,349,98,98))
        if len(str(plansza[3][1]))==1:
            okno.blit(napis14, [135,350])
        elif plansza[3][1]=="11":
            okno.blit(napis14, [125,350])           
        else:
            okno.blit(napis14, [120,350])

    if plansza[3][2]=="15": 
        pygame.draw.rect(okno, [255,0,255], pygame.Rect(201,349,98,98))
        okno.blit(napis15, [220,350])
    elif plansza[3][2]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(201,349,98,98))
        okno.blit(napis15, [235,350])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(201,349,98,98))
        if len(str(plansza[3][2]))==1:
            okno.blit(napis15, [235,350])
        elif plansza[3][2]=="11":
            okno.blit(napis15, [225,350])            
        else:
            okno.blit(napis15, [220,350])

    if plansza[3][3]==" ": 
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(301,349,98,98))
        okno.blit(napis16, [335,350])
    elif plansza[3][3]==" ":
        pygame.draw.rect(okno, [100,100,100], pygame.Rect(301,349,98,98))
        okno.blit(napis16, [335,350])
    else:
        pygame.draw.rect(okno, [0,255,255], pygame.Rect(301,349,98,98))
        if len(str(plansza[3][3]))==1:
            okno.blit(napis16, [335,350])
        elif plansza[3][3]=="11":
            okno.blit(napis16, [325,350])
        else:
            okno.blit(napis16, [320,350])
    pygame.display.update()

pygame.font.init()
czcionka=pygame.font.SysFont("Comic Sans MS",60)
czcionka2=pygame.font.SysFont("Comic Sans MS",30)
czcionka3=pygame.font.SysFont("Comic Sans MS",27)
czcionka4=pygame.font.SysFont("Comic Sans MS",20)

napis1=czcionka.render(plansza[0][0], False, [255,255,255])
napis2=czcionka.render(plansza[0][1], False, [255,255,255])
napis3=czcionka.render(plansza[0][2], False, [255,255,255])
napis4=czcionka.render(plansza[0][3], False, [255,255,255])
napis5=czcionka.render(plansza[1][0], False, [255,255,255])
napis6=czcionka.render(plansza[1][1], False, [255,255,255])
napis7=czcionka.render(plansza[1][2], False, [255,255,255])
napis8=czcionka.render(plansza[1][3], False, [255,255,255])
napis9=czcionka.render(plansza[2][0], False, [255,255,255])
napis10=czcionka.render(plansza[2][1], False, [255,255,255])
napis11=czcionka.render(plansza[2][2], False, [255,255,255])
napis12=czcionka.render(plansza[2][3], False, [255,255,255])
napis13=czcionka.render(plansza[3][0], False, [255,255,255])
napis14=czcionka.render(plansza[3][1], False, [255,255,255])
napis15=czcionka.render(plansza[3][2], False, [255,255,255])
napis16=czcionka.render(plansza[3][3], False, [255,255,255])


druga_gra=0

display()
runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

    if start_gry==-1:     
        pygame.draw.rect(okno, [150,150,150], pygame.Rect(301,2,98,45))
        message4=czcionka3.render("START", False, [255,255,255])
        okno.blit(message4,[305,5])
        pygame.draw.rect(okno,[0,0,0,], pygame.Rect(1,2,148,45))

        if event.type == pygame.MOUSEBUTTONDOWN:   
            cord = pygame.mouse.get_pos()
            x=cord[0]
            y=cord[1] 
            if x>=301 and x<=399 and y>=2 and y<=47: #Wlaczanie gry
                start_gry=start_gry*(-1)
                pygame.draw.rect(okno, [0,0,0], pygame.Rect(301,2,98,45))
                timer_started= not timer_started
                if timer_started:
                    start_time=pygame.time.get_ticks()

    if start_gry==1:     
        pygame.draw.rect(okno, [150,150,150], pygame.Rect(301,2,98,45))
        message8=czcionka4.render("RESTART", False, [255,255,255])
        okno.blit(message8,[305,10])
    
        if event.type==pygame.MOUSEBUTTONDOWN:
            cord = pygame.mouse.get_pos()
            x=cord[0]
            y=cord[1]
            if x>=301 and x<=399 and y>=2 and y<=47: #restart gry
                start_gry=1
                okno.fill((0,0,0))
                lista = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16]
                random.shuffle(lista)
                num=16
                for iter1 in range(0,4):
                    for iter2 in range(0,4):
                        num-=1      
                        plansza[iter1][iter2]=lista[num]
                napis1=czcionka.render(plansza[0][0], False, [255,255,255])
                napis2=czcionka.render(plansza[0][1], False, [255,255,255])
                napis3=czcionka.render(plansza[0][2], False, [255,255,255])
                napis4=czcionka.render(plansza[0][3], False, [255,255,255])
                napis5=czcionka.render(plansza[1][0], False, [255,255,255])
                napis6=czcionka.render(plansza[1][1], False, [255,255,255])
                napis7=czcionka.render(plansza[1][2], False, [255,255,255])
                napis8=czcionka.render(plansza[1][3], False, [255,255,255])
                napis9=czcionka.render(plansza[2][0], False, [255,255,255])
                napis10=czcionka.render(plansza[2][1], False, [255,255,255])
                napis11=czcionka.render(plansza[2][2], False, [255,255,255])
                napis12=czcionka.render(plansza[2][3], False, [255,255,255])
                napis13=czcionka.render(plansza[3][0], False, [255,255,255])
                napis14=czcionka.render(plansza[3][1], False, [255,255,255])
                napis15=czcionka.render(plansza[3][2], False, [255,255,255])
                napis16=czcionka.render(plansza[3][3], False, [255,255,255])
                display()
                start_time=None
                #restartowanie timera
                timer_started=not timer_started
                start_time=None
                passed_time=None
                
                timer_started= not timer_started
                if timer_started:
                    start_time=pygame.time.get_ticks()

    if timer_started:
        passed_time=pygame.time.get_ticks() - start_time        

    if start_time and start_gry==1:
        pygame.draw.rect(okno,[0,0,0,], pygame.Rect(1,2,148,45))
        czas_gry2=f"Czas: {str(passed_time//1000)} s"
        message6=czcionka3.render(czas_gry2,True,[255,255,255])
        okno.blit(message6,[5,5])
        pygame.display.update()
        
    if event.type == pygame.MOUSEBUTTONDOWN and start_gry==1:
        cord = pygame.mouse.get_pos()
        x=cord[0]
        y=cord[1]
        if x>=1 and x<= 99 and y>=49 and y<=148: #pierwszy wiersz
            if plansza[0][1]==" ":
                plansza[0][1]=plansza[0][0]
                plansza[0][0]=" "
            elif plansza[1][0]==" ":
                plansza[1][0]=plansza[0][0]
                plansza[0][0]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=101 and x<= 199 and y>=49 and y<=148:
            if plansza[0][2]==" ":
                plansza[0][2]=plansza[0][1]
                plansza[0][1]=" "
            elif plansza[1][1]==" ":
                plansza[1][1]=plansza[0][1]
                plansza[0][1]=" "
            elif plansza[0][0]==" ":
                plansza[0][0]=plansza[0][1]
                plansza[0][1]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=201 and x<= 299 and y>=49 and y<=148:
            if plansza[0][3]==" ":
                plansza[0][3]=plansza[0][2]
                plansza[0][2]=" "
            elif plansza[1][2]==" ":
                plansza[1][2]=plansza[0][2]
                plansza[0][2]=" "
            elif plansza[0][1]==" ":
                plansza[0][1]=plansza[0][2]
                plansza[0][2]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=301 and x<= 399 and y>=49 and y<=148:
            if plansza[1][3]==" ":
                plansza[1][3]=plansza[0][3]
                plansza[0][3]=" "
            elif plansza[0][2]==" ":
                plansza[0][2]=plansza[0][3]
                plansza[0][3]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()        
            pygame.display.flip()

        if x>=1 and x<= 99 and y>=149 and y<=248: #drugi wiersz
            if plansza[0][0]==" ":
                plansza[0][0]=plansza[1][0]
                plansza[1][0]=" "
            elif plansza[1][1]==" ":
                plansza[1][1]=plansza[1][0]
                plansza[1][0]=" "
            elif plansza[2][0]==" ":
                plansza[2][0]=plansza[1][0]
                plansza[1][0]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=101 and x<= 199 and y>=149 and y<=248:
            if plansza[0][1]==" ":
                plansza[0][1]=plansza[1][1]
                plansza[1][1]=" "
            elif plansza[1][2]==" ":
                plansza[1][2]=plansza[1][1]
                plansza[1][1]=" "
            elif plansza[2][1]==" ":
                plansza[2][1]=plansza[1][1]
                plansza[1][1]=" "
            elif plansza[1][0]==" ":
                plansza[1][0]=plansza[1][1]
                plansza[1][1]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=201 and x<= 299 and y>=149 and y<=248:
            if plansza[0][2]==" ":
                plansza[0][2]=plansza[1][2]
                plansza[1][2]=" "
            elif plansza[1][3]==" ":
                plansza[1][3]=plansza[1][2]
                plansza[1][2]=" "
            elif plansza[2][2]==" ":
                plansza[2][2]=plansza[1][2]
                plansza[1][2]=" "
            elif plansza[1][1]==" ":
                plansza[1][1]=plansza[1][2]
                plansza[1][2]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=301 and x<= 399 and y>=149 and y<=248:
            if plansza[2][3]==" ":
                plansza[2][3]=plansza[1][3]
                plansza[1][3]=" "
            elif plansza[1][2]==" ":
                plansza[1][2]=plansza[1][3]
                plansza[1][3]=" "
            elif plansza[0][3]==" ":
                plansza[0][3]=plansza[1][3]
                plansza[1][3]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()   

        if x>=1 and x<= 99 and y>=249 and y<=348: #trzeci wiersz
            if plansza[1][0]==" ":
                plansza[1][0]=plansza[2][0]
                plansza[2][0]=" "
            elif plansza[2][1]==" ":
                plansza[2][1]=plansza[2][0]
                plansza[2][0]=" "
            elif plansza[3][0]==" ":
                plansza[3][0]=plansza[2][0]
                plansza[2][0]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=101 and x<= 199 and y>=249 and y<=348:
            if plansza[1][1]==" ":
                plansza[1][1]=plansza[2][1]
                plansza[2][1]=" "
            elif plansza[2][2]==" ":
                plansza[2][2]=plansza[2][1]
                plansza[2][1]=" "
            elif plansza[3][1]==" ":
                plansza[3][1]=plansza[2][1]
                plansza[2][1]=" "
            elif plansza[2][0]==" ":
                plansza[2][0]=plansza[2][1]
                plansza[2][1]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=201 and x<= 299 and y>=249 and y<=348:
            if plansza[1][2]==" ":
                plansza[1][2]=plansza[2][2]
                plansza[2][2]=" "
            elif plansza[2][3]==" ":
                plansza[2][3]=plansza[2][2]
                plansza[2][2]=" "
            elif plansza[3][2]==" ":
                plansza[3][2]=plansza[2][2]
                plansza[2][2]=" "
            elif plansza[2][1]==" ":
                plansza[2][1]=plansza[2][2]
                plansza[2][2]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=301 and x<= 399 and y>=249 and y<=348:
            if plansza[1][3]==" ":
                plansza[1][3]=plansza[2][3]
                plansza[2][3]=" "
            elif plansza[3][3]==" ":
                plansza[3][3]=plansza[2][3]
                plansza[2][3]=" "
            elif plansza[2][2]==" ":
                plansza[2][2]=plansza[2][3]
                plansza[2][3]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()  

        if x>=1 and x<= 99 and y>=349 and y<=448: #czwarty wiersz
            if plansza[2][0]==" ":
                plansza[2][0]=plansza[3][0]
                plansza[3][0]=" "
            elif plansza[3][1]==" ":
                plansza[3][1]=plansza[3][0]
                plansza[3][0]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=101 and x<= 199 and y>=349 and y<=448:
            if plansza[3][0]==" ":
                plansza[3][0]=plansza[3][1]
                plansza[3][1]=" "
            elif plansza[2][1]==" ":
                plansza[2][1]=plansza[3][1]
                plansza[3][1]=" "
            elif plansza[3][2]==" ":
                plansza[3][2]=plansza[3][1]
                plansza[3][1]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=201 and x<= 299 and y>=349 and y<=448:
            if plansza[3][1]==" ":
                plansza[3][1]=plansza[3][2]
                plansza[3][2]=" "
            elif plansza[2][2]==" ":
                plansza[2][2]=plansza[3][2]
                plansza[3][2]=" "
            elif plansza[3][3]==" ":
                plansza[3][3]=plansza[3][2]
                plansza[3][2]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip()
        if x>=301 and x<= 399 and y>=349 and y<=448:
            if plansza[2][3]==" ":
                plansza[2][3]=plansza[3][3]
                plansza[3][3]=" "
            elif plansza[3][2]==" ":
                plansza[3][2]=plansza[3][3]
                plansza[3][3]=" "
            napis1=czcionka.render(plansza[0][0], False, [255,255,255])
            napis2=czcionka.render(plansza[0][1], False, [255,255,255])
            napis3=czcionka.render(plansza[0][2], False, [255,255,255])
            napis4=czcionka.render(plansza[0][3], False, [255,255,255])
            napis5=czcionka.render(plansza[1][0], False, [255,255,255])
            napis6=czcionka.render(plansza[1][1], False, [255,255,255])
            napis7=czcionka.render(plansza[1][2], False, [255,255,255])
            napis8=czcionka.render(plansza[1][3], False, [255,255,255])
            napis9=czcionka.render(plansza[2][0], False, [255,255,255])
            napis10=czcionka.render(plansza[2][1], False, [255,255,255])
            napis11=czcionka.render(plansza[2][2], False, [255,255,255])
            napis12=czcionka.render(plansza[2][3], False, [255,255,255])
            napis13=czcionka.render(plansza[3][0], False, [255,255,255])
            napis14=czcionka.render(plansza[3][1], False, [255,255,255])
            napis15=czcionka.render(plansza[3][2], False, [255,255,255])
            napis16=czcionka.render(plansza[3][3], False, [255,255,255])
            display()
            pygame.display.flip() 
    #w razie zwyciestwa
    if (
        plansza[0][0]=="1" 
        and plansza[0][1]=="2" 
        and plansza[0][2]=="3" 
        and plansza[0][3]=="4" 
        and plansza[1][0]=="5" 
        and plansza[1][1]=="6" 
        and plansza[1][2]=="7" 
        and plansza[1][3]=="8"
        and plansza[2][0]=="9"
        and plansza[2][1]=="10"
        and plansza[2][2]=="11"
        and plansza[2][3]=="12"
        and plansza[3][0]=="13"
        and plansza[3][1]=="14"
        and plansza[3][2]=="15"
        and plansza[3][3]==" "
        and start_gry==1
    ):
        end_time=pygame.time.get_ticks()
        czas_gry=pygame.time.get_ticks() - end_time
        czas_gry_ostateczny=(passed_time - czas_gry)//1000
        #odczytywanie starego wyniku
        results = open("results.txt","r")
        najlepszy_wynik=results.read()
        stary_wynik=int(najlepszy_wynik)
        results.close()

        if stary_wynik==0:
            najlepszy_wynik=czas_gry_ostateczny
            results = open("results.txt", "w")
            results.write(str(najlepszy_wynik))
            results.close()
            
            #aktualizacja odczytu z pliku
            results = open("results.txt","r")
            najlepszy_wynik=results.read()
            stary_wynik=int(najlepszy_wynik)
            results.close()
        

        if czas_gry_ostateczny < stary_wynik and stary_wynik > 0 and czas_gry_ostateczny>0:
            najlepszy_wynik=czas_gry_ostateczny
            results = open("results.txt", "w")
            results.write(str(najlepszy_wynik))
            results.close()
            
            #aktualizacja odczytu z pliku
            results = open("results.txt","r")
            najlepszy_wynik=results.read()
            stary_wynik=int(najlepszy_wynik)
            results.close()


        #wyswietlany komunikat po zwyciestwie
        pygame.draw.rect(okno, [0,0,255], pygame.Rect(20,120,360,180))
        zwyciestwo=czcionka.render("Zwycięstwo!", False, [255,255,0])
        okno.blit(zwyciestwo, [35,120])

        wynik=czcionka2.render("Twój wynik:", False, [255,255,255])
        okno.blit(wynik,[75,200])

        czas=czcionka2.render(f"{czas_gry_ostateczny} s", False, [255,255,255])
        okno.blit(czas,[280,200])

        message5=czcionka2.render("Najlepszy wynik:", False, [255,255,255])
        okno.blit(message5,[55,240])

        message7=czcionka2.render(f"{najlepszy_wynik} s", False, [255,255,255])
        okno.blit(message7,[300,240])

        druga_gra=1
        start_gry=-1
        
        #restartowanie timera
        timer_started=not timer_started
        start_time=None
        passed_time=None


        if event.type == pygame.MOUSEBUTTONDOWN:
            cord = pygame.mouse.get_pos()
            x=cord[0]
            y=cord[1] 
            if x>=301 and x<=399 and y>=2 and y<=47: #Wlaczanie gry
                start_gry=1
                okno.fill((0,0,0))
                lista = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16]
                random.shuffle(lista)
                num=16
                for iter1 in range(0,4):
                    for iter2 in range(0,4):
                        num-=1      
                        plansza[iter1][iter2]=lista[num]
                napis1=czcionka.render(plansza[0][0], False, [255,255,255])
                napis2=czcionka.render(plansza[0][1], False, [255,255,255])
                napis3=czcionka.render(plansza[0][2], False, [255,255,255])
                napis4=czcionka.render(plansza[0][3], False, [255,255,255])
                napis5=czcionka.render(plansza[1][0], False, [255,255,255])
                napis6=czcionka.render(plansza[1][1], False, [255,255,255])
                napis7=czcionka.render(plansza[1][2], False, [255,255,255])
                napis8=czcionka.render(plansza[1][3], False, [255,255,255])
                napis9=czcionka.render(plansza[2][0], False, [255,255,255])
                napis10=czcionka.render(plansza[2][1], False, [255,255,255])
                napis11=czcionka.render(plansza[2][2], False, [255,255,255])
                napis12=czcionka.render(plansza[2][3], False, [255,255,255])
                napis13=czcionka.render(plansza[3][0], False, [255,255,255])
                napis14=czcionka.render(plansza[3][1], False, [255,255,255])
                napis15=czcionka.render(plansza[3][2], False, [255,255,255])
                napis16=czcionka.render(plansza[3][3], False, [255,255,255])
                display()
                #okno.blit(message5,[305,10]) 
                start_time=None
                
                timer_started= not timer_started
                if timer_started:
                    start_time=pygame.time.get_ticks()

    pygame.display.update()