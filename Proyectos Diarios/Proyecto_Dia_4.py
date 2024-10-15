
nombre=input("Para comenzar el juego ingrese su nombre: ")
numero_elegido=int(input(f"Bueno, {nombre}, he pensado un numero del 1 al 100. Tienes ocho intentos para adivinarlo, comienza ingresando el primer numero: "))

intentos=1

while True:
    if numero_elegido < 1 or numero_elegido >100:
        print("Asegúrate de escribir un número entre 0 y 100")
        numero_elegido = int(input("Introduce un número valido: "))  

    if numero_elegido > 0 and numero_elegido < 100:
        break


from random import *
num_azar = randint(1,100)



while True:
    if numero_elegido > num_azar:
        print("Tu numero es mayor al que pienso, ingresa un numero menor.")
        numero_elegido = int(input("Introduce un número menor: ")) 
        intentos=intentos+1
    if numero_elegido < num_azar:
        print("Tu numero es menor al que pienso, ingresa un numero mayor.")
        numero_elegido = int(input("Introduce un número mayor: ")) 
        intentos=intentos+1
    if numero_elegido==num_azar:
        print(f"Ganaste, el numero que habia que adivinar era el {num_azar}! Lo lograste en {intentos} intentos!")
        break
    if intentos==8:
        print("Se te acabaron los intentos :(")
        break