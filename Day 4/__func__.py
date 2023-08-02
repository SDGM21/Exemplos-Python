import msvcrt
from pathlib import Path
import os


def listar_archivos(carpeta):
    ruta = sorted(
        Path.joinpath(Path(os.path.dirname(os.path.abspath(__file__))), "Recetas").glob(
            "**/*.*"
        )
    )

    archivos = list()
    for arch in ruta:
        archivos.append(arch.name)
        pass

    return archivos


def elegir_opcion(opciones):
    seleccion = 0
    while True:
        print("\033[2J\033[H")  # Limpiar la consola

        for i, opcion in enumerate(opciones):
            if i == seleccion:
                print(f"> {opcion}")
            else:
                print(f"  {opcion}")
        pass

        tecla = msvcrt.getch()
        if tecla == b"\xe0":  # Flecha especial
            tecla = msvcrt.getch()
            if tecla == b"H":  # Flecha arriba
                seleccion = seleccion - 1
            elif tecla == b"P":  # Flecha abajo
                seleccion = seleccion + 1
        elif tecla == b"\r":  # Enter
            print(opciones[seleccion])
            return opciones[seleccion]
