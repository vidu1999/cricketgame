import time
import math
import pygame as py
from tensorflow.python.data.experimental.ops.testing import sleep

py.init()
sc=py.display.set_mode((360,720))
py.display.set_caption("CRICKET 19/20")
ic=py.image.load('cricket.png')
py.display.set_icon(ic)
bgimg=py.image.load('CRGAMEN.png')
ball=py.image.load('cricket (5).png')
bat=py.image.load('cricket-bat (2).png')
player=py.image.load('player.png')
bplayer=py.image.load('cricket (6).png')
wicket=py.image.load('wicket (2).png')
hel=py.image.load('cricket-helmet.png')
bc=py.image.load('cricket-ball (2).png')
font=py.font.Font('freesansbold.ttf',32)
bcX=320
bcY=640
wX=180
wY=360
bgX=0
bgY=0
blX=180
blY=650
btX=180
btY=60
plX=180
plY=650
bplX=205
bplY=20
bmoveY=0
bmoveX=0
btmoveY1=0
btmoveY2=0
btmoveX1=0
btmoveX2=0
plmoveY1=0
plmoveY2=0
plmoveX1=0
plmoveX2=0
bmove=0
score=0
sX=15
sY=50
hX=10
hY=10
bcs=0
bcsX=325
bcsY=675
k=True
def bg():
    sc.blit(bgimg,(bgX,bgY))
def ball1(x,y):
    sc.blit(ball,(x,y))
def bat1(x,y):
    sc.blit(bat,(x,y))
def player1(x,y):
    sc.blit(player,(x,y))
def bplayer1(x, y):
    sc.blit(bplayer, (x, y))
def wicket1(x,y):
    sc.blit(wicket,(x,y))
def score1(x,y):
    score1=font.render(f"{score}",str(score),True,(255,255,255))
    sc.blit(score1,(x,y))
def helme(x,y):
    sc.blit(hel,(x,y))
def bc1(x,y):
    sc.blit(bc,(x,y))
def bcs1(x,y):
    bcs1 = font.render(f"{bcs}", str(bcs), True, (255, 255, 255))
    sc.blit(bcs1,(x,y))
run=True
while run:
    for event in py.event.get():
        if event.type==py.QUIT:
            run=False
        if event.type==py.KEYDOWN:
            if event.key==py.K_UP and k:
               bmoveY=-1
            if event.key==py.K_LEFT and k:
                bmoveX=-0.1
            if event.key==py.K_RIGHT and k:
                bmoveX=0.1
            if event.key==py.K_w:
                btmoveY1=-0.3
            if event.key==py.K_s:
                btmoveY2=0.3
                #bmove += 0.3
            if event.key==py.K_a:
                btmoveX1=-0.3
            if event.key==py.K_d:
                btmoveX2=0.3
            if event.key==py.K_UP and k==False:
               plmoveY1=-1
            if event.key==py.K_DOWN and k==False:
               plmoveY2=1
            if event.key==py.K_LEFT and k==False:
                plmoveX1=-1
            if event.key==py.K_RIGHT and k==False:
                plmoveX2 = 1
        if event.type==py.KEYUP:
            if event.key==py.K_a:
                btmoveX1 = 0
            if event.key==py.K_s:
                btmoveY2 = 0
            if event.key==py.K_w:
                btmoveY1 = 0
            if event.key==py.K_d:
                btmoveX2 = 0

            if event.key==py.K_LEFT:
                plmoveX1 = 0
            if event.key==py.K_RIGHT:
                plmoveX2 = 0
            if event.key==py.K_UP:
                plmoveY1=0
            if event.key==py.K_DOWN:
                plmoveY2 = 0
    if blY < 0 or blY>720 or blX<0 or blX>360:
        bmoveY = 0
        blY = 650
        plY=650
        bmoveX=0
        bmove=0
        blX=180
        plX=180
        score+=1
        k=True
        print(score)


    if btY <= 0 or btY>=720 or btX<0 or btX>360:
        btmoveY = 0
        btY = 60
        btmoveX=0
        btX=180
        bplY=20
        bplX=205
    if (btX-20)<=blX<=(btX+20) and (btY-20)<=blY<=(btY+20):
        if event.type == py.KEYDOWN:
            if event.key == py.K_s:
                bmove += 0.3
            if event.key == py.K_a:
                bmove += 0.3
            if event.key == py.K_d:
                btmoveX2 = 0.3
        bmove = 1
        bmoveY = 0
        bcs+=1
        k=False
    if k==True and blY==650:
        plX+=bmoveX
    if (plX-10)<=blX<=(plX+10) and (plY-10)<=blY<=(plY+10) and k==False:
        blX=plX
        blY=plY
        blY = 650
        plY = 650
        blX = 180
        plX = 180
        bmove = 0
        k = True
        time.sleep(1)
    if 120<blX and blX<220 and blY<=40:
        wicket1(wX,wY)

        blY = 650
        blX = 180
        py.display.update()
        time.sleep(2)
        score=0
        bcs+=1
        bcs=0
        score1(sX,sY)
        py.display.update()
        bmoveY=0
        bmoveX=0
        btmoveY = 0
        btmoveX = 0

    blY += bmoveY
    blY += bmove
    blX+=bmoveX
    btY += btmoveY1
    btY += btmoveY2
    btX += btmoveX1
    btX += btmoveX2
    plX+=plmoveX1
    plX+=plmoveX2
    plY+= plmoveY1
    plY += plmoveY2
    bplY += btmoveY1
    bplY += btmoveY2
    bplX += btmoveX1
    bplX += btmoveX2
    bg()
    ball1(blX,blY)
    score1(sX, sY)
    bplayer1(bplX,bplY)
    bat1(btX, btY)
    player1(plX,plY)
    helme(hX,hY)
    bc1(bcX,bcY)
    bcs1(bcsX,bcsY)
    py.display.update()
