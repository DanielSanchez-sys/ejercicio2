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


# ROMAN ZEBALLOS DYLAN ROBERTO
numero = float(input("Ingresa el número al que deseas sacarle la raíz: "))
indice = float(input("Ingresa el índice de la raíz (ej: 2 para cuadrada, 3 para cúbica): "))
if numero < 0 and indice % 2 == 0:
    import cmath
    resultado = cmath.sqrt(numero) if indice == 2 else numero ** (1 / indice)
    print(f"El resultado es un número complejo: {resultado}")
else:
    resultado = numero ** (1 / indice)
    print(f"La raíz {indice} de {numero} es: {resultado}")



