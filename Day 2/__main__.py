from random import randint

sorte = randint(1, 21)
in_user = int()
intentos = 8
nombre = str(input("Digite su nombre: "))

while in_user != sorte or intentos > 0:
    in_user = int(input("Ingrese un numero del 1 al 20: "))
    if in_user > 20 or in_user < 1:
        print(f"Numero fuera de rango, intentos restantes {intentos - 1}")

    elif in_user > sorte:
        print(f"Sorte es menor, intentos restantes {intentos - 1}")

    elif in_user < sorte:
        print(f"Sorte es mayor, intentos restantes {intentos - 1}")

    elif in_user == sorte:
        print("Ganador")
        break
    intentos -= 1
    pass
