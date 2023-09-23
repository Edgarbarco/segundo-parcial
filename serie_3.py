#Plantear una funcion que reciba un string en mayusculas o minusculas y una letra, luego el programa 
#debe indicarle cuantas veces se encuentra la letra dentro del string ingresado

def contar_letras(string, letra):
    string = string.lower()
    letra = letra.lower()

    cantidad = string.count(letra)
    
    return cantidad

entrada = input("Ingrese una cadena de texto: ")
letra_buscar = input("Ingrese una letra: ")

resultado = contar_letras(entrada, letra_buscar)
print(f"La letra '{letra_buscar}' aparece {resultado} veces en la cadena ingresada.")
