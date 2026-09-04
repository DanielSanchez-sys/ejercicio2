import math

def formula_general(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        return "No tiene soluciones reales"
    
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    
    return x1, x2
   # ALEJANDRO SOLIZ GONZALES

def potencia(base, exponente):
    return base ** exponente

if __name__ == "__main__":
    b = float(input("Ingresa la base: "))
    e = float(input("Ingresa el exponente: "))
    print(f"Resultado: {potencia(b, e)}")

# JOSE DANIEL SANCHEZ MAMANI


def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado
    
# DIEGO RAFAEL MANCILLA FLORES

def resta(a, b):
    return a - b

# DYANA VILLARROEL CHOQUE
def suma(a, b):
    return a + b 

# DAYANA IBARRA ZARATE

def logaritmo_natural(x):
    if not isinstance(x, (int, float)):
        return "El valor debe ser un número"

    if x <= 0:
        return "El logaritmo natural solo está definido para números positivos"

    return math.log(x)

# GABRIEL BAZUALDO ROJAS

def suma_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "las matirces deben tener el mismo tamaño"

    filas = len(matriz1)
    columnas = len(matriz1[0])
    
    resultado = []
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            fila_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila_resultado)
    return resultado

if __name__ == "__main__":
    filas = int(input("Numero de filas de las matrices: "))
    columnas = int(input("Numero de columnas de las matrices: "))
    print("Escribe cada fila con los numeros separados por espacio (ej: 1 2 3)")
    matriz_a = [list(map(float, input(f"Matriz A - Fila {i+1}: ").split())) for i in range(filas)]
    matriz_b = [list(map(float, input(f"Matriz B - Fila {i+1}: ").split())) for i in range(filas)]
    print("Resultado de la suma:", suma_matrices(matriz_a, matriz_b))

# VICENTE SILVESTRE VELASQUEZ 

def division(dividendo, divisor):
    if divisor == 0:
        return "No se puede dividir entre cero"
    
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    
    return cociente, residuo

if __name__ == "__main__":
    a = int(input("Ingresa el dividendo (entero): "))
    b = int(input("Ingresa el divisor (entero): "))
    
    resultado = division(a, b)
    
    if isinstance(resultado, str):
        print(resultado)
    else:
        cociente, residuo = resultado
        print(f"Cociente: {cociente}, Residuo: {residuo}")

# HEIDY JHAEL FLORES TIÑINI

a = 5
b = 3
resultado = a * b
print(resultado)  
# DEYNA YARA CHOQUE LIMACHI

numero = float(input("Ingresa el número al que deseas sacarle la raíz: "))
indice = float(input("Ingresa el índice de la raíz (ej: 2 para cuadrada, 3 para cúbica): "))

if numero < 0 and indice % 2 == 0:
    import cmath
    resultado = cmath.sqrt(numero) if indice == 2 else numero ** (1 / indice)
    print(f"El resultado es un número complejo: {resultado}")
else:
    resultado = numero ** (1 / indice)
    print(f"La raíz {indice} de {numero} es: {resultado}")

# DYLAN ROBERTO ROMAN ZEBALLOS