#! /usr/bin/env python2
# -*- coding: utf-8 -*-


import pygame
import sys
from pygame.locals import *
import time
import random



# inicjacja modułu pygame
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.mixer.init()
# szerokość i wysokość okna gry
OKNOGRY_SZER = 400
OKNOGRY_WYS = 800
# kolor okna gry, składowe RGB zapisane w tupli
TLO = (000, 000, 000)




# powierzchnia do rysowania, czyli inicjacja okna gry
oknogry = pygame.display.set_mode((OKNOGRY_SZER, OKNOGRY_WYS), 0, 32)
# tytuł okna gry
pygame.display.set_caption('Multijocker')
spacefont = pygame.font.Font('font.ttf', 32)

def drukuj_wynik_koniec(x):
    PKT_1 = str(x)
    tekst1 = spacefont.render(PKT_1, True, (255, 255, 255))
    tekst_prost1 = tekst1.get_rect()
    tekst_prost1.center = (OKNOGRY_SZER * 0.5, OKNOGRY_WYS * 0.2)
    oknogry.blit(tekst1, tekst_prost1)

    napisek = 'Twój wynik:'
    tekst2 = spacefont.render(napisek, True, (255, 255, 255))
    tekst_prost2 = tekst2.get_rect()
    tekst_prost2.center = (OKNOGRY_SZER * 0.5, OKNOGRY_WYS * 0.15)
    oknogry.blit(tekst2, tekst_prost2)


def drukuj_intro(x):
    PKT_1 = str(x)
    tekst1 = spacefont.render(PKT_1, True, (255, 255, 255))
    tekst_prost1 = tekst1.get_rect()
    tekst_prost1.center = (OKNOGRY_SZER * 0.5, OKNOGRY_WYS * 0.5)
    oknogry.blit(tekst1, tekst_prost1)


def intro():
    introtlo = pygame.image.load("grafiki/tlointro.png")
    napis = "PRESS SPACE"
    pygame.mixer.music.load('Audio/start.mp3')
    pygame.mixer.music.play(-1)
    while True:
        KLATKI = 30  # liczba klatek na sekundę
        czas_spacja = time.time()
        time_spacja = round(czas_spacja)
        # obsługa zdarzeń generowanych przez gracza
        for event in pygame.event.get():
            # przechwyć zamknięcie okna
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==K_SPACE: #if mrugniecie = True:
                    gra()
        # rysowanie obiektów
        oknogry.fill(TLO)  # kolor okna gry
        oknogry.blit(introtlo,(0,0))
        if time_spacja % 2 == 0:
            drukuj_intro(napis)
        # zaktualizuj okno i wyświetl
        pygame.display.update()


def outro(y):
    napis = "PRESS SPACE"
    pygame.mixer.music.load('Audio/8.mp3')
    pygame.mixer.music.play(-1)
    while True:
        KLATKI = 30  # liczba klatek na sekundę
        czas_spacja = time.time()
        time_spacja = round(czas_spacja)
        # obsługa zdarzeń generowanych przez gracza
        for event in pygame.event.get():
            # przechwyć zamknięcie okna
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==K_SPACE: #if mrugniecie = True:
                    gra()
        # rysowanie obiektów
        oknogry.fill(TLO)  # kolor okna gry
        if time_spacja % 2 == 0:
            drukuj_intro(napis)
        # zaktualizuj okno i wyświetl
        drukuj_wynik_koniec(y)
        pygame.display.update()




utwory = ['Audio/third.mp3','Audio/4.mp3','Audio/5.mp3','Audio/6.mp3','Audio/7.mp3']
# tutaj intro #
def gra():
    muzyczka = random.choice(utwory)
    if muzyczka == 'Audio/6.mp3':
        pygame.mixer.music.load(muzyczka)
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.load(muzyczka)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)
    # paletka gracza #########################################################
    PALETKA_SZER = 30  # szerokość
    PALETKA_WYS = 90  # wysokość
    BLUE = (0, 0, 255)  # kolor paletki
    PALETKA_1_POZ = (0, 700)  # początkowa pozycja zapisana w tupli
    # utworzenie powierzchni paletki, wypełnienie jej kolorem,
    #paletka1 = pygame.Surface([PALETKA_SZER, PALETKA_WYS])
    paletka1 = pygame.image.load("grafiki/paletka.png")
    #paletka1.fill(BLUE)
    # ustawienie prostokąta zawierającego paletkę w początkowej pozycji
    paletka1_prost = paletka1.get_rect()
    paletka1_prost.x = PALETKA_1_POZ[0]
    paletka1_prost.y = PALETKA_1_POZ[1]


    # piłka #################################################################
    P_SZER = 20  # szerokość
    P_WYS = 20  # wysokość
    P_PREDKOSC_X = 0  # prędkość pozioma x
    P_PREDKOSC_Y = 1  # prędkość pionowa y
    RED = (255, 0, 0)  # kolor piłki
    # utworzenie powierzchni piłki, narysowanie piłki i wypełnienie kolorem
    #pilka = pygame.Surface([P_SZER, P_WYS], pygame.SRCALPHA, 32).convert_alpha()
    pilka = pygame.image.load("grafiki/pilka.png")
    #pygame.draw.ellipse(pilka, RED, [0, 0, P_SZER, P_WYS])
    # ustawienie prostokąta zawierającego piłkę w początkowej pozycji
    pilka_prost = pilka.get_rect()
    pilka_prost.x = OKNOGRY_SZER / 2
    pilka_prost.y = 650

    #####################
    moment_sygnalu = 30
    licznik = 0
    lot_pilki = int(650)
    czas = 0 #przedłużenie czasu trwania sygnału
    start = 0
    #####################

    # ustawienia animacji ###################################################
    FPS = 30  # liczba klatek na sekundę
    fpsClock = pygame.time.Clock()  # zegar śledzący czas

    #   TEKST #


    fontObj = pygame.font.Font('font.ttf', 64)  # czcionka
    punkty = 0
    def drukuj_punkty1(x):
        PKT_1 = str(x)
        tekst1 = fontObj.render(PKT_1, True, (255, 255, 255))
        tekst_prost1 = tekst1.get_rect()
        tekst_prost1.center = (OKNOGRY_SZER * 0.8, OKNOGRY_WYS * 0.08)
        oknogry.blit(tekst1, tekst_prost1)

    # pętla główna programu
    while True:
        ###### BACKGROUND #####
        if punkty == 0:
            obraz = pygame.image.load("grafiki/t1.png")

#### JAKA PIŁKA? ######
        if P_PREDKOSC_Y >= 0  and (punkty >= 5 and punkty < 10):
            pilka = pygame.image.load("grafiki/pilka1p.png")
        if P_PREDKOSC_Y >= 0  and (punkty >= 10 and punkty <20):
            pilka = pygame.image.load("grafiki/pilka2p.png")
        if P_PREDKOSC_Y >= 0  and (punkty >= 20 and punkty <30):
            pilka = pygame.image.load("grafiki/pilka3p.png")
        if P_PREDKOSC_Y >= 0  and (punkty >= 30):
            pilka = pygame.image.load("grafiki/pilka4p.png")


        czas = pygame.time.get_ticks() #przedłużenie czasu trwania sygnału
        # obsługa zdarzeń generowanych przez gracza
        for event in pygame.event.get():
            # przechwyć zamknięcie okna
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==K_SPACE:
                    moment_sygnalu = pygame.time.get_ticks()
            #if blink.value == 1:
                    #moment_sygnalu = pygame.time.get_ticks()
                    #blink.value = 0
                #if mrugniecie == True:
                    #moment_sygnalu = pygame.time.get_ticks()
        # ruch piłki ########################################################
        # przesuń piłkę po obsłużeniu zdarzeń
        pilka_prost.move_ip(P_PREDKOSC_X, P_PREDKOSC_Y)
        # jeżeli piłka wykracza poza pole gry
        if pilka_prost.top <= lot_pilki:  # piłka uciekła górą #0 oznacza górną krawędź
            P_PREDKOSC_Y *= -1  # odwracamy kierunek ruchu pionowego piłki

        if pilka_prost.bottom >= OKNOGRY_WYS:
                outro(punkty)# piłka uciekła dołem


        # jeżeli piłka dotknie paletki gracza, skieruj ją w przeciwną stronę
        if (pilka_prost.colliderect(paletka1_prost) == True) and ((pygame.time.get_ticks()) - moment_sygnalu) <= 3:
            P_PREDKOSC_Y *= -1
            lot_pilki = lot_pilki - 50
            if lot_pilki < 0:
                lot_pilki = 0
            if P_PREDKOSC_Y < 0 and (punkty >= 5 and punkty < 10):
                pilka = pygame.image.load("grafiki/pilka1.png")
            if P_PREDKOSC_Y < 0 and (punkty >= 10 and punkty <20):
                pilka = pygame.image.load("grafiki/pilka2.png")
            if P_PREDKOSC_Y < 0 and (punkty >= 20 and punkty < 30):
                pilka = pygame.image.load("grafiki/pilka3.png")
            if P_PREDKOSC_Y >= 0  and (punkty >= 30):
                pilka = pygame.image.load("grafiki/pilka4.png")

            licznik = licznik + 1
            punkty = punkty + 1
            if punkty < 20:
                P_PREDKOSC_Y = P_PREDKOSC_Y - 1  #po 20 punkcie "przyspieszenie zwalnia"
            if punkty >= 20:
                P_PREDKOSC_Y = P_PREDKOSC_Y - 0.75
            if punkty == 10:
                obraz = pygame.image.load("grafiki/t2.png")
            if punkty == 20:
                obraz = pygame.image.load("grafiki/t3.png")
            if punkty == 30:
                obraz = pygame.image.load("grafiki/t4.png")
            if punkty == 40:
                obraz = pygame.image.load("grafiki/t5.png")
            if punkty == 50:
                obraz = pygame.image.load("grafiki/t6.png")
            # zapobiegaj przysłanianiu paletki przez piłkę
            pilka_prost.bottom = paletka1_prost.top
            if punkty == 20:
                pygame.mixer.music.load('Audio/second.mp3')
                pygame.mixer.music.play(-1)



        # rysowanie obiektów ################################################
        oknogry.fill(TLO)  # wypełnienie okna gry kolorem
        oknogry.blit(obraz,(0,0))
        drukuj_punkty1(punkty)
        # narysuj w oknie gry paletki
        oknogry.blit(paletka1, paletka1_prost)

        # narysuj w oknie piłkę
        oknogry.blit(pilka, pilka_prost)
        # zaktualizuj okno i wyświetl
        pygame.display.update()

        # zaktualizuj zegar po narysowaniu obiektów
        fpsClock.tick(FPS)

    # KONIEC
intro()
