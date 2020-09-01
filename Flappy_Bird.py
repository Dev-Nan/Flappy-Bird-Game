import pygame
import random
pygame.init()
screen=pygame.display.set_mode((397,500))
img11=pygame.image.load("12n1pipe.png")
img22=pygame.image.load("12rn1pipe.png")
birdimg=pygame.image.load("bird.png")
back=pygame.image.load("bk1.jpg")
game_over=pygame.image.load("game_over.jpg")
img0=pygame.image.load("0.png")
img1=pygame.image.load("1.png")
img2=pygame.image.load("2.png")
img3=pygame.image.load("3.png")
img4=pygame.image.load("4.png")
img5=pygame.image.load("5.png")
img6=pygame.image.load("6.png")
img7=pygame.image.load("7.png")
img8=pygame.image.load("8.png")
img9=pygame.image.load("9.png")
birdy=100
birdx=100
upar=0
pipex=400
countt=1
n11=0
n22=0
n33=0
n44=0
passed=0
listt=[150,260,340]
pipeh2=[-190,-190,-100]
pipeh1=[450,400,475]
def show_score(n1,n2,n3,n4):
    if n1==0:
        screen.blit(img0,(198,40))
    if n1==1:
        screen.blit(img1,(198,40))
    if n1==2:
        screen.blit(img2,(198,40))
    if n1==3:
        screen.blit(img3,(198,40))
    if n1==4:
        screen.blit(img4,(198,40))
    if n1==5:
        screen.blit(img5,(198,40))
    if n1==6:
        screen.blit(img6,(198,40))
    if n1==7:
        screen.blit(img7,(198,40))
    if n1==8:
        screen.blit(img8,(198,40))
    if n1==9:
        screen.blit(img9,(198,40))
    if n2==0:
        screen.blit(img0,(220,40))
    if n2==1:
        screen.blit(img1,(220,40))
    if n2==2:
        screen.blit(img2,(220,40))
    if n2==3:
        screen.blit(img3,(220,40))
    if n2==4:
        screen.blit(img4,(220,40))
    if n2==5:
        screen.blit(img5,(220,40))
    if n2==6:
        screen.blit(img6,(220,40))
    if n2==7:
        screen.blit(img7,(220,40))
    if n2==8:
        screen.blit(img8,(220,40))
    if n2==9:
        screen.blit(img9,(220,40))
    if n3==0:
        screen.blit(img0,(176,40))
    if n3==1:
        screen.blit(img1,(176,40))
    if n3==2:
        screen.blit(img2,(176,40))
    if n3==3:
        screen.blit(img3,(176,40))
    if n3==4:
        screen.blit(img4,(176,40))
    if n3==5:
        screen.blit(img5,(176,40))
    if n3==6:
        screen.blit(img6,(176,40))
    if n3==7:
        screen.blit(img7,(176,40))
    if n3==8:
        screen.blit(img8,(176,40))
    if n3==9:
        screen.blit(img9,(176,40))
    if n4==0:
        screen.blit(img0,(154,40))
    if n4==1:
        screen.blit(img1,(154,40))
    if n4==2:
        screen.blit(img2,(154,40))
    if n4==3:
        screen.blit(img3,(154,40))
    if n4==4:
        screen.blit(img4,(154,40))
    if n4==5:
        screen.blit(img5,(154,40))
    if n4==6:
        screen.blit(img6,(154,40))
    if n4==7:
        screen.blit(img7,(154,40))
    if n4==8:
        screen.blit(img8,(154,40))
    if n4==9:
        screen.blit(img9,(154,40))
    
def bak():
    screen.blit(back,(0,0))
def bird(x1,y1):
    screen.blit(birdimg,(x1,y1))
def show(lo,y,yy):
    for i in range(len(lo)):
        screen.blit(img11,(lo[i],y[i]))
        screen.blit(img22,(lo[i],yy[i]))
def change(li):
    for i in range(len(li)):
        li[i]-=1
    if li[0]==0:
        del li[0]
        del pipeh1[0]
        del pipeh2[0]
        li.append(340)
        pipeyy=-(random.randrange(0,230,10))
        pipeh2.append(pipeyy)
        pipey=random.randrange(280,490,20)
        pipeh1.append(pipey)
        global passed
        passed=1
        pygame.mixer.music.load("point.wav")
        pygame.mixer.music.play(0)
    return li
run=True
while run:
    screen.fill((0,0,0))
    bak()
    for k in pygame.event.get():
        if k.type==pygame.QUIT:
            run=False
        if k.type==pygame.KEYDOWN:
            if countt==1:
                pygame.mixer.music.load("wing.wav")
                pygame.mixer.music.play(0)
            if k.key==pygame.K_UP:
                upar=-1
            if k.key==pygame.K_DOWN:
                upar=1
        if k.type==pygame.KEYUP:
            if countt==1:
                pygame.mixer.music.load("swoosh.wav")
                pygame.mixer.music.play(0)
            if k.key==pygame.K_UP:
                upar=-1
            if k.key==pygame.K_DOWN:
                upar=1
    if countt==0:
        upar=0
    birdy+=upar
    if birdy<=0:
        birdy=0
    if birdy>=466:
        birdy=466
    if countt==1:
        bird(birdx,birdy)
        listt=change(listt)
        show(listt,pipeh1,pipeh2)
    if ((((birdy+34)>=pipeh1[0] or (birdy<=(230+pipeh2[0]))) and (listt[0]<birdx and listt[0]>(birdx-57))) or (birdy==0 or birdy==466)):
        if(countt==1):
            pygame.mixer.music.load("hit.wav")
            pygame.mixer.music.play(0)
        countt=0
    if countt==0:
        screen.blit(game_over,(0,0))
        passed=0
    show_score(n11,n22,n33,n44)
    if passed==1:
        n22+=1
        if n22==10:
            n22=0
            n11+=1
            if n11==10:
                n11=0
                n33+=1
                if n33==10:
                    n33=0
                    n44+=1
        passed=0
    pygame.display.update()


