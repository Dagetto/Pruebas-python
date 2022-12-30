nota1=int(input('ingrese su primer nota'))
nota2=int(input('ingrese su segunda nota'))
nota3=int(input('ingrese su tercer nota'))

media=(nota1+nota2+nota3)/3

if media ==9 or media ==10: print ('sobresaliente')
elif media== 5: print('suficiente')
elif media== 6: print('bien')
elif media== 7 or media == 8: print ('regular/M.bien')
else: print ('insuficiente')
