import pygame
import time
import random

pygame.init()

#Screen & Background
Height = 500
Width = 650
screen = pygame.display.set_mode((Width,Height))
CloudsHeight = 85
Clouds = pygame.image.load("Imagens/NuvenSol.xcf")
Clouds = pygame.transform.scale(Clouds, (Width, CloudsHeight))
FenceHeight = 50
FenceWidth = 1300
Fence = pygame.image.load("Imagens/Fence.xcf")
Fence.set_colorkey([255,0,255])
Fence = pygame.transform.scale(Fence, (FenceWidth, FenceHeight))
FPS = 60

# ------------------------------------------------- Plane --------------------------------------------------
HeightP = 65
WidthP = 95
landed = False
StationaryPlane = [
    pygame.image.load("Imagens/TAPs.xcf"),

    ]
StationaryPlane = list(map(lambda x:pygame.transform.scale(x, (WidthP, HeightP)), StationaryPlane))
StationaryPlane[0].set_colorkey([255,0,255])
AnimatedPlane = [
pygame.image.load("Imagens/TAP.xcf"),
pygame.image.load("Imagens/TAP1.xcf"),
pygame.image.load("Imagens/TAP2.xcf"),
    ]
AnimatedPlane = list(map(lambda x:pygame.transform.scale(x, (WidthP, HeightP)), AnimatedPlane))
for surface in AnimatedPlane:
    surface.set_colorkey([255,0,255])
AviaoVelocidadeY = 4

# ------------------------------------------------- Obstacles --------------------------------------------------

BarnBirdHeight = 35
BarnBirdWidth = 35
BarnBird = pygame.image.load("Imagens/BarnBird.xcf")
BarnBird = pygame.transform.scale(BarnBird, (BarnBirdWidth, BarnBirdHeight))
BarnBird.set_colorkey([255,0,255])

BarnHeight = 150
BarnWidth = 190
Barn= pygame.image.load("Imagens/Barn.xcf")
Barn = pygame.transform.scale(Barn, (BarnWidth, BarnHeight))
Barn.set_colorkey([255,0,255])

TowerHeight = 215
TowerWidth = 45
AnimatedTower = [
    pygame.image.load("Imagens/Torre.xcf"),
    pygame.image.load("Imagens/Torre1.xcf"),
    pygame.image.load("Imagens/Torre2.xcf")
]
AnimatedTower = list(map(lambda x: pygame.transform.scale(x, (TowerWidth, TowerHeight)), AnimatedTower))
for surface in AnimatedTower:
    surface.set_colorkey([255,0,255])

CrashUpwards = 50
CrashDownwards = 80
ObstacleSpeed = 2
########################################################################################################################################################################################

test1 = pygame.image.load("Imagens/testeverde.xcf")
test1 = pygame.transform.scale(test1, (BarnBirdWidth, BarnBirdHeight))



# ------------------- Fonts --------------------------------------------------
arcadeFontPath = r"C:/Users/danie/.spyder-py3/Projeto FP/Fonts/ARCADECLASSIC.ttf"
arial = 'arial'

def time_convert(sec): #!!!!!!!!!!!!!!!!!!!! milisegundos !!!!!!!!!!!!!!!!!!!
  '''The time that will be displayed on the game'''
  mins = sec // 60
  secs = sec % 60
  hours = mins // 60
  ms = sec
  mins = mins % 60
  time = "Time          " + str(hours) + "  " + str(mins) + "  " + str(secs) 
  return time
    
def drawText(texto,x,y,fontPath,size,color, bool):
    '''A function that draws every text through it's path on the game'''
    pygame.font.init()
    if bool:
        font = pygame.font.Font(fontPath,size)
    else:
        font = pygame.font.SysFont(fontPath, size)
    a_escrever = font.render(texto,True,color)
    screen.blit(a_escrever, (x,y))

def draw(indiceAnimado, AnimatedPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, scoreText): #Bool for omitting Score & Time
    screen.fill([103,164,67])
    screen.blit(Clouds , (0,0))
    screen.blit(Fence, (fence.x, fence.y))
    screen.blit(AnimatedPlane[indiceAnimado],(aviao.x,aviao.y))
    screen.blit(AnimatedTower[indiceAnimado], (torre.x,torre.y))
    screen.blit(Barn, (celeiro.x, celeiro.y))
    screen.blit(BarnBird, (celeiroBird.x, celeiroBird.y))
    if scoreText:
        drawText("Score      " + str(score),0,0,arcadeFontPath,30,'green', True)
        drawText(str(time_convert(lapsed_time)),0,30,arcadeFontPath,30,'green', True)

def crash(startingY, aviao, torre, celeiro, celeiroUp, celeiroDown, score, lapsed_time, fence, indiceAnimado, UpDown, FrontBack, celeiroBird, aviaoFront, aviaoBack):
    if UpDown == "Up":  
        if FrontBack == "Front":
            while aviao.y > startingY - CrashUpwards:
                aviao.y -= 10
                aviaoBack.y -= 10
                aviaoFront.y -= 10
                fence.x -= ObstacleSpeed * 2
                celeiro.x -= ObstacleSpeed * 2
                celeiroUp.x -= ObstacleSpeed * 2
                celeiroDown.x -= ObstacleSpeed * 2
                celeiroBird.x -= ObstacleSpeed * 2
                torre.x -= ObstacleSpeed * 2 
                if fence.x <= -648:
                    fence.x = -324
                draw(indiceAnimado, AnimatedPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, True)
                pygame.display.update()
                pygame.time.delay(15)
                aviao.y += 5
                aviaoBack.y += 5
                aviaoFront.y += 5
                draw(indiceAnimado, AnimatedPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, True)
                pygame.display.update()
                pygame.time.delay(15)
        if FrontBack == "Back":
            while aviao.y > startingY - CrashUpwards:
                aviao.y -= 10
                aviaoBack.y -= 10
                aviaoFront.y -= 10
                torre.x += ObstacleSpeed * 2
                fence.x += ObstacleSpeed * 2
                celeiro.x += ObstacleSpeed * 2
                celeiroUp.x += ObstacleSpeed * 2
                celeiroDown.x += ObstacleSpeed * 2
                celeiroBird.x += ObstacleSpeed * 2
                draw(indiceAnimado, AnimatedPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, True)
                pygame.display.update()
                pygame.time.delay(15)
                aviao.y += 5
                aviaoBack.y += 5
                aviaoFront.y += 5
                draw(indiceAnimado, AnimatedPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, True)
                pygame.display.update()
                pygame.time.delay(15)
    if UpDown == "Down": #Apenas frente
        while aviao.y < startingY + CrashDownwards:
            aviao.y += 10
            aviaoBack.y += 10
            aviaoFront.y += 10
            torre.x -= ObstacleSpeed * 2
            fence.x -= ObstacleSpeed * 2
            celeiroBird.x -= ObstacleSpeed * 2
            if fence.x <= -648:
                fence.x = -324
            celeiro.x -= ObstacleSpeed * 2
            celeiroDown.x -= ObstacleSpeed * 2
            celeiroUp.x -= ObstacleSpeed * 2
            draw(indiceAnimado, AnimatedPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, True)
            pygame.display.update()
            pygame.time.delay(15)
            aviao.y -= 5
            aviaoBack.y -= 5
            aviaoFront.y -= 5
            draw(indiceAnimado, AnimatedPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, True)
            pygame.display.update()
            pygame.time.delay(15)

def landed(celeiro,indiceAnimado,aviao,torre,lapsed_time,score,celeiroBird, fence):
            if indiceAnimado >= len(AnimatedPlane):
                indiceAnimado = 0
            while celeiro.x + BarnWidth > -50:
                celeiro.x -= ObstacleSpeed
                fence.x -= ObstacleSpeed
                celeiroBird.x -= ObstacleSpeed
                if fence.x <= -0:
                    fence.x = -324
                draw(indiceAnimado, AnimatedPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, True)
                pygame.display.update() 
                pygame.time.delay(10)
            while aviao.y + HeightP + FenceHeight < Height:
                aviao.y += 1
                draw(indiceAnimado, AnimatedPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, True)
                pygame.display.update()
                pygame.time.delay(8)
            draw(0, StationaryPlane, aviao, torre, celeiro, score, lapsed_time, fence, celeiroBird,  False)

def menu_text(levels, choice):
    drawText("SPACEBAR     TO     PLAY!", 55, CloudsHeight, arcadeFontPath, 60, 'green', True)
    drawText("LEVEL     SELECTION       X", (Width/2)-200, (Height/2)-30, arcadeFontPath, 30, 'green', True)
    drawText('  -"  "', 371, 210, arial, 40, 'green', False)
    drawText("-",(Width/2)-220,(Height/2)-40, arial, 40, 'green', False)
    drawText("Level %s     %s    points    to    win!" %(levels[choice][0], levels[choice][1]), (Width/2)-200, Height/2+50, arcadeFontPath, 30, 'green', True)
    drawText("-",(Width/2)-220,(Height/2)+40, arial, 40, 'green', False)
    drawText("=",(Width/2)-90,(Height/2)+45, arial, 35, 'green', False)

def mainloop(test1):
    lapsed_time = 0
    stationary  = True
    levels = [(1,10), (2,15), (3,25)]
    choice = 0
    score = levels[choice][1]

    aviao = pygame.Rect(10, (Height - HeightP - FenceHeight ), WidthP, HeightP)
    aviaoFront = pygame.Rect(10 + WidthP/2, (Height- HeightP - FenceHeight), WidthP/2, HeightP)
    aviaoBack = pygame.Rect(10, (Height- HeightP - FenceHeight), WidthP/2, HeightP/2 )

    celeiro = pygame.Rect(Width, (Height-BarnHeight-FenceHeight), BarnWidth, BarnHeight)
    celeiroUp = pygame.Rect(Width+65, (Height-FenceHeight-BarnHeight), BarnWidth-65, 10) #Cima
    celeiroDown = pygame.Rect(Width+55, (Height-BarnHeight-FenceHeight+10), BarnWidth-55, 5) #Baixo
    celeiroBird = pygame.Rect(Width, (Height-FenceHeight-BarnHeight-BarnBirdHeight),  BarnBirdWidth, BarnBirdHeight)
    celeiroPontos = pygame.Rect(Width+(BarnWidth/2), (Height-BarnHeight-FenceHeight+50), BarnWidth/2, BarnHeight) #Pontos

    torre = pygame.Rect( -TowerWidth, (Height-TowerHeight-FenceHeight), TowerWidth, TowerHeight)
    fence = pygame.Rect(0 ,Height-FenceHeight, FenceWidth,FenceHeight)

    Speed = pygame.time.Clock()
    SpeedBoost = 1
    indiceAnimado = -1

    run = True
    while run:
        Speed.tick(FPS)
        while stationary:
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        stationary = False
                        run = False
                    if event.type == pygame.KEYUP:
                        if keys_pressed[pygame.K_SPACE]:
                            stationary = False
                        if keys_pressed[pygame.K_x]:
                            if choice == len(levels)-1:
                                choice = -1   
                            choice += 1
            draw(0, StationaryPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, False)
            menu_text(levels, choice)
            pygame.display.update()
            score = levels[choice][1]
            start_time = time.time()

        if indiceAnimado >= len(AnimatedPlane):
            indiceAnimado = 0
        
#--------------------------------------------------------------------- REGISTOS DO TECLADO -----------------------------------------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_ESCAPE]:
            mainloop()
        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]) and aviao.y > 85: #Subir
            aviao.y -= AviaoVelocidadeY * SpeedBoost
            aviaoFront.y -= AviaoVelocidadeY * SpeedBoost
            aviaoBack.y -= AviaoVelocidadeY * SpeedBoost
        if (keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]) and aviao.y+HeightP+FenceHeight < Height-2:#Descer
            aviao.y += AviaoVelocidadeY * SpeedBoost
            aviaoFront.y += AviaoVelocidadeY * SpeedBoost
            aviaoBack.y += AviaoVelocidadeY * SpeedBoost
        if keys_pressed[pygame.K_SPACE]:
            SpeedBoost = 2
        else:
            SpeedBoost = 1 

#-------------------------------------------------------------------- OBSTACULOS ---------------------------------------------------------------------

        obstaculos = [celeiro, torre]
        celeiro.x -= ObstacleSpeed * SpeedBoost
        celeiroPontos.x -= ObstacleSpeed * SpeedBoost
        celeiroUp.x -= ObstacleSpeed * SpeedBoost
        celeiroDown.x -= ObstacleSpeed * SpeedBoost
        torre.x -= ObstacleSpeed * SpeedBoost
        fence.x -= ObstacleSpeed * SpeedBoost
        celeiroBird.x -= ObstacleSpeed * SpeedBoost

        if fence.x <= -648:
            fence.x = -324
        if celeiro.x + BarnWidth < 0 and torre.x + TowerWidth < 0: #Random Choice put on Width
            obstaculo = random.choice(obstaculos)
            if obstaculo == celeiro:
                celeiroPontos.x = Width+(BarnWidth/2)
                celeiroUp.x = Width+65
                celeiroDown.x = Width+55
                celeiroBird.x = Width
            obstaculo.x = Width

#------------------------------------------------------------------------------ Colisões -----------------------------------------------------
        if aviao.colliderect(celeiroPontos):#PONTOS
            celeiroPontos.x = -BarnWidth
            score -= 1

        if aviaoBack.colliderect(celeiroBird):
            startingY = aviao.y
            crash(startingY, aviao, torre, celeiro, celeiroUp, celeiroDown, score, lapsed_time, fence, indiceAnimado, "Up", "Front", celeiroBird,aviaoFront,aviaoBack)
        elif aviaoFront.colliderect(celeiroBird):
            startingY = aviao.y
            crash(startingY, aviao, torre, celeiro, celeiroUp, celeiroDown, score, lapsed_time, fence, indiceAnimado, "Up", "Back", celeiroBird,aviaoFront,aviaoBack)
        elif aviaoFront.colliderect(celeiroDown):#BAIXO CELEIRO -Front
            startingY = aviao.y
            crash(startingY, aviao, torre, celeiro, celeiroUp, celeiroDown, score, lapsed_time, fence, indiceAnimado, "Down", "Front", celeiroBird,aviaoFront,aviaoBack)
        elif aviaoBack.colliderect(celeiroDown):#BAIXO CELEIRO - Back
            startingY = aviao.y
            crash(startingY, aviao, torre, celeiro, celeiroUp, celeiroDown, score, lapsed_time, fence, indiceAnimado, "Down", "Front", celeiroBird,aviaoFront,aviaoBack)
        elif aviaoFront.colliderect(celeiroUp):#CIMA CELEIRO - Front
            startingY = aviao.y
            crash(startingY, aviao, torre, celeiro, celeiroUp, celeiroDown, score, lapsed_time, fence, indiceAnimado, "Up", "Front", celeiroBird,aviaoFront,aviaoBack)
        elif aviaoBack.colliderect(celeiroUp):#CIMA CELEIRO - Back
            startingY = aviao.y
            crash(startingY, aviao, torre, celeiro, celeiroUp, celeiroDown, score, lapsed_time, fence, indiceAnimado, "Up", "Front", celeiroBird,aviaoFront,aviaoBack)

        if aviaoFront.colliderect(torre):
            startingY = aviao.y
            crash(startingY, aviao, torre, celeiro, celeiroUp, celeiroDown, score, lapsed_time, fence, indiceAnimado, "Up", "Back", celeiroBird,aviaoFront,aviaoBack)
        elif aviaoBack.colliderect(torre):
            startingY = aviao.y
            crash(startingY, aviao, torre, celeiro, celeiroUp, celeiroDown, score, lapsed_time, fence, indiceAnimado, "Up", "Front", celeiroBird,aviaoFront,aviaoBack)


#------------------------------------------------------------------------------ DESENHAR --------------------------------------------------
        draw(indiceAnimado, AnimatedPlane, aviao, torre, celeiro, score, lapsed_time, fence,celeiroBird, True)


        #Width+75, (Height-FenceHeight-BarnHeight), BarnWidth-75, 10
        test1 = pygame.transform.scale(test1, (BarnWidth-65, 10))
        screen.blit(test1, (celeiroUp.x,celeiroUp.y))

        if pygame.time.get_ticks() % 3 == 0 and SpeedBoost == 1:
            indiceAnimado += 1

        if pygame.time.get_ticks() % 2 == 0 and SpeedBoost != 1:
                indiceAnimado += 1
#----------------------------------------------------------------------------- Fim do Jogo ------------------------------------------------
        if score == 0:
            landed(celeiro,indiceAnimado,aviao,torre,lapsed_time,score, celeiroBird, fence)
            pygame.display.update()
            pygame.time.delay(1000)
            while run:
                drawText(str(time_convert(lapsed_time)), 200, CloudsHeight, arcadeFontPath, 50, 'green', True)
                drawText("PRESS    R    TO    P LAY    AGAIN", 100, 230, arcadeFontPath, 40, 'green', True)
                drawText("-", 80, 215, arial, 50, 'green', False)
                drawText("PRESS   ESC    TO    LEAVE", 100, 280, arcadeFontPath, 40, 'green', True)
                drawText("-", 80, 265, arial, 50, 'green', False)
                pygame.display.update()
                for event in pygame.event.get():
                    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                        pygame.quit()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if pygame.key.get_pressed()[pygame.K_r]:
                        mainloop()
        end_time = time.time()
        lapsed_time = round((end_time - start_time))
        pygame.display.update()
    pygame.quit()
    
mainloop(test1)