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
    z = random.random()
    if z <= probability_food:
        food.append(pygame.Vector2(random.randint (0, largura), random.randint (0, altura)))
    return food


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
    z = random.random()
    if z <= probability_poison:
        poison.append(pygame.Vector2(random.randint (0, largura), random.randint (0, altura)))
    return poison

# TODO
def new_generation(start_vehicles=50, start_food=50, start_poison=50):
    return create_vehicles (start_vehicles), create_food (start_food), create_poison (start_poison)
    
# TODO
def to_draw_vehicle_picture(v1, vehicles, window):
    health_i = round(v1.health) + 1
    if health_i < 1:
        health_i = 1
    elif health_i > 7:
        health_i = 7
    k = float(v1.r)
    vehicles[health_i] = pygame.transform.scale(vehicles_base[health_i], (int(k * 30), int(k * 16)))

    teta = v1.velocity.as_polar()
    teta = teta[1]
    
    vehicles[health_i] = pygame.transform.rotate(vehicles[health_i], -teta)
    
    rect = vehicles[health_i].get_rect()
    rect.center = v1.position
    
    window.blit(vehicles[health_i], rect)

# TODO
def to_draw_vehicle_polygon():
    pass

# TODO
def to_draw_dna(window, v1, dna_view):
    if dna_view:
        pygame.draw.line(window, green, v1.position, (v1.position + v1.velocity.normalize() * v1.dna[0] * 20), width=3)
        pygame.draw.line(window, red, v1.position, (v1.position + v1.velocity.normalize() * v1.dna[1] * 20), width=2)
        pygame.draw.circle(window, green, v1.position, int(v1.dna[3]), width=1)
        pygame.draw.circle(window, red, v1.position, int(v1.dna[4]), width=1)    




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