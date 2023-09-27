
print('Existe un ser vivo capaz de beber agua con los pies. ¿Cuál es?')
print('')
print('a) Un Arbol')
print('b) Un Elefante')
print('c) Una hormiga' )
print('')
contador=0
respuesta = 'a'
turespuesta = input('Tu respuesta: ').lower()
if turespuesta != respuesta:
    print('''Respuesta incorrecta.
          La respuesta correcta era:
           a) Un Arbol''')
    print("+ 5 ")
    contador=contador+5
    
else:
    print('Respuesta correcta')
    print("+ 10")
    contador=contador+10
 
print('')
print('¿Qué cosa es que cuanto más le quitas más grande es?')
print('')
print('a) La ambicion')
print('b) Un agujero')
print('c) Un trozo de queso' )
print('')
respuesta = 'b'
turespuesta = input('Tu respuesta: ').lower()
if turespuesta != respuesta:
    print('''Respuesta incorrecta.
          La respuesta correcta era:
           b) Un Agujero''')
    print("+ 5")
    contador=contador+5
    
else:
    print('Respuesta correcta')
    print("+ 10")
    contador=contador+10
  

print('')


print('Es blanco como la espuma. Facil de abrir pero imposible de cerrar')
print('')
print('a) Un huevo')
print('b) Una puerta blanca')
print('c) Un gato' )
print('')
respuesta = 'a'
turespuesta = input('Tu respuesta: ').lower()
if turespuesta != respuesta:
    print('''Respuesta incorrecta.
          La respuesta correcta era:
           a) Un huevo ''')
    print("+ 5")
    contador=contador+5
    
else:
    print('Respuesta correcta')
    print("+ 10")
    contador=contador+10

print('')


print('Tu puntuacion es : ')
print(contador)