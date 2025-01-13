import readfile
def mymenu():
  opciones = [1,2,3]
  print("Que opción de las siguientes opciones quieres ejecutar")
  print("|1| Mostrar el contenido del archivo")
  print("|2| Busca dentro del archvio un texto")
  print("|3| Salir de la terminal")
  userinput = input("Presione una tecla de las anteriores opciones para continuar, " + str(opciones) + ": ")
  if userinput.isdigit() and int(userinput) in opciones:
    return int(userinput)
  else:
    print("Opción no válida. Intente de nuevo.")
    return None  
condicion = True
while condicion:
  userinput = mymenu()

  if userinput == 1:
    readfile.readfile()
  elif userinput == 2:
      print("Buscar dentro del archivo un texto.")
  elif userinput == 3:
      print("Saliendo de la terminal.")
      condicion = False
