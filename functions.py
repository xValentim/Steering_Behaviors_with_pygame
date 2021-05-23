from vehicle import create_vehicles
import pygame
import random
from values import *

max_dots = 50

# TODO
def show_environment(window, walls, foods, poisons):
    for wall in walls:
        pygame.draw.circle(window, black, wall, 1)
    for food in foods:
        pygame.draw.circle(window, green, food, 1)
    for poison in poisons:
        pygame.draw.circle(window, red, poison, 1)
    return None

# TODO
def create_food(n):
    posicoes = []
    for i in range(n):
        posicoes.append(pygame.Vector2(random.randint (0, largura), random.randint (0, altura)))
    return posicoes


# TODO
def add_food(n, food):
    for i in range(n):
        food.append(pygame.Vector2(random.randint (0, largura), random.randint (0, altura)))
    return food

# TODO
def insert_food(probability_food, food):
    pass

# TODO
def create_poison(n):
    posicoes = []
    for i in range(n):
        posicoes.append(pygame.Vector2(random.randint (0, largura), random.randint (0, altura)))
    return posicoes

# TODO
def add_posion(n, poison):
    for i in range(n):
        poison.append(pygame.Vector2(random.randint (0, largura), random.randint (0, altura)))
    return poison

# TODO
def insert_poison(probability_poison, poison):
    pass

# TODO
def new_generation(start_vehicles=50, start_food=50, start_poison=50):
    pass
    
# TODO
def to_draw_vehicle_picture(v1, vehicles, window):
    pass

# TODO
def to_draw_vehicle_polygon():
    pass

# TODO
def to_draw_dna(window, v1, dna_view):
    pass

#
def texto(window, msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, [x, y])

# Constroi o tapete de sierpinski
def sierpinski_carpet(k=1, aumento=50, active=True):
    if not active:
        return []
    #k = 2
    LL = 3 ** k
    L = int(LL)
    lista_de_vetores = []
    for i in range(L):
        for j in range(L):
            kk = 0
            while kk <= k-1:
                if floor((i - 1) / pow(3, kk)) % 3 == 1 and floor((j - 1) / pow(3, kk)) % 3 == 1:
                    x, y = float(i), float(j)
                    lista_de_vetores.append(pygame.Vector2(x, y))
                kk += 1
    aumento = 50
    soma_total_x = 0
    soma_total_y = 0
    qtde_total = 0
    for i in range(len(lista_de_vetores)):
        lista_de_vetores[i].x = lista_de_vetores[i].x * aumento #+ largura / 4
        lista_de_vetores[i].y = lista_de_vetores[i].y * aumento #+ altura / 4
        #pygame.draw.rect(window, black, (lista_de_vetores[i].x, lista_de_vetores[i].y, aumento, aumento), 0)
        soma_total_x += lista_de_vetores[i].x
        soma_total_y += lista_de_vetores[i].y
        qtde_total += 1

    # Calcula o centro da figura, soma todos os vetores posição e divide pela qtde total
    centro_x = soma_total_x / qtde_total
    centro_y = soma_total_y / qtde_total
    centro_sc = pygame.Vector2(centro_x, centro_y)
    centro = pygame.Vector2(largura / 2, altura / 2)

    # Calcula o vetor de translação
    vetor_de_translação = centro - centro_sc

    # Translada os muros
    for i in range(len(lista_de_vetores)):
        lista_de_vetores[i] += vetor_de_translação #+ largura / 4
        #pygame.draw.rect(window, gray2, (lista_de_vetores[i].x, lista_de_vetores[i].y, aumento / 3, aumento / 3), 0)
     
    return lista_de_vetores