import pygame, sys,random
from game_main import Game_Run
from game_main import Game_Run_Set5
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Let's go Turtle")
screen = pygame.display.set_mode((1250, 700),0,32)
cacuoc =''
nv1 = ''
nv2 = ''
nv3 = ''
nv4 = ''
nv5 = ''
nv6 = ''
checkset5 = False
background_image = pygame.image.load("background/background.jpg").convert() 
allsets = pygame.image.load("background/allsets.png").convert()
length_bg = pygame.image.load("background/length.png").convert()
set1_bg = pygame.image.load("background/turtle.png").convert() 
set2_bg = pygame.image.load("background/car.png").convert()
set3_bg = pygame.image.load("background/larva.png").convert() 
set4_bg = pygame.image.load("background/pokemon.png").convert()  
set5_bg = pygame.image.load("background/members.png").convert() 
Background_Money = pygame.transform.scale(pygame.image.load("background/background_money.png"),(300,40))   
font = pygame.font.Font('8-BIT WONDER.TTF', 30)
filename =""
Money = ""
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
def main_menu(namefile,money):
    global filename,Money
    filename = namefile
    Money = money
    while True:
        screen.blit(background_image, [0, 0])
        Output_Money(Money)
        draw_text('Select set', font, (255, 255, 255), screen, 50, 400)
        draw_text('Back', font, (255, 255, 255), screen, 50, 500)   
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(50, 400, 280, 50)
        button_2 = pygame.Rect(50, 500, 130, 50)
        if button_1.collidepoint((mx, my)):
            draw_text('Select set', font, (0, 255, 255), screen, 50, 400)
            if click:
                set()
        if button_2.collidepoint((mx, my)):
            draw_text('Back', font, (0, 255, 255), screen, 50, 500)
            if click:
                from input import Input_Cost
                Input_Cost()    
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
# Option 1 - Select character set
def set():
    click = False
    running = True
    while running:
        screen.blit(allsets, [0, 0])
        Output_Money(Money)
        mx, my = pygame.mouse.get_pos()
        # Click box
        button_11 = pygame.Rect(  0 , 245, 210, 210)
        button_12 = pygame.Rect(260 , 245, 210, 210)
        button_13 = pygame.Rect(520 , 245, 210, 210)
        button_14 = pygame.Rect(780 , 245, 210, 210)
        button_15 = pygame.Rect(1040, 245, 210, 210)
        if button_11.collidepoint((mx, my)):
            draw_text('[      ]', font, (238, 165, 3), screen, 52, 464)
            if click:
                set_1()
        if button_12.collidepoint((mx, my)):
            draw_text('[    ]', font, (238, 165, 3), screen, 316, 464)
            if click:
                set_2()
        if button_13.collidepoint((mx, my)):
            draw_text('[      ]', font, (238, 165, 3), screen, 571, 464)  
            if click:
                set_3()
        if button_14.collidepoint((mx, my)):
            draw_text('[         ]', font, (238, 165, 3), screen, 805, 464) 
            if click:
                set_4()
        if button_15.collidepoint((mx, my)):
            draw_text('[             ]', font, (238, 165, 3), screen, 1022, 464) 
            if click:
                set_5()  
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                main_menu(filename,Money)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True  
        pygame.display.update()
        mainClock.tick(60)
# Option 2 - Back to Start-menu
def back():   
    main_menu(filename,Money)      
# Set 1 - Turtles
def set_1():
    click = False
    running = True
    global nv1, nv2,nv3,nv4,nv5,cacuoc,checkset5
    checkset5 = False
    while running:
        screen.blit(set1_bg, [0, 0])   
        Output_Money(Money)
        mx, my = pygame.mouse.get_pos()
        # Click box
        button_11 = pygame.Rect(  0 , 245, 210, 210)
        button_12 = pygame.Rect(260 , 245, 210, 210)
        button_13 = pygame.Rect(520 , 245, 210, 210)
        button_14 = pygame.Rect(780 , 245, 210, 210)
        button_15 = pygame.Rect(1040, 245, 210, 210)
        if button_11.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 22, 490)
            if click:
                player = pygame.image.load("character/set1/rua1.png").convert() 
                cacuoc = "character/set1/rua1.png"
                trans()
        if button_12.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 282, 490)
            if click:
                player = pygame.image.load("character/set1/rua2.png").convert()
                cacuoc = "character/set1/rua2.png"
                trans()
        if button_13.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 542, 490)  
            if click:
                player = pygame.image.load("character/set1/rua3.png").convert()
                cacuoc = "character/set1/rua3.png"
                trans()
        if button_14.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 802, 490) 
            if click:
                player = pygame.image.load("character/set1/rua4.png").convert()
                cacuoc = "character/set1/rua4.png"
                trans()
        if button_15.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 1047, 490) 
            if click:
                player = pygame.image.load("character/set1/rua5.png").convert()
                cacuoc = "character/set1/rua5.png"
                trans()
        click = False
        nv1 = "character/set1/rua1.png"
        nv2 = "character/set1/rua2.png"
        nv3 = "character/set1/rua3.png"
        nv4 = "character/set1/rua4.png"
        nv5 = "character/set1/rua5.png"
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                set()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
# Set 2 - Cars
def set_2():
    click = False
    running = True
    global nv1, nv2,nv3,nv4,nv5,cacuoc,checkset5
    checkset5 = False
    while running:
        screen.blit(set2_bg, [0, 0])   
        Output_Money(Money)
        mx, my = pygame.mouse.get_pos()
        # Click box
        button_11 = pygame.Rect(  0 , 245, 210, 210)
        button_12 = pygame.Rect(260 , 245, 210, 210)
        button_13 = pygame.Rect(520 , 245, 210, 210)
        button_14 = pygame.Rect(780 , 245, 210, 210)
        button_15 = pygame.Rect(1040, 245, 210, 210)
        if button_11.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 22, 490)
            if click:
                player = pygame.image.load("character/set2/xe1.png").convert()
                cacuoc = "character/set2/xe1.png"
                trans()
        if button_12.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 282, 490)
            if click:
                player = pygame.image.load("character/set2/xe2.png").convert()
                cacuoc = "character/set2/xe2.png"
                trans()
        if button_13.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 542, 490)  
            if click:
                player = pygame.image.load("character/set2/xe3.png").convert()
                cacuoc = "character/set2/xe3.png"
                trans()
        if button_14.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 802, 490) 
            if click:
                player = pygame.image.load("character/set2/xe4.png").convert()
                cacuoc = "character/set2/xe4.png"
                trans()
        if button_15.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 1047, 490) 
            if click:
                player = pygame.image.load("character/set2/xe5.png").convert()
                cacuoc = "character/set2/xe5.png"
                trans()
        nv1 = "character/set2/xe1.png"
        nv2 = "character/set2/xe2.png"
        nv3 = "character/set2/xe3.png"
        nv4 = "character/set2/xe4.png"
        nv5 = "character/set2/xe5.png"
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                set()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
# Set 3 - Larvas
def set_3():
    click = False
    running = True
    global nv1, nv2,nv3,nv4,nv5,cacuoc,checkset5
    checkset5 = False
    while running:
        screen.blit(set3_bg, [0, 0])   
        Output_Money(Money)
        mx, my = pygame.mouse.get_pos()
        # Click box
        button_11 = pygame.Rect(  0 , 245, 210, 210)
        button_12 = pygame.Rect(260 , 245, 210, 210)
        button_13 = pygame.Rect(520 , 245, 210, 210)
        button_14 = pygame.Rect(780 , 245, 210, 210)
        button_15 = pygame.Rect(1040, 245, 210, 210)
        if button_11.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 22, 490)
            if click:
                player = pygame.image.load("character/set3/larva1.png").convert()
                cacuoc = "character/set3/larva1.png"
                trans()
        if button_12.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 282, 490)
            if click:
                player = pygame.image.load("character/set3/larva2.png").convert()
                cacuoc = "character/set3/larva2.png"
                trans()
        if button_13.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 542, 490)  
            if click:
                player = pygame.image.load("character/set3/larva3.png").convert()
                cacuoc = "character/set3/larva3.png"
                trans()
        if button_14.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 802, 490) 
            if click:
                player = pygame.image.load("character/set3/bug1.png").convert()
                cacuoc = "character/set3/bug1.png"
                trans()
        if button_15.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 1047, 490) 
            if click:
                player = pygame.image.load("character/set3/bug2.png").convert()
                cacuoc = "character/set3/bug2.png"
                trans()
        nv1 = "character/set3/larva1.png"
        nv2 = "character/set3/larva2.png"
        nv3 = "character/set3/larva3.png"
        nv4 = "character/set3/bug1.png"
        nv5 = "character/set3/bug2.png"
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                set()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
# Set 4 - Pokemons
def set_4():
    click = False
    running = True
    global nv1, nv2,nv3,nv4,nv5,cacuoc,checkset5
    checkset5 = False
    while running:
        screen.blit(set4_bg, [0, 0])   
        Output_Money(Money)
        mx, my = pygame.mouse.get_pos()
        # Click box
        button_11 = pygame.Rect(  0 , 245, 210, 210)
        button_12 = pygame.Rect(260 , 245, 210, 210)
        button_13 = pygame.Rect(520 , 245, 210, 210)
        button_14 = pygame.Rect(780 , 245, 210, 210)
        button_15 = pygame.Rect(1040, 245, 210, 210)
        if button_11.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 22, 490)
            if click:
                player = pygame.image.load("character/set4/munchiax.png").convert()
                cacuoc = "character/set4/munchiax.png"
                trans()
        if button_12.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 282, 490)
            if click:
                player = pygame.image.load("character/set4/ibui.png").convert()
                cacuoc = "character/set4/ibui.png"
                trans()
        if button_13.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 542, 490)  
            if click:
                player = pygame.image.load("character/set4/pikachu.gif").convert()
                cacuoc = "character/set4/pikachu.gif"
                trans()
        if button_14.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 802, 490) 
            if click:
                player = pygame.image.load("character/set4/emolga.png").convert()
                cacuoc = "character/set4/emolga.png"
                trans()
        if button_15.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 1047, 490) 
            if click:
                player = pygame.image.load("character/set4/rapidash.png").convert()
                cacuoc = "character/set4/rapidash.png"
                trans()
        nv1 = "character/set4/munchiax.png"
        nv2 = "character/set4/ibui.png"
        nv3 = "character/set4/pikachu.gif"
        nv4 = "character/set4/emolga.png"
        nv5 = "character/set4/rapidash.png"
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                set()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
# Set 5 - The Impostors
def set_5():
    click = False
    running = True
    global nv1, nv2,nv3,nv4,nv5,nv6,cacuoc,checkset5
    checkset5 = True
    while running:
        screen.blit(set5_bg, [0, 0])   
        Output_Money(Money)
        mx, my = pygame.mouse.get_pos()
        # Click box
        button_11 = pygame.Rect( 30 , 170, 175, 175)
        button_12 = pygame.Rect(225 , 315, 175, 175)
        button_13 = pygame.Rect(440 , 170, 175, 175)
        button_14 = pygame.Rect(635 , 315, 175, 175)
        button_15 = pygame.Rect(850 , 170, 175, 175)
        button_16 = pygame.Rect(1045, 315, 175, 175)
        if button_11.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 25, 380)
            if click:
                player = pygame.image.load("character/set5/vu.png").convert()
                cacuoc = "character/set5/vu.png"
                trans()
        if button_12.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 225, 520)
            if click:
                player = pygame.image.load("character/set5/quoc.png").convert()
                cacuoc = "character/set5/quoc.png"
                trans()
        if button_13.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 435, 380)  
            if click:
                player = pygame.image.load("character/set5/phong.png").convert()
                cacuoc = "character/set5/phong.png"
                trans()
        if button_14.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 635, 520) 
            if click:
                player = pygame.image.load("character/set5/van.png").convert()
                cacuoc = "character/set5/van.png"
                trans()
        if button_15.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 845, 380) 
            if click:
                player = pygame.image.load("character/set5/phat.png").convert()
                cacuoc = "character/set5/phat.png"
                trans()
        if button_16.collidepoint((mx, my)):
            draw_text('Select', font, (215, 212, 2), screen, 1045, 520) 
            if click:
                player = pygame.image.load("character/set5/loc.png").convert()
                cacuoc = "character/set5/loc.png"
                trans()
        nv1 = "character/set5/vu.png"
        nv2 = "character/set5/quoc.png"
        nv3 = "character/set5/phong.png"
        nv4 = "character/set5/van.png"
        nv5 = "character/set5/phat.png"
        nv6 = "character/set5/loc.png"
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                set()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
# Transection
def trans():
    click1 = False
    while True:
        screen.blit(background_image, [0, 0])
        Output_Money(Money)
        # Display text
        draw_text('Select track length', font, (255, 255, 255), screen, 50, 400)
        draw_text('Back', font, (255, 255, 255), screen, 50, 500)   
        mx, my = pygame.mouse.get_pos()
        # Click box       
        button_1 = pygame.Rect(50, 400, 550, 50)
        button_2 = pygame.Rect(50, 500, 130, 50)
        if button_1.collidepoint((mx, my)):
            draw_text('Select track length', font, (0, 255, 255), screen, 50, 400)
            if click1:
                length()
        if button_2.collidepoint((mx, my)):
            draw_text('Back', font, (0, 255, 255), screen, 50, 500)
            if click1:
                set()    
        click1 = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click1 = True
        pygame.display.update()
        mainClock.tick(60)
def Map(map1,map2,map3,map4):
    temp = random.randint(1,4)
    if temp ==1:
        return map1
    if temp ==2:
        return map2
    if temp ==3:
        return map3
    if temp ==4:
        return map4
# Select race track length
def length():
    click = False
    running = True
    temp =""
    while running:
        screen.blit(length_bg, [0, 0])    
        Output_Money(Money)
        mx, my = pygame.mouse.get_pos()
        # Draw rect
        rect_1 = pygame.Rect(166, 259, 652, 10)
        rect_2 = pygame.Rect(166, 389, 815, 10)
        rect_3 = pygame.Rect(166, 518, 977, 10)
        # Click box
        button_21 = pygame.Rect(25, 220, 90, 90)
        button_22 = pygame.Rect(25, 350, 90, 90)
        button_23 = pygame.Rect(25, 480, 90, 90)
        if button_21.collidepoint((mx, my)):
            pygame.draw.rect(screen, (247, 244, 2), rect_1)
            if click:
                temp = Map("map/Short/map1.1.jpg","map/Short/map2.1.jpg","map/Short/map3.1.jpg","map/Short/map4.1.png")
                if checkset5:
                    Game_Run_Set5(nv1,nv2,nv3,nv4,nv5,nv6,"map/Short/map5.1.png",cacuoc,filename,Money)
                else:
                    Game_Run(nv1,nv2,nv3,nv4,nv5,temp,cacuoc,filename,Money)
                main_menu(filename,Money)
        if button_22.collidepoint((mx, my)):
            pygame.draw.rect(screen, (247, 244, 2), rect_2)
            if click:
                temp = Map("map/Medium/map1.2.jpg","map/Medium/map2.2.jpg","map/Medium/map3.2.jpg","map/Medium/map4.2.png")
                if checkset5:
                    Game_Run_Set5(nv1,nv2,nv3,nv4,nv5,nv6,"map/Medium/map5.2.png",cacuoc,filename,Money)
                else:
                    Game_Run(nv1,nv2,nv3,nv4,nv5,temp,cacuoc,filename,Money)
                main_menu(filename,Money)
        if button_23.collidepoint((mx, my)):
            pygame.draw.rect(screen, (247, 244, 2), rect_3)  
            if click:
                temp = Map("map/Long/map1.3.jpg","map/Long/map2.3.jpg","map/Long/map3.3.jpg","map/Long/map4.3.png")
                if checkset5:
                    Game_Run_Set5(nv1,nv2,nv3,nv4,nv5,nv6,"map/Long/map5.3.png",cacuoc,filename,Money)
                else:
                    Game_Run(nv1,nv2,nv3,nv4,nv5,temp,cacuoc,filename,Money)
                main_menu(filename,Money)   
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                main_menu(filename,Money)
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
def Output_Money(tien):
    screen.blit(Background_Money,[10,5])
    draw_text(tien, font, (0, 0, 0), screen, 80, 6)