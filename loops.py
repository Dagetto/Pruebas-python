### loops/ciclo/bucle ###

# While
my_condition = 0

while my_condition < 10:  # se repite el codigo hasta que se cumple la condicion
    print(my_condition)
    my_condition += 2  # este elemento suma 1 my_condction, hasta que cumple su condicion y deja de ejecutarse.
else:
    print('se cumplio la condicion del inicio')

print('siguiente ejemplo')

while my_condition < 20:  # se repite el codigo hasta que se cumple la condicion
    print(my_condition)
    my_condition += 2

    if my_condition == 14:
     print('la condicion de if se cumple y continua el ciclo')  # se imprime el IF pero continua luego con el while

print('siguiente ejemplo')

while my_condition < 30:  # se repite el codigo hasta que se cumple la condicion
    print(my_condition)
    my_condition += 2
    if my_condition == 24:
        print('la condicion de if se cumple y aparece el break')  # se imprime el IF y luego aparece el break.
        break
print('siguiente ejemplo')

### FOR ###

my_list = [12, 17, 21, 29, 25, 30]

for element in my_list:
    print(element)  # el FOR tiene un numero limitado de repeticiones, se aplica a elementos con la capaicdad de almacenamiento.

print('siguiente ejemplo')

my_tuple = (30, 'Lucas', 'Monzon', 'python')

for element in my_tuple:
    print(element)

my_set = {'Lucas', 'Monzon', '29'}

for element in my_set:
    print(element)

my_dict = {'nombre': 'Lucas', 'Apellido': 'Monzon', 'edad': '29', 
           1: 'python'}
for element in my_dict:  # imprime solo las keys no los valores.
    print(element)
    if element == 'edad':
     break  # se aplica el break y finaliza el codigo
else:
    print('el ejemplo finalizo')

