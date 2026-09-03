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