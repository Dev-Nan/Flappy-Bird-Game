import pygame
import random
pygame.init()
# screen variable loads a screen with lenghts x and y 
screen=pygame.display.set_mode((397,500))
# these variables loads images with name and format provided in bracket 
img11=pygame.image.load("bottom_pipe.png")
img22=pygame.image.load("upper_pipe.png")
birdimg=pygame.image.load("bird.png")
back=pygame.image.load("background.jpg")
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
# Y co-ordinate of bird
birdy=100
# X co-ordinate of bird
birdx=100
# it contains displacement of bird in y direction when key is pressed
upar=0
# it is used in some conditional statements for checking collision conditions 
countt=1
# these are used to blit score on screen
n11=0
n22=0
n33=0
n44=0
# checks if bird has passed a pipe or not
passed=0
# list contains X co-ordinate of pipes
pipe_x=[150,260,340]
# two lists contains Y co-ordinate of upper and bottom pipe
pipeh2=[-190,-200,-100]
pipeh1=[450,350,475]
# function is used to show score on screen
def show_score(n4,n3,n2,n1):
    if n4==0:
        screen.blit(img0,(220,40))
    if n4==1:
        screen.blit(img1,(220,40))
    if n4==2:
        screen.blit(img2,(220,40))
    if n4==3:
        screen.blit(img3,(220,40))
    if n4==4:
        screen.blit(img4,(220,40))
    if n4==5:
        screen.blit(img5,(220,40))
    if n4==6:
        screen.blit(img6,(220,40))
    if n4==7:
        screen.blit(img7,(220,40))
    if n4==8:
        screen.blit(img8,(220,40))
    if n4==9:
        screen.blit(img9,(220,40))
    if n3==0:
        screen.blit(img0,(198,40))
    if n3==1:
        screen.blit(img1,(198,40))
    if n3==2:
        screen.blit(img2,(198,40))
    if n3==3:
        screen.blit(img3,(198,40))
    if n3==4:
        screen.blit(img4,(198,40))
    if n3==5:
        screen.blit(img5,(198,40))
    if n3==6:
        screen.blit(img6,(198,40))
    if n3==7:
        screen.blit(img7,(198,40))
    if n3==8:
        screen.blit(img8,(198,40))
    if n3==9:
        screen.blit(img9,(198,40))
    if n2==0:
        screen.blit(img0,(176,40))
    if n2==1:
        screen.blit(img1,(176,40))
    if n2==2:
        screen.blit(img2,(176,40))
    if n2==3:
        screen.blit(img3,(176,40))
    if n2==4:
        screen.blit(img4,(176,40))
    if n2==5:
        screen.blit(img5,(176,40))
    if n2==6:
        screen.blit(img6,(176,40))
    if n2==7:
        screen.blit(img7,(176,40))
    if n2==8:
        screen.blit(img8,(176,40))
    if n2==9:
        screen.blit(img9,(176,40))
    if n1==0:
        screen.blit(img0,(154,40))
    if n1==1:
        screen.blit(img1,(154,40))
    if n1==2:
        screen.blit(img2,(154,40))
    if n1==3:
        screen.blit(img3,(154,40))
    if n1==4:
        screen.blit(img4,(154,40))
    if n1==5:
        screen.blit(img5,(154,40))
    if n1==6:
        screen.blit(img6,(154,40))
    if n1==7:
        screen.blit(img7,(154,40))
    if n1==8:
        screen.blit(img8,(154,40))
    if n1==9:
        screen.blit(img9,(154,40))
# it shows background image on screen
def show_background():
    screen.blit(back,(0,0))
# it shows changing Y Co-ordinate of bird such that it appears moving
def show_y_movement_of_bird(x1,y1):
    screen.blit(birdimg,(x1,y1))
# it shows changing X and Y Co-ordinates of pipes such that it appears moving
def show_moving_pipes(pipe_x,pipeh1,pipeh2):
    for i in range(len(pipe_x)):
        screen.blit(img11,(pipe_x[i],pipeh1[i]))
        screen.blit(img22,(pipe_x[i],pipeh2[i]))
# it changes X Co-ordinates of pipes which is in list and also append a new pipe X when required 
def change_x_of_pipes(pipe_xx):
    for i in range(len(pipe_xx)):
        pipe_xx[i]-=1
    if pipe_xx[0]==0:
        # if pipe X reaches 0 delete it from the lists
        del pipe_xx[0]
        del pipeh1[0]
        del pipeh2[0]
        # append a new pipe in list with given X Co-ordinate
        pipe_xx.append(340)
        # it generates a random Y Co-ordinate for pipe which was appended in the list
        pipeyy=-(random.randrange(0,220,10))
        pipeh2.append(pipeyy)
        pipey=random.randrange(285,500,20)
        pipeh1.append(pipey)
        global passed
        passed=1
        pygame.mixer.music.load("point.wav")
        pygame.mixer.music.play(0)
    return pipe_xx
run=True
while run:
    screen.fill((0,0,0))
    show_background()
    # this loop detects any event happening in pygame 
    for k in pygame.event.get():
        if k.type==pygame.QUIT:
            run=False
        # checking if a key is pressed
        if k.type==pygame.KEYDOWN:
            if countt==1:
                pygame.mixer.music.load("wing.wav")
                pygame.mixer.music.play(0)
            if k.key==pygame.K_UP:
                upar=-1
            if k.key==pygame.K_DOWN:
                upar=1
        # checking if a key is released
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
        show_y_movement_of_bird(birdx,birdy)
        pipe_x=change_x_of_pipes(pipe_x)
        show_moving_pipes(pipe_x,pipeh1,pipeh2)
    # collision condition of bird 
    if ((((birdy+34)>=pipeh1[0] or (birdy<=(230+pipeh2[0]))) and (pipe_x[0]<birdx and pipe_x[0]>(birdx-57))) or (birdy==0 or birdy==466)):
        if(countt==1):
            pygame.mixer.music.load("hit.wav")
            pygame.mixer.music.play(0)
        countt=0
    if countt==0:
        screen.blit(game_over,(0,0))
        passed=0
    show_score(n44,n33,n22,n11)
    # this condition is used change values of variable so that score changes
    if passed==1:
        n44+=1
        if n44==10:
            n44=0
            n33+=1
            if n33==10:
                n33=0
                n22+=1
                if n22==10:
                    n22=0
                    n11+=1
        passed=0
    pygame.display.update()


