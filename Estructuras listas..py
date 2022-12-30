'''ESTRUCTURAS DE DATOS TIPO LISSTA, PERMITE ALMACENAR UNA COLECCION DE DATOS Y LUEGO ACCEDER POR MEDIO DE SUBINDICE.
PARA CREAR UNA LISTA DEBEMOS INDICAR SUS ELEMENTOS ENCERRADOS ENTRE CORCHETES Y SEPARADOS POR COMAS:
LISTA=[10.6,20,] LISTA DE ENTEROS
LISTA= [2.8,2.9.3.7] LISTA DE FLOAT
LISTA=['CARLOS', 'PEPE', 'JUAN'] LISTA DE STRING
LISTA= ['CARLOS', 2.8, 30] LISTA DE VALORES COMBINADOS

SI QUEREMOS CONOCER LA CANTIDAD DE ELEMENTOS DE UNA LISTA UTILIZAREMOS LA FUNCION  LEN:
LISTA= [4,9,10,8,7,4,8,3] #LISTA DE ELEMENTOS
PRINT (LEN(LISTA)) #VISUALIZA 5

MUTACION DE LISTAS.
partiendo de la lista: lista [2,3,'carlos']
para cambiar un componente de la lista, seleccionamos el componente mediante su indice y se le asigna un nuevo valor:
lista[3]='cambio'
para agregar un nuevo valor al final de la lista se utiliza el operador appedn():
lista. append(23)
para instertar un elemento en una posicion determinada de la lista y desplazar un lugar el elemento que este en esa posicion con insert:
lista.insert (2,76) #insertamos en la posicion 2
para eliminar un valor de la lista utilizar el operador remove ():
lista.remove(2)
Para buscar un valor de la lista utilizaremos el operador in:
23 in lista
Para saber la posicion de un valor en una lista usaremos index():
lista.index(3)'''
#ejemplo

lista=[]
for k in range(10):
    lista.append (input('introduce valor en lista:')) #añadimos los valores de la lista por teclado

print('los elementos de la lista son:'+str(lista)) #visualizamos los elementos de la lista
valor= int (input('introduce el valor a modificar de la lista con el indice:'))#indice a modificar
nuevo=input('introduce el nuevo valor:')#valor nuevo del indice que se modifica
lista [valor]=nuevo#hacemos la modificacion
print ('los elementos de la lista son:'+str(lista)) #visualizamos los elementos para comprobar la modificacion
valor=int (input('introduce el indice en el que se insertara nuevo valor:'))
nuevo=input('introduce el nuevo valor:') #valor a insertar
lista.insert (valor, nuevo)
print ('los elementos de la lista son:'+str (lista)) #visualizamos los elementos para comprobar la modificacion
nuevo=input ('introduce el valor a eliminar:') #valor a eliminiar
lista.remove(nuevo) #eliminamos el valor
print ('LOS ELEMENTOS DE LA LISTA SON:'+str (lista))#visualizamos la lista
nuevo=input ('introduce el valor a buscar:')
resultado=(nuevo in lista)
if(resultado):
       print ('existe este elemento y su indice es:'+str(lista.index(nuevo)))
else:print('no existe ese elemento')
                        
                        
                        
