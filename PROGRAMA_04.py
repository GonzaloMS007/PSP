import math

def calcular_tamano_relativo(datos):
    # Transforma los valores en un arreglo de logaritmos naturales
    tamanos_ln = [math.log(value) for value in datos.values()]
    # Calcula la media de los logaritmos naturales
    media = sum(tamanos_ln) / len(tamanos_ln)
    # Calcula la varianza de los logaritmos naturales
    varianza = sum((x - media) ** 2 for x in tamanos_ln) / (len(tamanos_ln) - 1)
    # Calcula la desviación estándar (sigma) a partir de la varianza
    sigma = math.sqrt(varianza)
    # Crea un nuevo diccionario llamado rangos_ln con categorías VS, S, M, L y VL basadas en la media y sigma
    rangos_ln = {
        "VS": media - 2 * sigma,
        "S": media - sigma,
        "M": media,
        "L": media + sigma,
        "VL": media + 2 * sigma
    }
    # Crea un nuevo diccionario llamado rangos que contiene los tamaños relativos reales
    rangos = {key: round(math.exp(value), 4) for key, value in rangos_ln.items()}
    # Retorna el diccionario de tamaños relativos
    return rangos

def main():
    # Crear un diccionario llamado datos_loc_metodo para almacenar datos relacionados con LOC/Método
    datos_loc_metodo = {
        "cada_caracter": 18.0 / 3.0,
        "lectura_cadena": 18.0 / 3.0,
        "caracter_individual": 25.0 / 3.0,
        "cada_linea": 31.0 / 3.0,
        "caracter_solo": 37.0 / 3.0,
        "constructor_cadena": 82.0 / 5.0,
        "gestor_cadena": 82.0 / 4.0,
        "grupo_lista": 87.0 / 4.0,
        "recorte_lista": 89.0 / 4.0,
        "decrementador_cadena": 230.0 / 10.0,
        "Caracter": 85.0 / 3.0,
        "Carácter": 87.0 / 3.0,
        "Convertidor": 558.0 / 10.0
    }

    # Crear un diccionario llamado datos_pags_capitulo para almacenar datos relacionados con Páginas/Capítulo
    datos_pags_capitulo = {
        "Prefacio": 7,
        "Capítulo 1": 12,
        "Capítulo 2": 10,
        "Capítulo 3": 12,
        "Capítulo 4": 10,
        "Capítulo 5": 12,
        "Capítulo 6": 12,
        "Capítulo 7": 12,
        "Capítulo 8": 12,
        "Capítulo 9": 8,
        "Apéndice A": 8,
        "Apéndice B": 8,
        "Apéndice C": 20,
        "Apéndice D": 14,
        "Apéndice E": 18,
        "Apéndice F": 12
    }

    # Calcular los tamaños relativos para datos_loc_metodo y almacenar los resultados en un nuevo diccionario
    resultado_datos_loc_metodo = calcular_tamano_relativo(datos_loc_metodo)

    # Calcular los tamaños relativos para datos_pags_capitulo y almacenar los resultados en un nuevo diccionario
    resultado_datos_pags_capitulo = calcular_tamano_relativo(datos_pags_capitulo)

    # Imprimir los resultados para datos_loc_metodo
    print("Datos LOC/Método:")
    for clave in ["VS", "S", "M", "L", "VL"]:
        print(f"LOC/Método: {clave} = {resultado_datos_loc_metodo[clave]}")

    # Imprimir los resultados para datos_pags_capitulo
    print("\nDatos Páginas/Capítulo:")
    for clave in ["VS", "S", "M", "L", "VL"]:
        print(f"Páginas/Capítulo: {clave} = {resultado_datos_pags_capitulo[clave]}")

if __name__ == "__main__":
    main()
