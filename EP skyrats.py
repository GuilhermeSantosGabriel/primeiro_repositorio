from cmath import sqrt
import random
import math


def trajectory(x_init, y_init,x_goal, y_goal, trajectory_type):
    match trajectory_type:
        case "trajetoria retilinea":
            distance_sqrt = (x_goal - x_init)^2 + (y_goal - y_init)^2
            distance = sqrt(distance_sqrt)
            return distance
        case "trajetoria manhattan":
            distance = abs(x_init - x_goal) + (y_init - y_goal)
            return distance
        case "trajetoria circular":
            distance = 1
            return distance
#ainda não sei fazer a trajetoria cirular, favor ver depois

def choose_environment():
    environments = ["Floresta", "Cidade", "Deserto"]
    chosen_environment = environments[random.randint(0,2)]
    print("Ambiente randomizado: ", chosen_environment)

    #ordem: trajetoria, velocidade, altura
    match chosen_environment:
        case "Floresta":
            return ("trajetoria circular", 5, 5)
        case "Cidade":
            return ("trajetoria manhattan", 3, 10)
        case "Deserto":
            return ("trajetoria retilia", 8, 3)

def change_pos():


def main():
    print("Olá! Bem vindo a esse programa!")
    drone = input("Qual drone estaremos voando?")
    print("De onde o drone partirá?")
    x_init = float(input("x:"))