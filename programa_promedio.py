#Desarrollar un programa que por linea de comandos debe recibir N cantidad de valores 
#separados por comas y el programa debe devolver la suma y el promedio de todo el conjunto, 
#tanto la suma como el promedio debe estar escritos como funciones.

import sys

def calcular_suma(valores):
    return sum(valores)

def calcular_promedio(valores):
    if len(valores) == 0:
        return 0
    else:
        return sum(valores) / len(valores)

def main():
    if len(sys.argv) < 2:
        print("Uso: python programa.py valor1,valor2,valor3,...")
        return

    valores_str = sys.argv[1]
    valores = [float(valor) for valor in valores_str.split(",")]

    suma = calcular_suma(valores)
    promedio = calcular_promedio(valores)

    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")

if __name__ == "__main__":
    main()
