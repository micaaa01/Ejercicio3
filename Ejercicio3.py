class NodoLigado:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Ejercicio3:

    # Función para hacer cero las filas y columnas en donde se encuentra un cero
    def matriz(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0])

        # Verificamos que la matriz esté bien formada (opcionalmente cuadrada si quieres)
        if any(len(fila) != columnas for fila in matriz):
            raise ValueError("La matriz no es rectangular (todas las filas deben tener el mismo número de columnas)")

        # Verificar si la primera fila y columna tienen ceros
        primer_fila = any(matriz[0][j] == 0 for j in range(columnas))
        primer_columna = any(matriz[i][0] == 0 for i in range(filas))

        # Marcar las filas y columnas que deben ser cero
        for i in range(1, filas):
            for j in range(1, columnas):
                if matriz[i][j] == 0:
                    matriz[0][j] = 0
                    matriz[i][0] = 0

        # Hacer cero las celdas marcadas
        for i in range(1, filas):
            for j in range(1, columnas):
                if matriz[0][j] == 0 or matriz[i][0] == 0:
                    matriz[i][j] = 0

        # Hacer cero la primera fila si es necesario
        if primer_fila:
            for j in range(columnas):
                matriz[0][j] = 0

        # Hacer cero la primera columna si es necesario
        if primer_columna:
            for i in range(filas):
                matriz[i][0] = 0

        return matriz

    def arregloIntervalo(self, intervalos):
        """
        Une intervalos sobrepuestos
        """
        if not intervalos:
            return []

        intervalos.sort(key=lambda x: x[0])
        resultado = [intervalos[0]]

        for inicio, fin in intervalos[1:]:
            ultimo_inicio, ultimo_fin = resultado[-1]
            if inicio <= ultimo_fin:
                resultado[-1][1] = max(ultimo_fin, fin)
            else:
                resultado.append([inicio, fin])

        return resultado

    def listaCiclo(self, cabeza):
        """
        Determina si una lista ligada contiene un ciclo.
        """
        puntero1 = cabeza
        puntero2 = cabeza

        while puntero2 and puntero2.siguiente:
            puntero1 = puntero1.siguiente
            puntero2 = puntero2.siguiente.siguiente

            if puntero1 == puntero2:
                return True
        return False

    def soloUnico(self, arreglo):
        """
        Encuentra el único número que aparece una vez en el arreglo.
        """
        if len(arreglo) < 1 or len(arreglo) > 30000:
            raise ValueError("El arreglo debe tener entre 1 y 30,000 elementos")

        resultado = 0
        for num in arreglo:
            resultado ^= num
        return resultado
def main():
    ejercicio = Ejercicio3()

    while True:
        print("\n--- MENÚ DE EJERCICIOS ---")
        print("1. Modificar matriz (convertir filas y columnas en 0)")
        print("2. Combinar intervalos")
        print("3. Verificar ciclo en lista ligada")
        print("4. Encontrar número único en arreglo")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            matriz = [
                [int(x) for x in input(f"Fila {i+1} (separar números con espacio): ").split()]
                for i in range(int(input("¿Cuántas filas tiene la matriz?: ")))
            ]
            resultado = ejercicio.matriz(matriz)
            print("Matriz modificada:")
            for fila in resultado:
                print(fila)

        elif opcion == "2":
            cantidad = int(input("¿Cuántos intervalos quieres ingresar?: "))
            intervalos = []
            for _ in range(cantidad):
                intervalo = list(map(int, input("Introduce el intervalo (inicio fin): ").split()))
                intervalos.append(intervalo)
            resultado = ejercicio.arregloIntervalo(intervalos)
            print("Intervalos combinados:", resultado)

        elif opcion == "3":
            # Creamos una lista ligada básica para probar
            nodos = [NodoLigado(i) for i in range(5)]
            for i in range(4):
                nodos[i].siguiente = nodos[i+1]

            hacer_ciclo = input("¿Quieres crear un ciclo en la lista? (s/n): ")
            if hacer_ciclo.lower() == 's':
                nodos[4].siguiente = nodos[1]  # conecta el último nodo con el segundo

            resultado = ejercicio.listaCiclo(nodos[0])
            print("¿La lista tiene un ciclo?:", resultado)

        elif opcion == "4":
            arreglo = list(map(int, input("Introduce los números del arreglo separados por espacio: ").split()))
            resultado = ejercicio.soloUnico(arreglo)
            print("El número único es:", resultado)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta otra vez.")

if __name__ == "__main__":
    main()
