#Ejemplos de CONDICIONALES
#Se utiliza la funcion INPUT para introducir valores por teclado.

# Condicional IF
sueldo=int(input('introduce el sueldo:'))
if sueldo >3000:print('el usuario debe pagar un porcentaje en impuestos')
if sueldo <=3000:print ('el usuario no debe pagar impuestos') #operador de comparacion

#ej:operador logico se tiene que cumplir las dos condiciones
if sueldo >6000 and sueldo <10000: print ('el usuario tiene que pagar una bonificacion de 1000 euros')
#ej: operador logico solo se tiene que cumplir una de las condiciones
if sueldo ==20000 or sueldo==30000:print ('el usuario paga un 10 por ciento de su sueldo')


