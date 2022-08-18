import sys, os, pygame, random,time
from Select import draw_text
mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1250,700))
font = pygame.font.Font('8-BIT WONDER.TTF',30)
BackGround = pygame.transform.scale(pygame.image.load("background/Background_Menu.jpg"),(1250,700))
BackGround_Credit = pygame.transform.scale(pygame.image.load("background/background_credits.png"),(1250,700))
pygame.display.set_caption('Let''s go Turtle')
click = False
count=0
def credit():
    click = False
    while True:
        screen.blit(BackGround_Credit,(0,0))
        button_back = pygame.Rect(  1000 , 500, 300, 30)
        draw_text('Back', font, (225,225,225), screen, 1000, 500)
        mx, my = pygame.mouse.get_pos()
        if button_back.collidepoint((mx, my)):
            draw_text('Back', font, (225,225,0), screen, 1000, 500)
            if click:
                menu()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
def menu():
    pygame.mixer.init()
    pygame.mixer.music.load("Music/BackgroundMusic.mp3")
    pygame.mixer.music.play()
    while True:
        screen.blit(BackGround,(0,0))
        draw_text('Main menu', font, (0,0,255), screen, 100, 300)
        draw_text('Start Game', font, (225,225,225), screen, 100, 400)
        draw_text('Credits', font, (225,225,225), screen, 100, 500)
        button_startgame = pygame.Rect(  100 , 400, 300, 30)
        button_credit = pygame.Rect(100 , 500, 200, 30)
        mx, my = pygame.mouse.get_pos()
        if button_startgame.collidepoint((mx, my)):
                draw_text('Start Game', font, (225,225,0), screen, 100, 400)
                if click:
                    from input import Input_Name
                    Input_Name()
        if button_credit.collidepoint((mx, my)):
            draw_text('Credits', font, (225,225,0), screen, 100, 500)
            if click:
                credit()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
menu()