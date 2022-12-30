def presentacion ():
	print('programa para hacer operaciones aritmeticas de suma y resta de dos valores')
	print ('********************')

def introducirdatos():
	global valor1
	global valor2 
	valor1= int(input('ingrese el primer valor'))
	valor2=int(input('ingrese el segundo valor'))

def suma():
	suma=valor1=valor2
	print('la suma de los dos valores es:', suma)

def resta():
	resta=valor1-valor2
	print('la resta de los valores es:',resta)

def finalizacion ():
	print('******************')
	print ('gracias por utilizar este programa')

presentacion()
introducirdatos()
suma()
resta ()
finalizacion()
