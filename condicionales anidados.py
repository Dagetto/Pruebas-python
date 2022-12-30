#Estructuras condicionales anidades se genera cunado por la rama del verdadero o falso de una estructura condicional hay otra estructura condicional.
""" La estructura IF permite encadenar varias condicionales ELIF() dentro de dicha estructura.
Estas sirven para evaluar mas detalladamente el proceso de ejecucion de un progama
Ej: if expression 1
 Statement (s)
 elif expression2
 statement(s)
 elif expression3
 statement(s)
 else: statement(s)"""
#Ejemplo 1
nota1=int(input('ingrese su primer nota:'))
nota2=int(input('ingrese su segunda nota:'))
nota3= int(input('ingrese se tercer nota:'))
prom=(nota1+nota2+nota3)/3
if prom >=7: print ('promocionado')
else:
    if prom>=4: print ('regular')
    else: print ('reprobado')                    
