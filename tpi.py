# Programación 1

# Trabajo páctico integrador

# Melisa
# Alejandro G. Mazzaforte
import csv
def importar_datos():
    with open('paises.csv', 'r', encoding='utf-8') as file:
        archivo_paises = csv.reader(file)
        
        lista_diccionario_paises = []
        
        for fila in archivo_paises:
            lista_diccionario_paises.append({"nombre":fila[0], "poblacion": int(fila[1]), "superficie": int(fila[2]), "continente":fila[3]})
        return lista_diccionario_paises
    
def menu_principal():
    opciones_validas = ["1", "2", "3", "4","5", "6", "7"]
    while True:
        try:
            print("""
                Elija en el siguiente menú la opcion que necesite..
                    1. Agregar un país.
                    2. Actualizar los datos de Población y Superficie de un País.
                    3. Buscar un país por nombre (coincidencia parcial o exacta).
                    4. Filtrar países por:
                        o Continente.
                        o Rango de población.
                        o Rango de superficie.
                    5. Ordenar países por:
                        o Nombre.
                        o Población.
                        o Superficie (ascendente o descendente).
                    6. Mostrar estadísticas:
                        o País con mayor y menor población.
                        o Promedio de población.
                    7. Para salir del sistema.
        """)

            opcion = input("Elija su opción ")

            if opcion not in opciones_validas:
                raise ValueError(f"'{opcion}' no es válida. Ingrese 1-7") 
              
            return opcion
        
        except ValueError as e:
            print(f"Error {e}")
            input("Presione Enter para continuar")
        
def menu_filtrar_paises():
    #Submenú para compra/venta
    opciones_validas = ["1", "2", "3", "4"]
    while True:
        try:
            print("""
                  --- Criterios de filtrado de paises ---
                    1. Continente
                    2. Rango de población
                    3. Rango de superficie
                    4. Volver al menu principal

                  """)            
            filtro = input("Seleccione: ").strip()
            
            if filtro not in opciones_validas:
                raise ValueError(f"'{filtro}' no es válida. Ingrese 1-3")            
            return filtro            
        except ValueError as e:
            print(f" Error: {e}")
            input("Presione Enter para continuar...")



def main():

    lista_diccionario_paises = []
    print("""
    Bienvenido al sistema de análisis geográfico mundial
    """)
    lista_diccionario_paises = importar_datos()
    return lista_diccionario_paises

main()
