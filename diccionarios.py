# diccionarios#
# Relacion Clave-Valor 
# Puede mezclar diversos tipos de datos, str, int, float.
my_dict = dict()
my_other_dict = {}

print(type(my_dict))

my_dict = {'nombre': 'Lucas', 'Apellido': 'Monzon', 'edad': '29', 
           1: 'python'}

my_other_dict = {'nombre': 'Lucas', 'Apellido': 'Monzon', 'edad': '29', 
                 'lenguajes': {'python', 'kotlin', 'sqs'}}

print(my_dict)
print(my_other_dict)
print(len(my_dict))
print(my_dict['nombre'])
print(my_dict[1]) #se representa como entero sin comillas.

my_dict['calle'] = 'Calle123'  # se agregan elementos al diccionario
print(my_dict)

del my_dict['calle']  # se eliminan claves del diccionario
print(my_dict)

print('Monzon' in my_dict)  # imprime solo la clave, asique arroja false
print('Apellido' in my_dict)

print(my_dict.items())  # Listado con cada uno de los items
print(my_dict.keys())  # listado de claves
print(my_dict.values())  # listado de valores
print(my_dict.fromkeys(('nombre', 1, 'sobrenombre')))  # Muestra claves sin valores

my_new_dict = dict.fromkeys(my_dict)  # se puede crear un diccionario vacio con las claves del diccionario viejo
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, ('Lucas', 'Monzon'))  # agrega el mismo datos a todas las claves. NO permite generar claves individuales
print(my_new_dict)