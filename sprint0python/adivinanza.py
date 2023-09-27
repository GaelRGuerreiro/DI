
print('Existe un ser vivo capaz de beber agua con los pies. ¿Cuál es?')
print('')
print('a) Un Arbol')
print('b) Un Elefante')
print('c) Una hormiga' )
print('')

respuesta = 'a'
turespuesta = input('Tu respuesta: ').lower()
if turespuesta != respuesta:
    print('''Respuesta incorrecta.
          La respuesta correcta era:
           a) Un Arbol''')
    
else:
    print('Respuesta correcta')
  