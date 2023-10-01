from operaciones import suma, resta, multiplicacion, division

repetir = "s"

while repetir == 's': 
  num1=int(input("Introduzca primer numero: "))
  num2=int(input("Introduzca segundo numero: "))
  decision = input("\nQue operacion desea realizar: ")

  if  decision== 'suma':
        operacion=suma(num1, num2)
        print("\nEl resultado de su operación es: "+str(operacion))
  elif decision == 'resta':
        operacion=resta(num1, num2)
        print("\nEl resultado de su operación es: "+str(operacion))
  elif decision == 'multiplicacion':
        operacion=multiplicacion(num1, num2)
        print("\nEl resultado de su operación es: "+str(operacion))
  elif decision == 'division':
        operacion=division(num1, num2)
        if  num2==0:
            repetir = input("\n¿Desea realizar mas operaciones? (s/n): ")
        print("\nEl resultado de su operación es: "+str(operacion))
repetir = input("\n¿Desea realizar mas operaciones? (s/n): ")