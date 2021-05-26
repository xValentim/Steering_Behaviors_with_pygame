from operator import pos
from tkinter import LEFT
import pygame
from values import *
from functions import *
from vehicle import *



def create_rect(window, color, center, b, h):
    pygame.draw.rect(window, color, [center[0] - b / 2, center[1] - h / 2, b, h])
    return None

def init_screen(window, relogio):
    vehicles_list = create_vehicles(50)

    init_sc = True
    while init_sc:
        target = pygame.mouse.get_pos()
        pos_mouse = pygame.Vector2(target[0], target[1])
        distancia_ao_centro = (pos_mouse - centro).magnitude()
        pygame.draw.circle(window, green, centro, 20)
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if distancia_ao_centro < 20 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True
            if (pos_mouse - pygame.Vector2(largura / 2, altura / 2 + 45)).magnitude() < 20 and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return False
        window.fill(gray)

        # texto(window, f''' Genetics.io''', white, 50, largura/2 - 100 , altura/2 - 150)
        texto(window, f''' The Evolution Game''', white, 70, largura/2 - 230 , altura/2 - 150)
        texto(window, f''' Para jogar aperte no botão "Start".''', white, 15, 0 , altura - 110)
        texto(window, f''' Durante o jogo pressione as teclas para''', white, 15, 0 , altura - 100)
        texto(window, f''' F - para adicionar mais comidas''', white, 15, 0 , altura - 90)
        texto(window, f''' P - para adicionar mais venenos''', white, 15, 0 , altura - 80)
        texto(window, f''' V - para adicionar mais veículos''', white, 15, 0 , altura - 70)
        texto(window, f''' D - para visualizar ou deixar de ver o DNA dos veículos''', white, 15, 0 , altura - 60)
        texto(window, f''' R - para passar para a proxima geração de veículos''', white, 15, 0 , altura - 50)
        texto(window, f''' L - para diminuir o FPS''', white, 15, 0 , altura - 40)
        texto(window, f''' S - para aumentar o FPS''', white, 15, 0 , altura - 30)
        texto(window, f''' M - para printar os pesos da comida, do raio da comida, do veneno e''', white, 15, 0 , altura - 20)
        texto(window, f''' do raio do veneno para o maior veículo e o maior tempo de vida''', white, 15, 0 , altura - 10)


        texto(window, f"Start", white, 30, largura / 2 - 25, altura / 2 - 12)
        if distancia_ao_centro < 20:
            create_rect(window, gray3, [largura / 2, altura / 2], 140, 40)
            texto(window, f"Start", green, 30, largura / 2 - 25, altura / 2 - 10)

        texto(window, f"Quit", white, 30, largura / 2 - 25, altura / 2 + 37)
        if (pos_mouse - pygame.Vector2(largura / 2, altura / 2 + 45)).magnitude() < 20:
            create_rect(window, gray3, [largura / 2, altura / 2 + 45], 140, 40)
            texto(window, f"Quit", red, 30, largura / 2 - 25, altura / 2 + 35)
            
        for v in vehicles_list:
            v.behaviors([pos_mouse], [], [])
            v.update()
            v.dna[3], v.dna[4], v.dna[5] = 200, 200, 200
            v.health = 4
            v.maxforce = 0.1
            v.maxspeed = 5
            to_draw_vehicle_polygon(v, window)

        relogio.tick(fps)
        pygame.display.update()
        
        

