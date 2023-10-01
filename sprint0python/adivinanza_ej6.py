
import random

puntos = 0
veces = 0

adivinanzas = {
    1: 'Existe un ser vivo capaz de beber agua con los pies. ¿Cuál es?\na. Un arbol, b. Un elefante, c. Una hormiga: ',
    2: "Qué cosa es que cuanto más le quitas más grande es?\na.Un agujero , b.La ambicion , c. Queso gruyer ",
    3: "Es blanco como la espuma. Facil de abrir pero imposible de cerrar\na. Un huevo, b. Un motor diesel blanco, c. Un gato : ",
}

Adivinanzas = list(adivinanzas.keys())

while veces < 3:
    sel = random.sample(Adivinanzas, 1)[0]
    Adivinanzas.remove(sel) 

    print(adivinanzas[sel])
    sol = input("\t")
    veces += 1

    if sel == 1:
        if sol == 'a':
            print("\n¡Enhorabuena! Has acertado.\n")
            puntos += 10
        else:
            print("\nError. Esa es la respuesta incorrecta.\n")
            puntos -= 5
    elif sel == 2:
        if sol == 'a':
            print("\n¡Enhorabuena! Has acertado.\n")
            puntos += 10
        else:
            print("\nError. Esa es la respuesta incorrecta.\n")
            puntos -= 5
    elif sel == 3:
        if sol == 'a':
            print("\n¡Enhorabuena! Has acertado.\n")
            puntos += 10
        else:
            print("\nError. Esa es la respuesta incorrecta.\n")
            puntos -= 5

print("Ha finalizado el juego. Tienes un total de: " + str(puntos) + "\n")