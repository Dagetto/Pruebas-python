#Para cargar por teclado una cadena de caracteres utilizamos la funcion INPUT
#Ejemplo de utilizacion de la funcion input.

print ('datos de la primera persona')
nombre1= input('ingrese nombre del producto:')
precio1=int(input (' ingrese el precio del producto:'))
nombre2= input ('ingrese nombre del producto:')
precio2=int(input ('ingrese el precio del producto:'))


#ejemplo de utilizacion de constantes

BONIFICACION=20

"""para comentarios mas largos de una linea utilizamos tres pares de comillas"""
# para comentarios de una linea utilizamos solamente un #

#suma de los dos precios y su resultado se guarda en una variable.

precio_compra_total= precio1 +precio2 #ejemplo de operador aritmetico

# comprobamos si el precio1 es mayor o igual al precio2
                   
comparar=precio1>=precio2 #ejemplo de operador de comparacion (Booler TRUE/FALSE)

logico=(precio1<precio2 and precio1== precio2) #ejemplo de operador logico (Booler TRUE/FALSE)

#ejemplo para concatenar cadenas de texto con la funcion FORMAT

cabecera='resultados del producto {0}. y del producto {1}.:'
print (cabecera.format (nombre1, nombre2))
print('el precIo del primer valor es mayor o igual a el precio del segundo valor:')
print (comparar)

 #ejemplo de concatenar con + y la variable de propiedad STR
print ('la suma de los productos es:' +str (precio_compra_total))
print('precio1<precio2 and precio1==precio2')
print (logico)

#ejemplo de operador de asignacion
precio_compra_total+=BONIFICACION
             

print ('al precio total le incrementamos su valor que tiene la constante:'+str (precio_compra_total))

        #FIN CLASE 1
       
       
