import random



puntosMaquina=0
puntosJugador=0
partidas=0

while partidas<=5:
    jugador=int(input("\nSeleccione : 1. Piedra, 2. Papel  3. Tijera: "))

    maquina = random.randint(1,3)

    if jugador==maquina :
        print("¡Empate! Vuelva a intentarlo. Esta jugada no será contada.")
    elif jugador==1 and maquina==2: 
        print("Vaya vaya. Has perdido contra una maquina las IA nos dominaran. \n Papel le gana a piedra.")
        puntosMaquina=puntosMaquina+1
        partidas=partidas+1
    elif jugador==2 and maquina==3:
        print("Madra mia. Has perdido contra una tostadora. \n Tijera le gana a papel.")
        puntosMaquina=puntosMaquina+1
        partidas=partidas+1
    elif jugador==3 and maquina==1:
        print("No puede ser has perdido.El T-800 te esta buscando. Huye \n Piedra le gana a tijera.")
        puntosMaquina=puntosMaquina+1
        partidas=partidas+1
    elif jugador==2 and maquina==1:
        print("Estaras orgulloso le acabas de ganar a una placa base.\n Papel le gana a piedra.")
        puntosJugador=puntosJugador+1
        partidas=partidas+1
    elif jugador==3 and maquina==2:
        print("Bravo has sido capaz de vencer a una secuencia de unos y ceros.\n Tijera le gana a papel.")
        puntosJugador=puntosJugador+1
        partidas=partidas+1
    elif jugador==1 and maquina==3:
        print("Muy bien has detenido la invasion liderada por Skynet.\n Piedra le gana a tijera.")
        puntosJugador=puntosJugador+1
        partidas=partidas+1

print("\nTu total de puntos es: "+str(puntosJugador)+". Y el total de puntos de la máquina es: "+str(puntosMaquina))
if puntosJugador>puntosMaquina:
    print ("Bravo has demostrado ser la persona mas suertuda existente habiendole ganado a priedra papel o tijeras a una maquina..")
elif puntosJugador == puntosMaquina:
    print("Has empatado con una maquina no se si es un logro o un fracaso.")
else:  
    print ("Has perdido.No estes triste es normal que tus pocas neuronas no sean capaces de ganar a un ordenador.")
