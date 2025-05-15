months =['January', 'February', 'March']
print (months)

#Acceder a un elemento de la lista
print (months [0])

#ordenar los elementos alfabéticamente
months.sort()
print (months)

ActualMonth = f'We are in {months [2]}'
print(ActualMonth)

#Modificar un valor de la lista
months [2]= 'April'
print (months)

#Agregar un elemento a la lista
months.append('May')
print (months)

#Eliminar un elemento de la lista
del months [2]
print (months)

#eliminar el último elemento de la lista
months.pop()
#Eliminar el elemento 3
#months.pop(3)
print (months)
