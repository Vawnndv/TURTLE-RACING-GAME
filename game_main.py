#inport 
import pygame, random, time, sys, os
from python_phaohoa import main
def Game_Run_Set5(Figure1,Figure2,Figure3,Figure4,Figure5,Figure6,BACKGROUND,CaCuoc,namefile,money):
    pygame.init()
    #load hinh anh
    m =60
    NV1 = pygame.transform.scale(pygame.image.load(Figure1),(m,m))
    NV2 = pygame.transform.scale(pygame.image.load(Figure2),(m,m))
    NV3 = pygame.transform.scale(pygame.image.load(Figure3),(m,m))
    NV4 = pygame.transform.scale(pygame.image.load(Figure4),(m,m))
    NV5 = pygame.transform.scale(pygame.image.load(Figure5),(m,m))
    NV6 = pygame.transform.scale(pygame.image.load(Figure6),(m,m))
    BackGround_Dich = pygame.transform.scale(pygame.image.load(BACKGROUND),(3000,700))
    So1 = pygame.transform.scale(pygame.image.load("background/1.png"),(150,150))
    So2 = pygame.transform.scale(pygame.image.load("background/2.png"),(150,150))
    So3 = pygame.transform.scale(pygame.image.load("background/3.png"),(150,150))
    Start = pygame.transform.scale(pygame.image.load("background/start.png"),(150,150))
    #tao cua so
    gameSurface = pygame.display.set_mode((1250,700))
    pygame.display.set_caption('Let''s go Turtle')
    #mau sac
    red = pygame.Color(255,0,0)
    blue = pygame.Color(65,105,255)
    black = pygame.Color(0,0,0)
    white = pygame.Color(255,255,255)
    gray = pygame.Color(128,128,128)
    #ham Winer
    def Winner():
        gfont = pygame.font.SysFont('8-BIT WONDER.TTF',50)
        gsurf = gfont.render('WINNER ',True,red)
        grect = gsurf.get_rect()
        grect.midtop = (625,250)
        gameSurface.blit(gsurf,grect)
        pygame.display.flip()
        time.sleep(1) #time wait to exit
    def ManHinhBatDau():
        gameSurface.fill(white)
        gameSurface.blit(BackGround_Dich,pygame.Rect(0,0,1250,700))
        gameSurface.blit(NV1,pygame.Rect(n1,230,m,m))
        gameSurface.blit(NV2,pygame.Rect(n2,310,m,m))
        gameSurface.blit(NV3,pygame.Rect(n3,390,m,m))
        gameSurface.blit(NV4,pygame.Rect(n4,470,m,m))
        gameSurface.blit(NV5,pygame.Rect(n5,550,m,m))
        gameSurface.blit(NV6,pygame.Rect(n6,630,m,m))
    #ham dem nguoc
    def Dem_Nguoc():
        ManHinhBatDau()
        gameSurface.blit(So3,pygame.Rect(550,300,250,250))
        pygame.display.flip()
        time.sleep(1)
        ManHinhBatDau()
        gameSurface.blit(So2,pygame.Rect(550,300,250,250))
        pygame.display.flip()
        time.sleep(1)
        ManHinhBatDau()
        gameSurface.blit(So1,pygame.Rect(550,300,250,250))
        pygame.display.flip()
        time.sleep(1)
        ManHinhBatDau()
        gameSurface.blit(Start,pygame.Rect(550,300,500,500))
        pygame.display.flip()
        time.sleep(1)
        ManHinhBatDau()
        pygame.display.flip()
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
    #khai bao bien
    n1 =0
    n2 =0
    n3 =0
    n4 =0
    n5 =0
    n6 =0
    v1=random.randint(5,10)
    v2=random.randint(5,10)
    v3=random.randint(5,10)
    v4=random.randint(5,10)
    v5=random.randint(5,10)
    v6=random.randint(5,10)
    t=0
    kt=0 #kt dieu kien de nv chay
    kt_tung_vn_1=0#kt nhan vat dung lai
    kt_tung_vn_2=0
    kt_tung_vn_3=0
    kt_tung_vn_4=0
    kt_tung_vn_5=0
    kt_tung_vn_6=0
    #kt de nhan vat quay lui
    kt_quaylui_nv_1 =0
    kt_quaylui_nv_2 =0
    kt_quaylui_nv_3 =0
    kt_quaylui_nv_4 =0
    kt_quaylui_nv_5 =0
    kt_quaylui_nv_6 =0
    count_nv_HetQuayLui1 =0
    count_nv_HetQuayLui2 =0
    count_nv_HetQuayLui3 =0
    count_nv_HetQuayLui4 =0
    count_nv_HetQuayLui5 =0
    count_nv_HetQuayLui6 =0
    #kt de dua vo mang
    count=0
    Background_x=0
    dem = -1
    MangNhanVat = [6]
    j=0
    i_win = [0 ]
    i_lose = [1, 2 , 3 , 4, 5]
    #vong lap chin
    pygame.mixer.init()
    pygame.mixer.music.load("Music/nhacdua.mp3")
    pygame.mixer.music.play()
    while pygame.event.Event != pygame.QUIT:  
        if t==0:
            Dem_Nguoc()         
        t=1
        count=count+1
        gameSurface.fill(white)
        gameSurface.blit(BackGround_Dich,pygame.Rect(Background_x,0,1250,700))
        gameSurface.blit(NV1,pygame.Rect(n1,230,m,m))
        gameSurface.blit(NV2,pygame.Rect(n2,310,m,m))
        gameSurface.blit(NV3,pygame.Rect(n3,390,m,m))
        gameSurface.blit(NV4,pygame.Rect(n4,470,m,m))
        gameSurface.blit(NV5,pygame.Rect(n5,550,m,m))
        gameSurface.blit(NV6,pygame.Rect(n6,630,m,m))
        if n1<=625 and n2<=625 and n3<=625 and n4<=625 and n5<=625 and n6<=625 and kt == 0:
            n1=n1+v1
            n2=n2+v2
            n3=n3+v3
            n4=n4+v4
            n5=n5+v5
            n6=n6+v6
        else:
            kt=1
            if Background_x>=-1700:
                Background_x = Background_x -5
                if kt_tung_vn_1 ==0 and kt_tung_vn_2 ==0 and kt_tung_vn_3 ==0 and kt_tung_vn_4 ==0 and kt_tung_vn_5 ==0 and kt_tung_vn_6==0: 
                    vt_vn_1=n1
                    vt_vn_2=n2
                    vt_vn_3=n3
                    vt_vn_4=n4
                    vt_vn_5=n5
                    vt_vn_6=n6
                if (vt_vn_1>=625) and kt_tung_vn_1 ==0:
                    if count<200:
                        n1=n1+random.randint(-30,-10)
                    else:
                        n1=n1+v1
                    if (n2<1150) and (kt_quaylui_nv_2==0):
                        n2=n2+random.randint(-20,30)
                        if (n3<1150) and (kt_quaylui_nv_3==0):
                            n3=n3+random.randint(-20,30)
                            if (n4<1150) and (kt_quaylui_nv_4==0):
                                n4=n4+random.randint(-20,30)
                                if (n5<1150) and (kt_quaylui_nv_5==0):
                                    n5=n5+random.randint(-20,30)
                                    if (n6<1150) and (kt_quaylui_nv_6==0):
                                        n6=n6+random.randint(-20,30)
                                    else:
                                        count_nv_HetQuayLui6 = count_nv_HetQuayLui6 +1
                                        if count_nv_HetQuayLui6 <40:
                                            n6=n6-20
                                        else:
                                            n6=n6+random.randint(0,5)
                                        n3=n3+random.randint(-10,5)
                                        n2=n2+random.randint(-10,5)
                                        n4=n4+random.randint(-10,5)
                                        n5=n5+random.randint(-10,5)
                                        kt_quaylui_nv_6=1
                                else:
                                    count_nv_HetQuayLui5 = count_nv_HetQuayLui5 +1
                                    if count_nv_HetQuayLui5 <40:
                                        n5=n5-20
                                    else:
                                        n5=n5+random.randint(0,5)
                                    n3=n3+random.randint(-10,5)
                                    n2=n2+random.randint(-10,5)
                                    n4=n4+random.randint(-10,5)
                                    n6=n6+random.randint(-10,5)
                                    kt_quaylui_nv_5=1
                            else:
                                count_nv_HetQuayLui = count_nv_HetQuayLui4 +1
                                if count_nv_HetQuayLui <40:
                                    n4=n4-20
                                else:
                                    n4=n4+random.randint(0,5)
                                n3=n3+random.randint(-10,5)
                                n2=n2+random.randint(-10,5)
                                n5=n5+random.randint(-10,5)
                                n6=n6+random.randint(-10,5)
                                kt_quaylui_nv_4=1
                        else:
                            count_nv_HetQuayLui3 = count_nv_HetQuayLui3 +1
                            if count_nv_HetQuayLui3 <40:
                                n3=n3-20
                            else:
                                n3=n3+random.randint(0,5)
                            n2=n2+random.randint(-10,5)
                            n4=n4+random.randint(-10,5)
                            n5=n5+random.randint(-10,5)
                            n6=n6+random.randint(-10,5)
                            kt_quaylui_nv_3=1
                    else:
                        count_nv_HetQuayLui2 = count_nv_HetQuayLui2 +1
                        if count_nv_HetQuayLui2 <40:
                            n2=n2-20
                        else:
                            n2=n2+random.randint(0,5)
                        n3=n3+random.randint(-10,5)
                        n4=n4+random.randint(-10,5)
                        n5=n5+random.randint(-10,5)
                        n6=n6+random.randint(-10,5)
                        kt_quaylui_nv_2=1
                    kt_tung_vn_2=1
                    kt_tung_vn_3=1
                    kt_tung_vn_4=1
                    kt_tung_vn_5=1
                    kt_tung_vn_6=1
                elif (vt_vn_2>=625)and kt_tung_vn_2 ==0:
                    if count<200:
                        n2=n2+random.randint(-30,-10)
                    else:
                        n2=n2+v2
                    if (n1<1150) and (kt_quaylui_nv_1==0):
                        n1=n1+random.randint(-20,30)
                        if (n3<1150) and (kt_quaylui_nv_3==0):
                            n3=n3+random.randint(-20,30)
                            if (n4<1150) and (kt_quaylui_nv_4==0):
                                n4=n4+random.randint(-20,30)
                                if (n5<1150) and (kt_quaylui_nv_5==0):
                                    n5=n5+random.randint(-20,30)
                                    if (n6<1150) and (kt_quaylui_nv_6==0):
                                        n6=n6+random.randint(-20,30)
                                    else:
                                        count_nv_HetQuayLui6 = count_nv_HetQuayLui6 +1
                                        if count_nv_HetQuayLui6 <40:
                                            n6=n6-20
                                        else:
                                            n6=n6+random.randint(0,5)
                                        n3=n3+random.randint(-10,5)
                                        n1=n1+random.randint(-10,5)
                                        n4=n4+random.randint(-10,5)
                                        n5=n5+random.randint(-10,5)
                                        kt_quaylui_nv_6=1
                                else:
                                    count_nv_HetQuayLui5 = count_nv_HetQuayLui5 +1
                                    if count_nv_HetQuayLui5 <40:
                                        n5=n5-20
                                    else:
                                        n5=n5+random.randint(0,5)
                                    n3=n3+random.randint(-10,5)
                                    n1=n1+random.randint(-10,5)
                                    n4=n4+random.randint(-10,5)
                                    n6=n6+random.randint(-10,5)
                                    kt_quaylui_nv_5=1
                            else:
                                count_nv_HetQuayLui4 = count_nv_HetQuayLui4 +1
                                if count_nv_HetQuayLui4 <40:
                                    n4=n4-20
                                else:
                                    n4=n4+random.randint(0,5)
                                n3=n3+random.randint(-10,5)
                                n1=n1+random.randint(-10,5)
                                n5=n5+random.randint(-10,5)
                                n6=n6+random.randint(-10,5)
                                kt_quaylui_nv_4=1
                        else:
                            count_nv_HetQuayLui3 = count_nv_HetQuayLui3 +1
                            if count_nv_HetQuayLui3 <40:
                                n3=n3-20
                            else:
                                n3=n3+random.randint(0,5)
                            n4=n4+random.randint(-10,5)
                            n1=n1+random.randint(-10,5)
                            n5=n5+random.randint(-10,5)
                            n6=n6+random.randint(-10,5)
                            kt_quaylui_nv_3=1
                    else:
                        count_nv_HetQuayLui1 = count_nv_HetQuayLui1 +1
                        if count_nv_HetQuayLui1 <40:
                            n1=n1-20
                        else:
                            n1=n1+random.randint(0,5)
                        n4=n4+random.randint(-10,5)
                        n3=n3+random.randint(-10,5)
                        n5=n5+random.randint(-10,5)
                        n6=n6+random.randint(-10,5)
                        kt_quaylui_nv_2=1
                    kt_tung_vn_1=1
                    kt_tung_vn_3=1
                    kt_tung_vn_4=1
                    kt_tung_vn_5=1
                    kt_tung_vn_6=1
                elif (vt_vn_3>=625)and kt_tung_vn_3 ==0:
                    if count<200:
                        n3=n3+random.randint(-30,-10)
                    else:
                        n3=n3+v3
                    if (n2<1150) and (kt_quaylui_nv_2==0):
                        n2=n2+random.randint(-20,30)
                        if (n1<1150) and (kt_quaylui_nv_1==0):
                            n1=n1+random.randint(-20,30)
                            if (n4<1150) and (kt_quaylui_nv_4==0):
                                n4=n4+random.randint(-20,30)
                                if (n5<1150) and (kt_quaylui_nv_5==0):
                                    n5=n5+random.randint(-20,30)
                                    if (n6<1150) and (kt_quaylui_nv_6==0):
                                        n6=n6+random.randint(-20,30)
                                    else:
                                        count_nv_HetQuayLui6 = count_nv_HetQuayLui6 +1
                                        if count_nv_HetQuayLui6 <40:
                                            n6=n6-20
                                        else:
                                            n6=n6+random.randint(0,5)
                                        n2=n2+random.randint(-10,5)
                                        n1=n1+random.randint(-10,5)
                                        n4=n4+random.randint(-10,5)
                                        n5=n5+random.randint(-10,5)
                                        kt_quaylui_nv_6=1
                                else:
                                    count_nv_HetQuayLui5 = count_nv_HetQuayLui5 +1
                                    if count_nv_HetQuayLui5 <40:
                                        n5=n5-20
                                    else:
                                        n5=n5+random.randint(0,5)
                                    n4=n4+random.randint(-10,5)
                                    n1=n1+random.randint(-10,5)
                                    n2=n2+random.randint(-10,5)
                                    n6=n6+random.randint(-10,5)
                                    kt_quaylui_nv_5=1
                            else:
                                count_nv_HetQuayLui4 = count_nv_HetQuayLui4 +1
                                if count_nv_HetQuayLui4 <40:
                                    n4=n4-20
                                else:
                                    n4=n4+random.randint(0,5)
                                n2=n2+random.randint(-10,5)
                                n1=n1+random.randint(-10,5)
                                n5=n5+random.randint(-10,5)
                                n6=n6+random.randint(-10,5)
                                kt_quaylui_nv_4=1
                        else:
                            count_nv_HetQuayLui1 = count_nv_HetQuayLui1 +1
                            if count_nv_HetQuayLui1 <40:
                                n1=n1-20
                            else:
                                n1=n1+random.randint(0,5)
                            n2=n2+random.randint(-10,5)
                            n4=n4+random.randint(-10,5)
                            n5=n5+random.randint(-10,5)
                            n6=n6+random.randint(-10,5)
                            kt_quaylui_nv_1=1
                    else:
                        count_nv_HetQuayLui2 = count_nv_HetQuayLui2 +1
                        if count_nv_HetQuayLui2 <40:
                            n2=n2-20
                        else:
                            n2=n2+random.randint(0,5)
                        n1=n1+random.randint(-10,5)
                        n4=n4+random.randint(-10,5)
                        n5=n5+random.randint(-10,5)
                        n6=n6+random.randint(-10,5)
                        kt_quaylui_nv_2=1
                    kt_tung_vn_2=1
                    kt_tung_vn_1=1
                    kt_tung_vn_4=1
                    kt_tung_vn_5=1
                    kt_tung_vn_6=1
                elif (vt_vn_4>=625)and kt_tung_vn_4 ==0:
                    if count<200:
                        n4=n4+random.randint(-30,-10)
                    else:
                        n4=n4+v4
                    if (n2<1150) and (kt_quaylui_nv_2==0):
                        n2=n2+random.randint(-20,30)
                        if (n3<1150) and (kt_quaylui_nv_3==0):
                            n3=n3+random.randint(-20,30)
                            if (n1<1150) and (kt_quaylui_nv_1==0):
                                n1=n1+random.randint(-20,30)
                                if (n5<1150) and (kt_quaylui_nv_5==0):
                                    n5=n5+random.randint(-20,30)
                                    if (n6<1150) and (kt_quaylui_nv_6==0):
                                        n6=n6+random.randint(-20,30)
                                    else:
                                        count_nv_HetQuayLui6 = count_nv_HetQuayLui6 +1
                                        if count_nv_HetQuayLui6 <40:
                                            n6=n6-20
                                        else:
                                            n6=n6+random.randint(0,5)
                                        n2=n2+random.randint(-10,5)
                                        n1=n1+random.randint(-10,5)
                                        n4=n4+random.randint(-10,5)
                                        n5=n5+random.randint(-10,5)
                                        kt_quaylui_nv_6=1
                                else:
                                    count_nv_HetQuayLui5 = count_nv_HetQuayLui5 +1
                                    if count_nv_HetQuayLui5 <40:
                                        n5=n5-20
                                    else:
                                        n5=n5+random.randint(0,5)
                                    n2=n2+random.randint(-10,5)
                                    n1=n1+random.randint(-10,5)
                                    n3=n3+random.randint(-10,5)
                                    n6=n6+random.randint(-10,5)
                                    kt_quaylui_nv_5=1
                            else:
                                count_nv_HetQuayLui1 = count_nv_HetQuayLui1 +1
                                if count_nv_HetQuayLui1 <40:
                                    n1=n1-20
                                else:
                                    n1=n1+random.randint(0,5)
                                n2=n2+random.randint(-10,5)
                                n5=n5+random.randint(-10,5)
                                n3=n3+random.randint(-10,5)
                                n6=n6+random.randint(-10,5)
                                kt_quaylui_nv_1=1
                        else:
                            count_nv_HetQuayLui3 = count_nv_HetQuayLui3 +1
                            if count_nv_HetQuayLui3 <40:
                                n3=n3-20
                            else:
                                n3=n3+random.randint(0,5)
                            n2=n2+random.randint(-10,5)
                            n5=n5+random.randint(-10,5)
                            n1=n1+random.randint(-10,5)
                            n6=n6+random.randint(-10,5)
                            kt_quaylui_nv_3=1
                    else:
                        count_nv_HetQuayLui2 = count_nv_HetQuayLui2 +1
                        if count_nv_HetQuayLui2 <40:
                            n2=n2-20
                        else:
                            n2=n2+random.randint(0,5)
                        n1=n1+random.randint(-10,5)
                        n5=n5+random.randint(-10,5)
                        n3=n3+random.randint(-10,5)
                        n6=n6+random.randint(-10,5)
                        kt_quaylui_nv_2=1
                    kt_tung_vn_2=1
                    kt_tung_vn_3=1
                    kt_tung_vn_1=1
                    kt_tung_vn_5=1
                    kt_tung_vn_6=1
                elif (vt_vn_5>=625)and kt_tung_vn_5 ==0:
                    if count<200:
                        n5=n5+random.randint(-30,-10)
                    else:
                        n5=n5+v5
                    if (n2<1150) and (kt_quaylui_nv_2==0):
                        n2=n2+random.randint(-20,30)
                        if (n3<1150) and (kt_quaylui_nv_3==0):
                            n3=n3+random.randint(-20,30)
                            if (n4<1150) and (kt_quaylui_nv_4==0):
                                n4=n4+random.randint(-20,30)
                                if (n1<1150) and (kt_quaylui_nv_1==0):
                                    n1=n1+random.randint(-20,30)
                                    if (n6<1150) and (kt_quaylui_nv_6==0):
                                        n6=n6+random.randint(-20,30)
                                    else:
                                        count_nv_HetQuayLui6 = count_nv_HetQuayLui6 +1
                                        if count_nv_HetQuayLui6 <40:
                                            n6=n6-20
                                        else:
                                            n6=n6+random.randint(0,5)
                                        n2=n2+random.randint(-10,5)
                                        n1=n1+random.randint(-10,5)
                                        n4=n4+random.randint(-10,5)
                                        n5=n5+random.randint(-10,5)
                                        kt_quaylui_nv_6=1
                                else:
                                    count_nv_HetQuayLui1 = count_nv_HetQuayLui1 +1
                                    if count_nv_HetQuayLui1 <40:
                                        n1=n1-20
                                    else:
                                        n1=n1+random.randint(0,5)
                                    n2=n2+random.randint(-10,5)
                                    n4=n4+random.randint(-10,5)
                                    n3=n3+random.randint(-10,5)
                                    n6=n6+random.randint(-10,5)
                                    kt_quaylui_nv_1=1
                            else:
                                count_nv_HetQuayLui4 = count_nv_HetQuayLui4 +1
                                if count_nv_HetQuayLui4 <40:
                                    n4=n4-20
                                else:
                                    n4=n4+random.randint(0,5)
                                n2=n2+random.randint(-10,5)
                                n1=n1+random.randint(-10,5)
                                n3=n3+random.randint(-10,5)
                                n6=n6+random.randint(-10,5)
                                kt_quaylui_nv_4=1
                        else:
                            count_nv_HetQuayLui3 = count_nv_HetQuayLui3 +1
                            if count_nv_HetQuayLui3 <40:
                                n3=n3-20
                            else:
                                n3=n3+random.randint(0,5)
                            n2=n2+random.randint(-10,5)
                            n4=n4+random.randint(-10,5)
                            n1=n1+random.randint(-10,5)
                            n6=n6+random.randint(-10,5)
                            kt_quaylui_nv_3=1
                    else:
                        count_nv_HetQuayLui2 = count_nv_HetQuayLui2 +1
                        if count_nv_HetQuayLui2 <40:
                            n2=n2-20
                        else:
                            n2=n2+random.randint(0,5)
                        n1=n1+random.randint(-10,5)
                        n4=n4+random.randint(-10,5)
                        n3=n3+random.randint(-10,5)
                        n6=n6+random.randint(-10,5)
                        kt_quaylui_nv_2=1
                    kt_tung_vn_2=1
                    kt_tung_vn_3=1
                    kt_tung_vn_4=1
                    kt_tung_vn_1=1
                    kt_tung_vn_6=1
                elif (vt_vn_6>=625)and kt_tung_vn_6 ==0:
                    if count<200:
                        n6=n6+random.randint(-30,-10)
                    else:
                        n6=n6+v6
                    if (n2<1150) and (kt_quaylui_nv_2==0):
                        n2=n2+random.randint(-20,30)
                        if (n3<1150) and (kt_quaylui_nv_3==0):
                            n3=n3+random.randint(-20,30)
                            if (n4<1150) and (kt_quaylui_nv_4==0):
                                n4=n4+random.randint(-20,30)
                                if (n1<1150) and (kt_quaylui_nv_1==0):
                                    n1=n1+random.randint(-20,30)
                                    if (n5<1150) and (kt_quaylui_nv_5==0):
                                        n5=n5+random.randint(-20,30)
                                    else:
                                        count_nv_HetQuayLui5 = count_nv_HetQuayLui5 +1
                                        if count_nv_HetQuayLui5 <40:
                                            n5=n5-20
                                        else:
                                            n6=n6+random.randint(0,5)
                                        n2=n2+random.randint(-10,5)
                                        n1=n1+random.randint(-10,5)
                                        n4=n4+random.randint(-10,5)
                                        n6=n6+random.randint(-10,5)
                                        kt_quaylui_nv_5=1
                                else:
                                    count_nv_HetQuayLui1 = count_nv_HetQuayLui1 +1
                                    if count_nv_HetQuayLui1 <40:
                                        n1=n1-20
                                    else:
                                        n1=n1+random.randint(0,5)
                                    n2=n2+random.randint(-10,5)
                                    n4=n4+random.randint(-10,5)
                                    n3=n3+random.randint(-10,5)
                                    n5=n5+random.randint(-10,5)
                                    kt_quaylui_nv_1=1
                            else:
                                count_nv_HetQuayLui4 = count_nv_HetQuayLui4 +1
                                if count_nv_HetQuayLui4 <40:
                                    n4=n4-20
                                else:
                                    n4=n4+random.randint(0,5)
                                n2=n2+random.randint(-10,5)
                                n1=n1+random.randint(-10,5)
                                n3=n3+random.randint(-10,5)
                                n5=n5+random.randint(-10,5)
                                kt_quaylui_nv_4=1
                        else:
                            count_nv_HetQuayLui3 = count_nv_HetQuayLui3 +1
                            if count_nv_HetQuayLui3 <40:
                                n3=n3-20
                            else:
                                n3=n3+random.randint(0,5)
                            n2=n2+random.randint(-10,5)
                            n4=n4+random.randint(-10,5)
                            n1=n1+random.randint(-10,5)
                            n5=5+random.randint(-10,5)
                            kt_quaylui_nv_3=1
                    else:
                        count_nv_HetQuayLui2 = count_nv_HetQuayLui2 +1
                        if count_nv_HetQuayLui2 <40:
                            n2=n2-20
                        else:
                            n2=n2+random.randint(0,5)
                        n1=n1+random.randint(-10,5)
                        n4=n4+random.randint(-10,5)
                        n3=n3+random.randint(-10,5)
                        n5=n5+random.randint(-10,5)
                        kt_quaylui_nv_2=1
                    kt_tung_vn_2=1
                    kt_tung_vn_3=1
                    kt_tung_vn_4=1
                    kt_tung_vn_1=1
                    kt_tung_vn_5=1
            elif kt_tung_vn_1 ==0 or kt_tung_vn_2 ==0 or kt_tung_vn_3 ==0 or kt_tung_vn_4 ==0 or kt_tung_vn_5 ==0 or kt_tung_vn_6==0: 
                n1=n1+v1
                n2=n2+v2
                n3=n3+v3
                n4=n4+v4 
                n5=n5+v5
                n6=n6+v6
        if n1>=1180 or n2>=1180 or n3>=1180 or n4>=1180 or n5>=1180 or n6 >=1180:
            if kt_tung_vn_1 ==0 or kt_tung_vn_1==1:
                kt_tung_vn_1=1
            if kt_tung_vn_2 ==0 or kt_tung_vn_2==1:
                kt_tung_vn_2=1
            if kt_tung_vn_3 ==0 or kt_tung_vn_3==1:
                kt_tung_vn_3=1
            if kt_tung_vn_4 ==0 or kt_tung_vn_4==1:
                kt_tung_vn_4=1
            if kt_tung_vn_5 ==0 or kt_tung_vn_5==1:
                kt_tung_vn_5=1
            if kt_tung_vn_6 ==0 or kt_tung_vn_6==1:
                kt_tung_vn_6=1
            if n1 <1180:
                n1=n1+random.randint(10,20)
            if n1>=1180 and dem<5 and kt_tung_vn_1 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure1)
                kt_tung_vn_1 =2
            if n2 <1180:
                n2=n2+random.randint(10,20)
            if n2>=1180 and dem<5 and kt_tung_vn_2 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure2)
                kt_tung_vn_2 =2
            if n3 <1180:  
                n3=n3+random.randint(10,20)
            if n3>=1180 and dem<5 and kt_tung_vn_3 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure3)
                kt_tung_vn_3 =2
            if n4 <1180:
                n4=n4+random.randint(10,20)
            if n4>=1180 and dem<5 and kt_tung_vn_4 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure4)
                kt_tung_vn_4 =2
            if n5 <1180:  
                n5=n5+random.randint(10,20)
            if n5>=1180 and dem<5 and kt_tung_vn_5 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure5)
                kt_tung_vn_5 =2
            if n6 <1180:  
                n6=n6+random.randint(10,20)
            if n6>=1180 and dem<5 and kt_tung_vn_6 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure6)
                kt_tung_vn_6 =2
        pygame.display.flip()
        pygame.time.Clock().tick(60)
        if n1>=1180 and n2>=1180 and n3>=1180 and n4>=1180 and n5>=1180 and n6>=1180:
            time.sleep(1)
            for j in i_win:
                if MangNhanVat[j] == CaCuoc:
                    file = open(namefile, "a+")
                    temp_money = int(tail(file,1))
                    file.write(namefile)
                    file.write("\n")
                    file.write(money)
                    file.write("\n")
                    file.write("Win \n")
                    file.write(str(j+1))
                    file.write("\n")
                    file.write(str(int(money)+temp_money))
                    file.write("\n")
                    file.close()
                    main(MangNhanVat[0],MangNhanVat[1],MangNhanVat[2],MangNhanVat[3],MangNhanVat[4],"background/WIN.png",str(int(money)*2),name_of_file=namefile)
                    break
            for j in i_lose:
                if MangNhanVat[j] == CaCuoc:
                    file = open(namefile, "a+")
                    temp_money = int(tail(file,1))
                    file.write(namefile)
                    file.write("\n")
                    file.write(money)
                    file.write("\n")
                    file.write("Lose \n")
                    file.write(str(j+1))
                    file.write("\n")
                    file.write(str(temp_money + -1*int(money)))
                    file.write("\n")
                    file.close()
                    main(MangNhanVat[0],MangNhanVat[1],MangNhanVat[2],MangNhanVat[3],MangNhanVat[4],"background/LOSE.png","0",name_of_file=namefile)
                    break
            pygame.quit()

""" -------------------------------------------------------------------------------------------------------"""
def Game_Run(Figure1,Figure2,Figure3,Figure4,Figure5,BACKGROUND,CaCuoc,namefile,money):
    pygame.init()
    m =70
    NV1 = pygame.transform.scale(pygame.image.load(Figure1),(m,m))
    NV2 = pygame.transform.scale(pygame.image.load(Figure2),(m,m))
    NV3 = pygame.transform.scale(pygame.image.load(Figure3),(m,m))
    NV4 = pygame.transform.scale(pygame.image.load(Figure4),(m,m))
    NV5 = pygame.transform.scale(pygame.image.load(Figure5),(m,m))
    BackGround_Dich = pygame.transform.scale(pygame.image.load(BACKGROUND),(3000,700))
    So1 = pygame.transform.scale(pygame.image.load("background/1.png"),(150,150))
    So2 = pygame.transform.scale(pygame.image.load("background/2.png"),(150,150))
    So3 = pygame.transform.scale(pygame.image.load("background/3.png"),(150,150))
    Start = pygame.transform.scale(pygame.image.load("background/start.png"),(150,150))
    #tao cua so
    gameSurface = pygame.display.set_mode((1250,700))
    pygame.display.set_caption('Let''s go Turtle')
    #mau sac
    red = pygame.Color(255,0,0)
    blue = pygame.Color(65,105,255)
    black = pygame.Color(0,0,0)
    white = pygame.Color(255,255,255)
    gray = pygame.Color(128,128,128)
    #ham Winer
    def Winner():
        gfont = pygame.font.SysFont('8-BIT WONDER.TTF',50)
        gsurf = gfont.render('WINNER ',True,red)
        grect = gsurf.get_rect()
        grect.midtop = (625,250)
        gameSurface.blit(gsurf,grect)
        pygame.display.flip()
        time.sleep(1) 
    def ManHinhBatDau():
        gameSurface.fill(white)
        gameSurface.blit(BackGround_Dich,pygame.Rect(0,0,1250,700))
        gameSurface.blit(NV1,pygame.Rect(n1,270,m,m))
        gameSurface.blit(NV2,pygame.Rect(n2,360,m,m))
        gameSurface.blit(NV3,pygame.Rect(n3,440,m,m))
        gameSurface.blit(NV4,pygame.Rect(n4,520,m,m))
        gameSurface.blit(NV5,pygame.Rect(n5,600,m,m))
    #ham dem nguoc
    def Dem_Nguoc():
        ManHinhBatDau()
        gameSurface.blit(So3,pygame.Rect(550,300,250,250))
        pygame.display.flip()
        time.sleep(1)
        ManHinhBatDau()
        gameSurface.blit(So2,pygame.Rect(550,300,250,250))
        pygame.display.flip()
        time.sleep(1)
        ManHinhBatDau()
        gameSurface.blit(So1,pygame.Rect(550,300,250,250))
        pygame.display.flip()
        time.sleep(1)
        ManHinhBatDau()
        gameSurface.blit(Start,pygame.Rect(550,300,500,500))
        pygame.display.flip()
        time.sleep(1)
        ManHinhBatDau()
        pygame.display.flip()
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
    #khai bao bien
    n1 =0
    n2 =0
    n3 =0
    n4 =0
    n5 =0
    v1=random.randint(5,10)
    v2=random.randint(5,10)
    v3=random.randint(5,10)
    v4=random.randint(5,10)
    v5=random.randint(5,10)
    t=0
    kt=0 #kt dieu kien de nv chay
    kt_tung_vn_1=0#kt nhan vat dung lai
    kt_tung_vn_2=0
    kt_tung_vn_3=0
    kt_tung_vn_4=0
    kt_tung_vn_5=0
    #kt de nhan vat quay lui
    kt_quaylui_nv_1 =0
    kt_quaylui_nv_2 =0
    kt_quaylui_nv_3 =0
    kt_quaylui_nv_4 =0
    kt_quaylui_nv_5 =0
    count_nv_HetQuayLui1 =0
    count_nv_HetQuayLui2 =0
    count_nv_HetQuayLui3 =0
    count_nv_HetQuayLui4 =0
    count_nv_HetQuayLui5 =0
    #kt de dua vo mang
    count=0
    Background_x=0
    dem = -1
    MangNhanVat = [6]
    j=0
    i_win = [0]
    i_lose = [1, 2 , 3 , 4]
    #vong lap chin
    pygame.mixer.init()
    pygame.mixer.music.load("Music/nhacdua.mp3")
    pygame.mixer.music.play()
    while pygame.event.Event != pygame.QUIT:  
        if t==0:
            Dem_Nguoc()         
        t=1
        count=count+1
        gameSurface.fill(white)
        gameSurface.blit(BackGround_Dich,pygame.Rect(Background_x,0,1250,700))
        gameSurface.blit(NV1,pygame.Rect(n1,270,m,m))
        gameSurface.blit(NV2,pygame.Rect(n2,360,m,m))
        gameSurface.blit(NV3,pygame.Rect(n3,440,m,m))
        gameSurface.blit(NV4,pygame.Rect(n4,520,m,m))
        gameSurface.blit(NV5,pygame.Rect(n5,600,m,m))
        if n1<=625 and n2<=625 and n3<=625 and n4<=625 and n5<=625 and kt == 0:
            n1=n1+v1
            n2=n2+v2
            n3=n3+v3
            n4=n4+v4
            n5=n5+v5
        else:
            kt=1
            if Background_x>=-1700:
                Background_x = Background_x -5
                if kt_tung_vn_1 ==0 and kt_tung_vn_2 ==0 and kt_tung_vn_3 ==0 and kt_tung_vn_4 ==0 and kt_tung_vn_5 ==0: 
                    vt_vn_1=n1
                    vt_vn_2=n2
                    vt_vn_3=n3
                    vt_vn_4=n4
                    vt_vn_5=n5
                if (vt_vn_1>=625) and kt_tung_vn_1 ==0:
                    if count<200:
                        n1=n1+random.randint(-30,-10)
                    else:
                        n1=n1+v1
                    if (n2<1150) and (kt_quaylui_nv_2==0):
                        n2=n2+random.randint(-20,30)
                        if (n3<1150) and (kt_quaylui_nv_3==0):
                            n3=n3+random.randint(-20,30)
                            if (n4<1150) and (kt_quaylui_nv_4==0):
                                n4=n4+random.randint(-20,30)
                                if (n5<1150) and (kt_quaylui_nv_5==0):
                                    n5=n5+random.randint(-20,30)
                                else:
                                    count_nv_HetQuayLui5 = count_nv_HetQuayLui5 +1
                                    if count_nv_HetQuayLui5 <40:
                                        n5=n5-20
                                    else:
                                        n5=n5+random.randint(0,5)
                                    n3=n3+random.randint(-10,5)
                                    n2=n2+random.randint(-10,5)
                                    n4=n4+random.randint(-10,5)
                                    kt_quaylui_nv_5=1
                            else:
                                count_nv_HetQuayLui = count_nv_HetQuayLui4 +1
                                if count_nv_HetQuayLui <40:
                                    n4=n4-20
                                else:
                                    n4=n4+random.randint(0,5)
                                n3=n3+random.randint(-10,5)
                                n2=n2+random.randint(-10,5)
                                n5=n5+random.randint(-10,5)
                                kt_quaylui_nv_4=1
                        else:
                            count_nv_HetQuayLui3 = count_nv_HetQuayLui3 +1
                            if count_nv_HetQuayLui3 <40:
                                n3=n3-20
                            else:
                                n3=n3+random.randint(0,5)
                            n2=n2+random.randint(-10,5)
                            n4=n4+random.randint(-10,5)
                            n5=n5+random.randint(-10,5)
                            kt_quaylui_nv_3=1
                    else:
                        count_nv_HetQuayLui2 = count_nv_HetQuayLui2 +1
                        if count_nv_HetQuayLui2 <40:
                            n2=n2-20
                        else:
                            n2=n2+random.randint(0,5)
                        n3=n3+random.randint(-10,5)
                        n4=n4+random.randint(-10,5)
                        n5=n5+random.randint(-10,5)
                        kt_quaylui_nv_2=1
                    kt_tung_vn_2=1
                    kt_tung_vn_3=1
                    kt_tung_vn_4=1
                    kt_tung_vn_5=1
                elif (vt_vn_2>=625)and kt_tung_vn_2 ==0:
                    if count<200:
                        n2=n2+random.randint(-30,-10)
                    else:
                        n2=n2+v2
                    if (n1<1150) and (kt_quaylui_nv_1==0):
                        n1=n1+random.randint(-20,30)
                        if (n3<1150) and (kt_quaylui_nv_3==0):
                            n3=n3+random.randint(-20,30)
                            if (n4<1150) and (kt_quaylui_nv_4==0):
                                n4=n4+random.randint(-20,30)
                                if (n5<1150) and (kt_quaylui_nv_5==0):
                                    n5=n5+random.randint(-20,30)
                                else:
                                    count_nv_HetQuayLui5 = count_nv_HetQuayLui5 +1
                                    if count_nv_HetQuayLui5 <40:
                                        n5=n5-20
                                    else:
                                        n5=n5+random.randint(0,5)
                                    n3=n3+random.randint(-10,5)
                                    n1=n1+random.randint(-10,5)
                                    n4=n4+random.randint(-10,5)
                                    kt_quaylui_nv_5=1
                            else:
                                count_nv_HetQuayLui4 = count_nv_HetQuayLui4 +1
                                if count_nv_HetQuayLui4 <40:
                                    n4=n4-20
                                else:
                                    n4=n4+random.randint(0,5)
                                n3=n3+random.randint(-10,5)
                                n1=n1+random.randint(-10,5)
                                n5=n5+random.randint(-10,5)
                                kt_quaylui_nv_4=1
                        else:
                            count_nv_HetQuayLui3 = count_nv_HetQuayLui3 +1
                            if count_nv_HetQuayLui3 <40:
                                n3=n3-20
                            else:
                                n3=n3+random.randint(0,5)
                            n4=n4+random.randint(-10,5)
                            n1=n1+random.randint(-10,5)
                            n5=n5+random.randint(-10,5)
                            kt_quaylui_nv_3=1
                    else:
                        count_nv_HetQuayLui1 = count_nv_HetQuayLui1 +1
                        if count_nv_HetQuayLui1 <40:
                            n1=n1-20
                        else:
                            n1=n1+random.randint(0,5)
                        n4=n4+random.randint(-10,5)
                        n3=n3+random.randint(-10,5)
                        n5=n5+random.randint(-10,5)
                        kt_quaylui_nv_1=1
                    kt_tung_vn_1=1
                    kt_tung_vn_3=1
                    kt_tung_vn_4=1
                    kt_tung_vn_5=1
                elif (vt_vn_3>=625)and kt_tung_vn_3 ==0:
                    if count<200:
                        n3=n3+random.randint(-30,-10)
                    else:
                        n3=n3+v3
                    if (n2<1150) and (kt_quaylui_nv_2==0):
                        n2=n2+random.randint(-20,30)
                        if (n1<1150) and (kt_quaylui_nv_1==0):
                            n1=n1+random.randint(-20,30)
                            if (n4<1150) and (kt_quaylui_nv_4==0):
                                n4=n4+random.randint(-20,30)
                                if (n5<1150) and (kt_quaylui_nv_5==0):
                                    n5=n5+random.randint(-20,30)
                                else:
                                    count_nv_HetQuayLui5 = count_nv_HetQuayLui5 +1
                                    if count_nv_HetQuayLui5 <40:
                                        n5=n5-20
                                    else:
                                        n5=n5+random.randint(0,5)
                                    n4=n4+random.randint(-10,5)
                                    n1=n1+random.randint(-10,5)
                                    n2=n2+random.randint(-10,5)
                                    kt_quaylui_nv_5=1
                            else:
                                count_nv_HetQuayLui4 = count_nv_HetQuayLui4 +1
                                if count_nv_HetQuayLui4 <40:
                                    n4=n4-20
                                else:
                                    n4=n4+random.randint(0,5)
                                n2=n2+random.randint(-10,5)
                                n1=n1+random.randint(-10,5)
                                n5=n5+random.randint(-10,5)
                                kt_quaylui_nv_4=1
                        else:
                            count_nv_HetQuayLui1 = count_nv_HetQuayLui1 +1
                            if count_nv_HetQuayLui1 <40:
                                n1=n1-20
                            else:
                                n1=n1+random.randint(0,5)
                            n2=n2+random.randint(-10,5)
                            n4=n4+random.randint(-10,5)
                            n5=n5+random.randint(-10,5)
                            kt_quaylui_nv_1=1
                    else:
                        count_nv_HetQuayLui2 = count_nv_HetQuayLui2 +1
                        if count_nv_HetQuayLui2 <40:
                            n2=n2-20
                        else:
                            n2=n2+random.randint(0,5)
                        n1=n1+random.randint(-10,5)
                        n4=n4+random.randint(-10,5)
                        n5=n5+random.randint(-10,5)
                        kt_quaylui_nv_2=1
                    kt_tung_vn_2=1
                    kt_tung_vn_1=1
                    kt_tung_vn_4=1
                    kt_tung_vn_5=1
                elif (vt_vn_4>=625)and kt_tung_vn_4 ==0:
                    if count<200:
                        n4=n4+random.randint(-30,-10)
                    else:
                        n4=n4+v4
                    if (n2<1150) and (kt_quaylui_nv_2==0):
                        n2=n2+random.randint(-20,30)
                        if (n3<1150) and (kt_quaylui_nv_3==0):
                            n3=n3+random.randint(-20,30)
                            if (n1<1150) and (kt_quaylui_nv_1==0):
                                n1=n1+random.randint(-20,30)
                                if (n5<1150) and (kt_quaylui_nv_5==0):
                                    n5=n5+random.randint(-20,30)
                                else:
                                    count_nv_HetQuayLui5 = count_nv_HetQuayLui5 +1
                                    if count_nv_HetQuayLui5 <40:
                                        n5=n5-20
                                    else:
                                        n5=n5+random.randint(0,5)
                                    n2=n2+random.randint(-10,5)
                                    n1=n1+random.randint(-10,5)
                                    n3=n3+random.randint(-10,5)
                                    kt_quaylui_nv_5=1
                            else:
                                count_nv_HetQuayLui1 = count_nv_HetQuayLui1 +1
                                if count_nv_HetQuayLui1 <40:
                                    n1=n1-20
                                else:
                                    n1=n1+random.randint(0,5)
                                n2=n2+random.randint(-10,5)
                                n5=n5+random.randint(-10,5)
                                n3=n3+random.randint(-10,5)
                                kt_quaylui_nv_1=1
                        else:
                            count_nv_HetQuayLui3 = count_nv_HetQuayLui3 +1
                            if count_nv_HetQuayLui3 <40:
                                n3=n3-20
                            else:
                                n3=n3+random.randint(0,5)
                            n2=n2+random.randint(-10,5)
                            n5=n5+random.randint(-10,5)
                            n1=n1+random.randint(-10,5)
                            kt_quaylui_nv_3=1
                    else:
                        count_nv_HetQuayLui2 = count_nv_HetQuayLui2 +1
                        if count_nv_HetQuayLui2 <40:
                            n2=n2-20
                        else:
                            n2=n2+random.randint(0,5)
                        n1=n1+random.randint(-10,5)
                        n5=n5+random.randint(-10,5)
                        n3=n3+random.randint(-10,5)
                        kt_quaylui_nv_2=1
                    kt_tung_vn_2=1
                    kt_tung_vn_3=1
                    kt_tung_vn_1=1
                    kt_tung_vn_5=1
                elif (vt_vn_5>=625)and kt_tung_vn_5 ==0:
                    if count<200:
                        n5=n5+random.randint(-30,-10)
                    else:
                        n5=n5+v5
                    if (n2<1150) and (kt_quaylui_nv_2==0):
                        n2=n2+random.randint(-20,30)
                        if (n3<1150) and (kt_quaylui_nv_3==0):
                            n3=n3+random.randint(-20,30)
                            if (n4<1150) and (kt_quaylui_nv_4==0):
                                n4=n4+random.randint(-20,30)
                                if (n1<1150) and (kt_quaylui_nv_1==0):
                                    n1=n1+random.randint(-20,30)
                                else:
                                    count_nv_HetQuayLui1 = count_nv_HetQuayLui1 +1
                                    if count_nv_HetQuayLui1 <40:
                                        n1=n1-20
                                    else:
                                        n1=n1+random.randint(0,5)
                                    n2=n2+random.randint(-10,5)
                                    n4=n4+random.randint(-10,5)
                                    n3=n3+random.randint(-10,5)
                                    kt_quaylui_nv_1=1
                            else:
                                count_nv_HetQuayLui4 = count_nv_HetQuayLui4 +1
                                if count_nv_HetQuayLui4 <40:
                                    n4=n4-20
                                else:
                                    n4=n4+random.randint(0,5)
                                n2=n2+random.randint(-10,5)
                                n1=n1+random.randint(-10,5)
                                n3=n3+random.randint(-10,5)
                                kt_quaylui_nv_4=1
                        else:
                            count_nv_HetQuayLui3 = count_nv_HetQuayLui3 +1
                            if count_nv_HetQuayLui3 <40:
                                n3=n3-20
                            else:
                                n3=n3+random.randint(0,5)
                            n2=n2+random.randint(-10,5)
                            n4=n4+random.randint(-10,5)
                            n1=n1+random.randint(-10,5)
                            kt_quaylui_nv_3=1
                    else:
                        count_nv_HetQuayLui2 = count_nv_HetQuayLui2 +1
                        if count_nv_HetQuayLui2 <40:
                            n2=n2-20
                        else:
                            n2=n2+random.randint(0,5)
                        n1=n1+random.randint(-10,5)
                        n4=n4+random.randint(-10,5)
                        n3=n3+random.randint(-10,5)
                        kt_quaylui_nv_2=1
                    kt_tung_vn_2=1
                    kt_tung_vn_3=1
                    kt_tung_vn_4=1
                    kt_tung_vn_1=1
            elif kt_tung_vn_1 ==0 or kt_tung_vn_2 ==0 or kt_tung_vn_3 ==0 or kt_tung_vn_4 ==0 or kt_tung_vn_5 ==0: 
                n1=n1+v1
                n2=n2+v2
                n3=n3+v3
                n4=n4+v4
                n5=n5+v5
        if n1>=1180 or n2>=1180 or n3>=1180 or n4>=1180 or n5>=1180:
            if kt_tung_vn_1 ==0 or kt_tung_vn_1==1:
                kt_tung_vn_1=1
            if kt_tung_vn_2 ==0 or kt_tung_vn_2==1:
                kt_tung_vn_2=1
            if kt_tung_vn_3 ==0 or kt_tung_vn_3==1:
                kt_tung_vn_3=1
            if kt_tung_vn_4 ==0 or kt_tung_vn_4==1:
                kt_tung_vn_4=1
            if kt_tung_vn_5 ==0 or kt_tung_vn_5==1:
                kt_tung_vn_5=1
            if n1 <1180:
                n1=n1+random.randint(10,20)
            if n1>=1180 and dem<5 and kt_tung_vn_1 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure1)
                kt_tung_vn_1 =2
            if n2 <1180:
                n2=n2+random.randint(10,20)
            if n2>=1180 and dem<5 and kt_tung_vn_2 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure2)
                kt_tung_vn_2 =2
            if n3 <1180:  
                n3=n3+random.randint(10,20)
            if n3>=1180 and dem<5 and kt_tung_vn_3 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure3)
                kt_tung_vn_3 =2
            if n4 <1180:
                n4=n4+random.randint(10,20)
            if n4>=1180 and dem<5 and kt_tung_vn_4 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure4)
                kt_tung_vn_4 =2
            if n5 <1180:  
                n5=n5+random.randint(10,20)
            if n5>=1180 and dem<5 and kt_tung_vn_5 ==1:
                dem=dem+1
                MangNhanVat.insert(dem,Figure5)
                kt_tung_vn_5 =2
        pygame.display.flip()
        pygame.time.Clock().tick(60)
        if n1>=1180 and n2>=1180 and n3>=1180 and n4>=1180 and n5>=1180:
            time.sleep(1)
            for j in i_win:
                if MangNhanVat[j] == CaCuoc:
                    file = open(namefile, "a+")
                    temp_money = int(tail(file,1))
                    file.write(namefile)
                    file.write("\n")
                    file.write(money)
                    file.write("\n")
                    file.write("Win \n")
                    file.write(str(j+1))
                    file.write("\n")
                    file.write(str(int(money)+temp_money))
                    file.write("\n")
                    file.close()
                    main(MangNhanVat[0],MangNhanVat[1],MangNhanVat[2],MangNhanVat[3],MangNhanVat[4],"background/WIN.png",str(int(money)*2),name_of_file=namefile)
                    break
            for j in i_lose:
                if MangNhanVat[j] == CaCuoc:
                    file = open(namefile, "a+")
                    temp_money = int(tail(file,1))
                    file.write(namefile)
                    file.write("\n")
                    file.write(money)
                    file.write("\n")
                    file.write("Lose \n")
                    file.write(str(j+1))
                    file.write("\n")
                    file.write(str(int(money)*-1+temp_money))
                    file.write("\n")
                    file.close()
                    main(MangNhanVat[0],MangNhanVat[1],MangNhanVat[2],MangNhanVat[3],MangNhanVat[4],"background/LOSE.png","0",name_of_file=namefile)
                    break
            pygame.quit()