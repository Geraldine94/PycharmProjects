#1. creamos la función, con un parámetro
def information (name):
    #cuerpo de la función. el indentado es obligatorio
    return name

#2. llamamos a la función y le pasamos un argumento
employee = information('Geraldine')
print(employee)

def information2 (name2, job = 'unknown'):
    print (f'I am {name2} and my occupation is {job}')

information2 ('Geraldine', 'tester')
information2 ('Berenice', 'functional analyst')
information2 (name2 = 'Ana María')

#Definimos una función sin parámetros
def sum ():
    print (2+2)

#y la llamamos sin argumentos
sum()

#Imprimimos una suma a través de una función
def sum2(a = 0, b = 0):
    print (a+b)

sum2(2, 3)
sum2(4, 1)
sum2 (8)