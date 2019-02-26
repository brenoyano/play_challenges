A = float(input())
B = float(input())
C = float(input())
pi = 3.14159

TRIANGULO = (A*C)/2
CIRCULO = pi*C**2
TRAPEZIO = ((A+B)*C)/2
QUADRADO = B*B
RETANGULO = A*B

print('TRIANGULO: '+'{0:.3f}'.format(TRIANGULO))
print('CIRCULO: '+'{0:.3f}'.format(CIRCULO))
print('TRAPEZIO: '+'{0:.3f}'.format(TRAPEZIO))
print('QUADRADO: '+'{0:.3f}'.format(QUADRADO))
print('RETANGULO: '+'{0:.3f}'.format(RETANGULO))
