#from hashlib import new
import pygame
import math
import random
from values import *

class Particle:
    def __init__(self, x=0, y=0):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        self.acceleration = pygame.Vector2()
    
    def applyForce(self, force):
        self.acceleration += force

    def limit(self, limit_value, vector):
        if vector.magnitude_squared() > limit_value * limit_value:
            return (vector.normalize()) * limit_value
        else:
            return vector

    def update_move(self, maxspeed=20):
        self.velocity += self.acceleration

        # Limit is maxspeed
        self.velocity = self.limit(maxspeed, self.velocity)

        # Update location with new velocity
        self.position += self.velocity

        # Boundary condition (depende da posição)
        #self.periodic_boundary()
        
        # Set zero acceleration
        self.acceleration = self.acceleration * 0

    def seek(self, target):
        # Calculate desired
        desired = target - self.position
        desired = desired.normalize() * self.maxspeed

        # Calculate steer (Craig Raynolds classic vehicle)
        # steering = desired - velocity
        steer = desired - self.velocity

        # Limit steer
        steer = self.limit(self.maxforce, steer)

        return steer

    
class Vehicle(Particle):
    def __init__(self, x=0 , y=0, dna=[], flag_predator=False):
        super().__init__(x, y)
        self.predator = flag_predator
        self.r = 0.8
        v0_max = 4
        self.maxforce = 0.2
        self.health = 4
        self.life_time = 1
        self.food_ate = 0
        self.poison_ate = 0
        self.fitness = 0
        kf_max = 3
        kp_max = 3
        Rf_max = 100
        Rp_max = 100
        mr = 0.01
        if dna == []:
            # Peso food
            A = random.uniform(-kf_max, kf_max)
            # Peso poison
            B = random.uniform(-kp_max, kp_max)
            # Peso predator
            C = random.uniform(-3, 3)
            # Food Perception
            D = random.uniform(10, Rf_max)
            # Poison Perception
            E = random.uniform(10, Rp_max)
            # Predator Perception
            F = random.uniform(10, Rp_max)
            self.dna = [A, B, C, D, E, F]
            #self.skin = round(a + b)
            #print(self.skin)
        else:
            self.dna = []
            self.dna.append(dna[0])
            #TODO: Diminuir codigo
            if random.random() < mr:
                self.dna[0] += random.uniform(-0.2, 0.2)
                if self.dna[0] < -3:
                    self.dna[0] = -3
                elif self.dna[0] > 3:
                    self.dna[0] = 3

            self.dna.append(dna[1])
            if random.random() < mr:
                self.dna[1] += random.uniform(-0.2, 0.2)
                if self.dna[1] < -3:
                    self.dna[1] = -3
                elif self.dna[1] > 3:
                    self.dna[1] = 3
            
            self.dna.append(dna[2])
            if random.random() < mr:
                self.dna[2] += random.uniform(-0.2, 0.2)
                if self.dna[2] < -3:
                    self.dna[2] = -3
                elif self.dna[2] > 3:
                    self.dna[2] = 3

            self.dna.append(dna[3])
            if random.random() < mr:
                self.dna[3] += random.uniform(-30, 30)
                if self.dna[3] < 10:
                    self.dna[3] = 10
                elif self.dna[3] > 150:
                    self.dna[3] = 150

            self.dna.append(dna[4])
            if random.random() < mr:
                self.dna[4] += random.uniform(-30, 30)
                if self.dna[4] < 10:
                    self.dna[4] = 10
                elif self.dna[4] > 150:
                    self.dna[4] = 150

            self.dna.append(dna[5])
            if random.random() < mr:
                self.dna[5] += random.uniform(-30, 30)
                if self.dna[5] < 10:
                    self.dna[5] = 10
                elif self.dna[5] > 150:
                    self.dna[5] = 150
        self.maxspeed = 4
                
    def is_predator(self):
        return self.predator

    def behaviors(self, good, bad, wall):
        steerG = self.eat(good, 0.5, self.dna[3])
        steerB = self.eat(bad, -1.0, self.dna[4])
        steerW = self.eat(wall, -0.5, self.dna[5], True)

        steerG *= self.dna[0] / 1.5
        steerB *= self.dna[1] / 1.5
        steerW *= self.dna[2] / 1.5

        self.applyForce(steerG)
        self.applyForce(steerB)
        self.applyForce(steerW)

    def clone(self, z):
        if random.random() < z:
            return Vehicle(self.position.x, self.position.y, self.dna)
        else:
            return None

    def eat(self, lista, nutrition, PerceptionRadius, flagWall=False):
        # list of foods
        record = largura
        record_2 = record * record
        Radius_eat = self.maxspeed + 2
        closest = None

        # List of food
        i = 0
        #for i in range(len(lista)):
        while i < len(lista):
            d_2 = (lista[i] - self.position).magnitude_squared()
            if d_2 < Radius_eat * Radius_eat:
                if not flagWall:
                    lista.pop(i)
                self.health += nutrition
                if nutrition > 0:
                    self.food_ate += 1
                else:
                    self.poison_ate += 1
                self.fitness = (self.food_ate - self.poison_ate) * (self.food_ate - self.poison_ate)#/self.life_time
                if self.health >= 6:
                    self.health = 6
            elif d_2 < record_2 and d_2 < PerceptionRadius * PerceptionRadius:
                record_2 = d_2
                closest = lista[i]
            i += 1
        # Eat food and remove food of list
        if closest != None:
            return self.seek(closest)
        return pygame.Vector2()
        
    #TODO: Projeto final
    def dead(self):
        return self.health < 0

    #TODO: Projeto final
    # Update location
    def update(self):

        self.health -= 0.005

        self.life_time += 1

        # Boundary condition (depende da aceleração)
        self.boundary()

        # Atualização a movimentação mecânica
        self.update_move(self.maxspeed)

    def boundary(self):
        d = 15
        desired = pygame.Vector2()
        if self.position.x < d:
            desired = pygame.Vector2(self.maxspeed, self.velocity.y)
        elif self.position.x > largura - d:
            desired = pygame.Vector2(-self.maxspeed, self.velocity.y)
        if self.position.y < d:
            desired = pygame.Vector2(self.velocity.x, self.maxspeed)
        elif self.position.y > altura - d:
            desired = pygame.Vector2(self.velocity.x, -self.maxspeed)

        if desired.magnitude_squared() > 0:
            desired = desired.normalize() * self.maxspeed
            steer = desired - self.velocity
            steer = self.limit(self.maxforce, steer)
            self.applyForce(steer)
    
    def wall(self, lista_de_vetores):
        d = 10
        d_2 = d * d
        desired = pygame.Vector2()
        for wall in lista_de_vetores:
            vector_d = wall - self.position
            distance_to_wall_2 = (vector_d).magnitude_squared()
            if distance_to_wall_2 < d_2:
                desired = vector_d.normalize()

            if desired.magnitude_squared() > 0:
                desired = desired.normalize() * self.maxspeed
                steer = desired - self.velocity
                steer = self.limit(self.maxforce, steer)
                self.applyForce(-steer)

    # TODO: Projeto final
    def periodic_boundary(self):
        self.position.x = self.position.x % largura
        self.position.y = self.position.y % altura


class Predator(Vehicle):
    pass

# REFACTOR LATER
def pick_best_return_new(population, length_new):
    new_population = []
    for j in range(length_new):
        Y = random.choice(population)
        X = random.choice(population)
        X_dna = X.dna
        Y_dna = Y.dna
        new_dna = crossover_simple(X_dna, Y_dna)
        new_population.append(Vehicle(random.randint(1, largura), random.randint(1, altura), new_dna))
    #new_population = mutation(new_population)
    return new_population

def fitness():
    pass

def selection():
    pass

def mutation():
    pass

# TODO
def crossover(X_dna, Y_dna):
    alfa = random.random()
    new_dna = [0] * 6
    for i in range(6):
        alfa = random.random()
        new_dna[i] = alfa * X_dna[i] + (1 - alfa) * Y_dna[i]
    return new_dna

# TODO
def crossover_simple(X_dna, Y_dna):
    alfa = random.random()
    i = random.randint(0, 5)
    base = random.choice([X_dna, Y_dna])
    base[i] = alfa * X_dna[i] + (1 - alfa) * Y_dna[i]
    new_dna = base
    return new_dna

# TODO: Outros crossovers


def evolutionary(vehicles):
    pass

# TODO
def create_vehicles(n):
    return [Vehicle(random.randint(1, largura), random.randint(1, altura)) for i in range(n)]

# TODO
def add_vehicles(n, vehicles_list):
    if n < 0:
        n = 0
    for i in range(n):
        vehicles_list.append(Vehicle(random.randint(1, largura), random.randint(1, altura)))
    return vehicles_list