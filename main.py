import pygame
import numpy
import random

#from pygame.transform import average_color
from vehicle import *
from values import *
from functions import *

pygame.init()

# Dots green : Food
# Dots red : Poison
t_major = 0
v_major = Vehicle(0, 0)
relogio = pygame.time.Clock()
window = pygame.display.set_mode((largura, altura))
#window2 = pygame.display.set_mode((int(largura/4), int(altura/4)))
pygame.display.set_caption("Evolutionary Steering Behaviors")
window.fill(gray)
print('generation,peso food,peso poison,raio food,raio poison,average life time,average fitness')
# Constroi o tapete de sierpinski
walls = sierpinski_carpet(active=False)

vehicles_list = create_vehicles(300)

food = create_food(300)

poison = create_poison(300)

continua = True
while continua and number_of_generation <= max_generation:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            continua = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continua = False
            if event.key == pygame.K_f:
                food = add_food(50, food)
            if event.key == pygame.K_p:
                poison = add_posion(50, poison)
            if event.key == pygame.K_v:
                vehicles_list = add_vehicles(50, vehicles_list)
            if event.key == pygame.K_d:
                dna_view = not dna_view
            if event.key == pygame.K_r:
                vehicles_list, food, poison = new_generation()
                t = 0
            if event.key == pygame.K_l:
                fps -= 60
            if event.key == pygame.K_s:
                fps += 60
            if event.key == pygame.K_m:
                life_times = []
                for i in range(len(vehicles_list)):
                    v = vehicles_list[i]
                    life_times.append(v.life_time)
                i_max = life_times.index(max(life_times))
                v_major2 = vehicles_list[i_max]
                print(f'Tempo de vida: {v_major2.life_time}')
                print(f'food peso: {v_major2.dna[0]} || raio food: {v_major2.dna[3]}')
                print(f'poison peso: {v_major2.dna[1]} || raio poison: {v_major2.dna[4]}')
                
        #target = pygame.mouse.get_pos()
        
    window.fill(gray)
    #pygame.draw.line(window, black, (tamanho_barra, 0), (tamanho_barra, altura), width=3)

    #TODO: Function Insert food
    insert_food(0.4, food)

    #TODO: Function Insert posion
    insert_poison(0.4, poison)
    
    #TODO: Projeto final
    if t >= t_max or len(vehicles_list) == 0:
        #vehicles_list, food, poison = new_generation()
        #vehicles_list, food, poison = add_vehicles(50 - len(vehicles_list), vehicles_list), add_food(50 - len(food), food), add_posion(50 - len(poison), poison)
        resto = len(vehicles_list)
        total_life_time += t_max * resto
        total_generation += resto
        for i in range(resto):
            v1 = vehicles_list[i]
            total_dna[0] += v1.dna[0]
            total_dna[1] += v1.dna[1]
            total_dna[3] += v1.dna[3]
            total_dna[4] += v1.dna[4]
            total_fitness += v1.fitness
        total_dna[0] /= total_generation
        total_dna[1] /= total_generation
        total_dna[3] /= total_generation
        total_dna[4] /= total_generation
        average_life_time = total_life_time / total_generation  
        average_fitness = total_fitness / total_generation
        print(f'{number_of_generation},{total_dna[0]},{total_dna[1]},{total_dna[3]},{total_dna[4]},{average_life_time},{average_fitness}')
        '''vehicles_list = pick_best_return_new(vehicles_list, 300)
        food = create_food(300)
        poison = create_poison(300)'''
        vehicles_list, food, poison = new_generation(300, 300, 300)

        total_dna = [0] * 6
        total_generation = 0
        total_life_time = 0
        total_fitness = 0
        t = 0
        
        number_of_generation += 1
    t += 1

    i = 0
    while i < len(vehicles_list):

        v1 = vehicles_list[i]
        v1.behaviors(food, poison, walls)
        v1.update()

        newVehicle = v1.clone(0.000001) # Argument is probability to clone
        if newVehicle != None:
            vehicles_list.append(newVehicle)

        # to_draw_vehicle_picture
        to_draw_vehicle_picture(v1, vehicles, window)
        '''health_i = round(v1.health) + 1
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
        
        window.blit(vehicles[health_i], rect)'''
        #################

        #to_draw_vehicle_polygon(v1, window)

        to_draw_dna(window, v1, dna_view)
        #print(v1.health)

        if v1.dead():
            food.append(v1.position)
            '''for i in range(6):
                total_dna[i] += v1.dna[i]'''
            total_dna[0] += v1.dna[0]
            total_dna[1] += v1.dna[1]
            total_dna[3] += v1.dna[3]
            total_dna[4] += v1.dna[4]
            total_life_time += v1.life_time
            total_generation += 1
            total_fitness += v1.fitness
            # Avaliar se precisa
            '''if v1.life_time > t_major:
                t_major = v1.life_time
                v_major = v1'''
            del(vehicles_list[i])
        i += 1

    '''texto(f"V1: Health={velocidade:.7f} Dna={}", white, 20, 10, altura - 80)
    texto(f"V2: {velocidade:.7f}", white, 20, 10, altura - 60)
    texto(f"V3: {min(p1.distancias):.5f}", white, 20, 10, altura - 40)
    texto(f"V4: {max(p1.distancias):.5f}", white, 20, 10, altura - 20)'''

    show_environment(window, walls, food, poison)

    '''texto(window, f"Numero de vehicles: {len(vehicles_list)}", white, 20, 10, altura - 120)
    texto(window, f"Geração: {number_of_generation}", white, 20, 10, altura - 100)
    texto(window, f"Maior tempo de vida: {v_major.life_time} ", white, 20, 10, altura - 80)
    texto(window, f'food peso: {v_major.dna[0]} || raio food: {v_major.dna[3]}', white, 20, 10, altura - 60)
    texto(window, f'poison peso: {v_major.dna[1]} || raio poison: {v_major.dna[4]}', white, 20, 10, altura - 40)
    texto(window, f"Tempo atual: {t} || Tempo maximo: {t_max} || fps: {fps}", white, 20, 10, altura - 20)'''

    relogio.tick(fps)
    pygame.display.update()

pygame.quit()
'''
    Tempo de vida: 3836
    dna_food peso: 1.9922644193998096 || dna_raio_food: 63.95870245480027
    dna_poison peso: -1.1600502475317431 || dna_raio_poison: 52.61828340020249
'''