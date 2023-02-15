'''
Autor: Miguel F. Gil Rivas
Fecha: 14-02-2023
Juego de Piedra, Papel, Tijeras

concepto basico del juego
#piedra gana a tijera
#tijera gana a papel
#papel gana a piedra
'''
import random

option = ("piedra", "papel" ,"tijera")

computer = random.choice(option)
computer_wins = 0
user_wins = 0
rounds = 0
# la opcion .lower() coloca todo el texto en minuscula y la opcion .upper() coloca todo el texto en mayuscula
while (computer_wins <= 2) and (user_wins <= 2):
    print("-"*8)
    print(f"\nROUND {rounds}\nuser_wins: {user_wins} \ncomputer_wins: {computer_wins}\n")
    print("-"*8)
    user = input("Escriba piedra, papel o tijera: ")
    if user.lower() in option:
        rounds +=1
        print(f"usuario: {user.lower()} \nComputer: {computer.lower()}")

        if user.lower() == computer.lower():
            print(f"Empate!")
        elif user.lower() == "tijera":
            if computer.lower() == "piedra":
                print("Gana Computer!")
                computer_wins += 1
            elif computer.lower() == "papel":
                print("Gana User!")
                user_wins += 1
        elif user.lower() == "papel":
            if computer.lower() == "tijera":
                print("Gana Computer!")
                computer_wins += 1
            elif computer.lower() == "piedra":
                print("Gana User!")
                user_wins += 1
        else:
            if computer.lower() == "tijera":
                print("Gana User!")
                user_wins += 1
            elif computer.lower() == "papel":
                print("Gana Computer!")
                computer_wins += 1
    else:
        print("¡La opcion no se encuentra!\nVuelva a Ingresar la Opcion\n")

if user_wins == 3:
    print(f"\nEl ganador es User con {user_wins} partidas despues de {rounds} rondas")
else:
    print(f"\nEl ganador es Computer con {computer_wins} partidas {rounds} rondas")




