"""Estructura repetitiva WHILE. una estructura repetitiva permite ejecutar
una instruccion o conjunto de instrucciones varias veces"
No se debe confundir la estructura del WHILE con la estructura del IF
Funcionamiento: en primer lugar se verifica la condicion, si la misma resulta verdadera
se ejecutan las operaciones que indicamos por la rama del verdadero.
A la rama del verdadero la graficamos en la parte inferior de la condicion. Una linea al final
del bloque de repeticion la conecta con la parte superior de la estructura repetitiva.
En caso que la condicion sea falsa continua por la rama del falso y sale de la estructura
repetitiva para continuar con la ejecucion del algoritmo

el bloque se repite mientras la condicion sea verdadera.

IMPORTANTE: Si la condicion siempre retorna verdadero estamos en presencia de
un ciclo repetitivo infinito. Dicha situacion es un error de programacion logico,
nunca finalizara el programa.
EVALUA UNA DETERMINADA CONDICION, SI LA MISMA ES VERDADERA SE EJECUTA HASTA QUE LA CONDICION DEJE
DE APLICARSE, Y CONTINUA CON LA EJECUCUION DEL RESTO DEL PROGRAMA"""


#ejemplo estructura repetitiva While

x=1
suma=0
while x<=10:
    valor=int(input('ingrese un valor'))
    suma=suma+valor
    x=x+1
promedio=suma/10
print ('la suma de los 10 valores es')
print (suma)
print ( 'el promedio es')
print (promedio)
       
#2 ejemplo bucle while

i=0
while i<=10:
    print ('hola mundo')
    i+=1
    
