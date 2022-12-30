### Condicionales ###

my_condition = True 
if my_condition:
    print('se ejecuta la condicion del if')  # solo se ejecuta si la condicion es true

my_condition = False  # caso opuesto donde no se ejecuta el if
if my_condition:
    print('se ejecuta la condicion del if')

print('la ejecucion continua')

my_condition = 5*2  # se asigna un valor pero  no se determina si es true o false.

if my_condition == 10:  # aca ya si se determina su valor y se define la linea siguiente del if ==10/==11
    print('se ejecuta la condicion del segundo if')

if my_condition > 11:
    print('se ejecuta la condicion del tercer if')  # este caso no se ejecuta porque no cumple la condicion

if my_condition > 10:
    print('es mayor que diez')
else:
    print('es menor o igual que diez')  # se aplica el else al esquema del if. Ejecuta algo si no se cumple la condicion del if

my_condition = 5*3  # ejecuta el else, si fuere 5*5 ejecutaria el if

if my_condition > 10 and my_condition < 20:
    print('es mayor que diez y menor que veinte')

else:
    print('es menor o igual que diez, o es mayor o igual que veinte ')

my_condition = 5*6

if my_condition > 10 and my_condition < 20:
    print('es mayor que diez y menor que veinte')
elif my_condition == 30:
    print('se cumple la condicion del elif')
else:
    print('es menor o igual que diez, o es mayor o igual que veinte ')   # es el valor donde continua el bucle si no se aplica el if o elif.

print('la ejecucion continua')

my_string = ''

if not my_string:
    print('la cadena de texto no tiene un valor asignado')  # se aplica el NOT, de otro modo el codigo no se ejecuta