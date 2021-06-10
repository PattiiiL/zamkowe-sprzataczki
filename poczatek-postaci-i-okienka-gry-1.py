import pygame
import math
from os import path

pygame.init()

screen = pygame.display.set_mode((430,460))

pygame.display.set_caption("Castle cleaners")


working_dir1 = path.dirname(__file__)
protag_Img = pygame.image.load(path.join(working_dir1, 'protag.png')).convert()

working_dir2 = path.dirname(__file__)
background_Img = pygame.image.load(path.join(working_dir2, 'castle.jpg')).convert()


protagX = 180
protagY = 340
protagX_change = 0
protagY_change = 0

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)

scoreX = 20
scoreY = 170

roomX = 200
roomY = 1

game_overX = 120
game_overY = 200

def protag(x,y):
    protag_Img.set_colorkey(0, 0)
    screen.blit(protag_Img,(x,y))

def show_score(x,y):
    score = font.render("You've cleaned the room!", True, (0,0,0))
    screen.blit(score, (x,y))

def collisionTrue(protagX,protagY,roomX,roomY):
    distance = math.sqrt((math.pow(roomX-protagX,2)) + (math.pow(roomY-protagY,2)))
    if distance < 25:
        return True
    else:
        return False

def show_game_over(x,y):
    game_over = font.render("GAME OVER", True, (0,0,0))
    screen.blit(game_over, (x,y))


running = True
while running:
    screen.blit(background_Img,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                protagX_change = -10
                if collision:
                    protagX_change = 0
            if event.key == pygame.K_RIGHT:
                protagX_change = 10
                if collision:
                    protagX_change = 0
            if event.key == pygame.K_UP:
                protagY_change = -10
                if collision:
                    protagY_change = 0
            if event.key == pygame.K_DOWN:
                protagY_change = 10
                if collision:
                    protagY_change = 0
        if event.type == pygame.KEYUP:
            if event.type == pygame.KEYDOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                protagX_change = 0
                protagY_change = 0

        protagX += protagX_change
        protagY += protagY_change

        if protagX <= 0:
            protagX = 0
        elif protagX >= 365:
            protagX = 365

        if protagY <= 0:
            protagY = 0
        elif protagY >= 355:
            protagY = 355


    collision = collisionTrue(protagX,protagY,roomX,roomY)
    if collision:
        show_score(scoreX,scoreY)
        show_game_over(game_overX,game_overY)

    protag(protagX,protagY)

    pygame.display.update()
