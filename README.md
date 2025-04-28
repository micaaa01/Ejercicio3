# Ejercico 3

## Descripción
Este programa implementa una serie de funciones para resolver problemas comunes relacionados con matrices, intervalos, listas ligadas y arreglos. El programa incluye un menú interactivo que permite al usuario seleccionar y ejecutar cada una de las funciones.

## Funcionalidades
El programa incluye las siguientes funcionalidades:

### Modificar matriz (convertir filas y columnas en 0):

Dada una matriz, si una celda contiene un 0, convierte toda la fila y columna correspondiente en ceros.
Entrada: Una matriz rectangular (lista de listas de enteros).
Salida: La matriz modificada.

### Combinar intervalos:

Une intervalos sobrepuestos en una lista de intervalos.
Entrada: Una lista de intervalos (pares de enteros).
Salida: Una lista de intervalos combinados.

### Verificar ciclo en lista ligada:

Determina si una lista ligada contiene un ciclo.
Entrada: Una lista ligada creada a partir de nodos.
Salida: True si hay un ciclo, False en caso contrario.

### Encontrar número único en arreglo:

Encuentra el único número que aparece una vez en un arreglo donde todos los demás números aparecen exactamente dos veces.
Entrada: Un arreglo de enteros.
Salida: El número único.

### Salir:

Finaliza la ejecución del programa.

## Requisitos
- Python 3.x: Asegúrate de tener Python 3 instalado en tu sistema.
- Sistema operativo: El programa es compatible con cualquier sistema operativo que soporte Python (Windows, macOS, Linux).

## Cómo ejecutar el programa

1. Abre una terminal o línea de comandos.
2. Navega al directorio donde se encuentra el archivo Ejercicio3.py.
3. Ejecuta el programa con el siguiente comando:
``` py 
python3 Ejercicio3.py
```

## Uso del menú

El programa presenta un menú interactivo con las siguientes opciones:

### Opción 1: Modificar matriz

- Introduce el número de filas de la matriz.
- Introduce cada fila de la matriz separando los números con espacios.
Ejemplo de entrada:
``` 
¿Cuántas filas tiene la matriz?: 3
Fila 1 (separar números con espacio): 1 1 1
Fila 2 (separar números con espacio): 1 0 1
Fila 3 (separar números con espacio): 1 1 1
```
``` 
Matriz modificada:
[1, 0, 1]
[0, 0, 0]
[1, 0, 1]
```
### Opción 2: Combinar intervalos

Introduce el número de intervalos.
Introduce cada intervalo como dos números separados por un espacio.
Ejemplo de entrada:
``` 
¿Cuántos intervalos quieres ingresar?: 4
Introduce el intervalo (inicio fin): 1 3
Introduce el intervalo (inicio fin): 2 6
Introduce el intervalo (inicio fin): 8 10
Introduce el intervalo (inicio fin): 15 18
```
Ejemplo de salida:
``` 
Intervalos combinados: [[1, 6], [8, 10], [15, 18]]
```

### Opción 3: Verificar ciclo en lista ligada

Introduce los valores de los nodos de la lista ligada.
Indica si deseas crear un ciclo en la lista.
Ejemplo de entrada:
``` 
Introduce los valores de la lista ligada separados por comas: 3,2,0,-4
¿Quieres crear un ciclo en la lista? (s/n): s
Introduce el índice del nodo al que debe apuntar el último nodo para formar el ciclo (0 basado): 1
```
Ejemplo de slaida:
``` 
¿La lista tiene un ciclo?: True
```

### Opción 4: Encontrar número único en arreglo

Introduce los números del arreglo separados por espacios.
Ejemplo de entrada:
``` 
Introduce los números del arreglo separados por espacio: 4 1 2 1 2
```
Ejemplo de salida:
``` 
El número único es: 4
```
### Opción 5: Salir

Finaliza el programa.

## Estructura del código
- Clase NodoLigado:

Representa un nodo de una lista ligada.

- Atributos:
valor: El valor del nodo.
siguiente: Apuntador al siguiente nodo.

- Clase Ejercicio3:

Contiene las funciones principales para resolver los problemas descritos en el menú.

- Función main:
```
Implementa el menú interactivo y permite al usuario seleccionar las opciones.
--- MENÚ DE EJERCICIOS ---
1. Modificar matriz (convertir filas y columnas en 0)
2. Combinar intervalos
3. Verificar ciclo en lista ligada
4. Encontrar número único en arreglo
5. Salir
Elige una opción (1-5): 4
Introduce los números del arreglo separados por espacio: 4 1 2 1 2
El número único es: 4
```
## Notas
Asegúrate de ingresar los datos en el formato correcto para evitar errores.
Si ingresas una opción no válida, el programa te pedirá que intentes de nuevo.

## Autor
Nombre: Michelle Alanis Navarro Fierro
