import math

def formula_general(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        return "No tiene soluciones reales"
    
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    
    return x1, x2

   # ALEJANDRO SOLIZ GONZALES