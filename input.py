import pygame, sys, os,tkinter
from pygame.locals import *
from tkinter import *
from Select import main_menu
namefile =""
money = ""
def enter_text(x1,y1,x2,y2,Background,function,max_length, lower = False, upper = False, title = False):
    global namefile,money
    BLUE = (0,0,255)
    pressed = ""
    finished = False
    click = False
    allowed_chars = [chr(i) for i in range(97, 123)] +\
                    [chr(i) for i in range(48,58)] +\
                    [chr(i) for i in range(65,90)]
    allowed_chars_Money = [chr(i) for i in range(48,58)]
    while not finished:
        button_go = pygame.Rect(x1,y1,x2,y2)     
        mx, my = pygame.mouse.get_pos()
        if button_go.collidepoint((mx, my)):
            if click:
                if Background == BackGround_Cost:
                    money = pressed
                    function(namefile,money)
                else:
                    namefile = pressed
                    if os.path.isfile(namefile) == False:
                        file = open(namefile, "a+")
                        file.write("None")
                        if tail(file, 1) == "None":
                            file.write("\n")
                            file.write("10000")
                            file.write("\n")
                        file.close()
                    function(namefile,money,0)
        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == KEYUP:
                if event.type == K_RETURN:
                    click = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # if input is in list of allowed characters, add to variable
            elif event.type == KEYUP and pygame.key.name(event.key) in \
               allowed_chars and len(pressed) < max_length and Background == BackGround_Name:
                pressed += pygame.key.name(event.key)
            elif event.type == KEYUP and pygame.key.name(event.key) in \
               allowed_chars_Money and len(pressed) < max_length and Background == BackGround_Cost:
                pressed += pygame.key.name(event.key)
            # otherwise, only the following are valid inputs
            elif event.type == KEYUP:
                if event.key == K_BACKSPACE:
                    pressed = pressed[:-1]
                elif event.key == K_SPACE:
                    pressed += " "
        if Background == BackGround_Cost:
            print_text(Background,font, 280, 310, pressed)
        else:
            print_text(Background,font, 420, 335, pressed)
        pygame.display.update()
    # perform any selected string operations
    if lower: pressed = pressed.lower()
    if upper: pressed = pressed.upper()
    if title: pressed = pressed.title()
    return pressed
def print_text(Background,font, x, y, text, color = (0,0,0)):
    """Draws a text image to display surface"""
    text_image = font.render(text, True, color)
    screen.blit(Background,pygame.Rect(0,0,1250,700))
    screen.blit(text_image, (x,y))
pygame.init()
screen = pygame.display.set_mode((1250,700))
BackGround_Cost = pygame.transform.scale(pygame.image.load("background/stake amount.png"),(1250,700))
BackGround_Name = pygame.transform.scale(pygame.image.load("background/loginname.png"),(1250,700))
BackGround_mainmenu2 = pygame.transform.scale(pygame.image.load("background/mainmenu2.png"),(1250,700))
BackGround = pygame.transform.scale(pygame.image.load("background/Background_Menu.jpg"),(1250,700))
font = pygame.font.Font('8-BIT WONDER.TTF', 30)
fpsclock = pygame.time.Clock()
fps = 30
Score = ""
BLUE = (0,0,255)
def tail(f, n):
    assert n >= 0
    pos, lines = n+1, []
    while len(lines) <= n:
        try:
            f.seek(-pos, 2)
        except IOError:
            f.seek(0)
            break
        finally:
            lines = list(f)
        pos *= 2
    return lines[-n]
def history(namefile,money,score):
    click = False
    screen.blit(BackGround,pygame.Rect(0,0,1250,700))
    while True:
        screen.blit(font.render("Loading... ", True, (225,225,225)), (400,350))
        button_back = pygame.Rect(  1000 , 500, 300, 30)
        screen.blit(font.render("Back", True, (225,225,225)), (1000,500))
        mx, my = pygame.mouse.get_pos()
        if button_back.collidepoint((mx, my)):
            screen.blit(font.render("Back", True, (0,0,225)), (1000,500))
            if click:
                mainmenu2(namefile,money,score)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        fpsclock.tick(fps)
def mainmenu2(namefile,money,score):
    screen = pygame.display.set_mode((1250,700))
    screen.blit(BackGround_mainmenu2,pygame.Rect(0,0,1250,700))
    file = open(namefile, "a+")
    t = tail(file,1)
    Score = int(t)+ score
    file.write(str(Score))
    t = tail(file,1)
    file.write("\n")
    file.close()
    from Select import Output_Money
    Output_Money(t)
    click = False
    while True:
        button_minigame = pygame.Rect(100,100,300,530)
        button_playgame = pygame.Rect(500,100,255,530)
        button_history = pygame.Rect(900,100,250,530)
        mx, my = pygame.mouse.get_pos()
        if button_minigame.collidepoint((mx, my)):
            if click:
                from minigame import Run
                Run(namefile,money)
        if button_playgame.collidepoint((mx, my)):
            if click:
                Input_Cost()
        if button_history.collidepoint((mx, my)):
            if click:
                history(namefile,money,score)
        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
def Input_Cost():
    name = False
    global namefile
    t = ""
    while True:
        pressed = None
        file = open(namefile, "a+")
        t = tail(file,1)
        file.close()
        from Select import Output_Money
        Output_Money("1000")
        for event in pygame.event.get():
            if event.type == KEYUP:
                print(pygame.key.name(event.key))
                print(ord(pygame.key.name(event.key)))
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if not name:
            name = enter_text(max_length =7,title = True,x1=510,y1=400,x2=210,y2=210,Background = BackGround_Cost,function = main_menu)
        pygame.display.update()
        fpsclock.tick(fps)
def Input_Name():
    global namefile
    name = False
    while True:
        pressed = None
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if not name:
            name = enter_text(max_length =18,title = True,x1=1035,y1=315,x2=70,y2=70,Background = BackGround_Name,function = mainmenu2)
        pygame.display.update()
        fpsclock.tick(fps)