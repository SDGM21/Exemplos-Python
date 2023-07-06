"""
1 escoger una palabra al azar, retornando su rango y la palabra
2 construir juego, escondiendo la palabra escogida con -,
mostrar las vidas del usuario
3 pedir que el usuario ingrese una letra *valida, letra invalida no quita vidas
4 verificar si la letra existe en la pálabra,
si existe cambiar el - por las letras que correspondan en la palabra
si no existe, restar una vida
5 si el usuario consiguio la palabra mostrar VICTORIA
6 si el usuario no consiguio la palabra y las vidas son igual a 0, mostrar PERDISTE
"""
import time
from random import choice
import os

palabra_escogida = choice(str("""
Aprender un poco cada día marca la diferencia. 
Hay estudios que muestran que los estudiantes que hacen 
del aprendizaje un hábito tienen una mayor probabilidad de 
alcanzar sus objetivos. 
Reserva tiempo para aprender y recibe recordatorios con la 
herramienta de planificación del aprendizaje.
""")
                          .lower()
                          .replace(".", "")
                          .replace("\n", "")
                          .translate(str.maketrans('áéíóúü', 'aeiouu'))
                          .split(" ", -1))


def verificar_letra(letra: str, palabra: str, vidas: int):
    if letra in palabra_escogida:
        for index, value in enumerate(palabra_escogida):
            if value == letra:
                palabra_aux = list(palabra)
                palabra_aux[index] = letra
                palabra = "".join(palabra_aux)
                pass
    else:
        vidas -= 1

    return palabra, vidas


def ahorcado():
    vidas = 6
    palabra_oculta = "-" * len(palabra_escogida)

    while palabra_oculta != palabra_escogida and vidas > 0:
        print(f"Palabra: {palabra_oculta}\n Vidas : {vidas} \n\n")
        letra_ingresada = input("Ingrese una letra: ").lower()

        if letra_ingresada.isalpha():
            palabra_oculta, vidas = verificar_letra(letra_ingresada, palabra_oculta, vidas)
        else:
            print("Ingrese una letra valida!")
            time.sleep(5)
            os.system("cls")

    pass

    if palabra_oculta == palabra_escogida:
        return f"VICTORIA\nPalabra encontrada: {palabra_oculta}\nVidas restantes: {vidas}"
    else:
        return "PERDISTE"


print(ahorcado())
