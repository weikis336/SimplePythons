import XMLReader.readxml as readxml
import SQLInstance.SQLConnector.WorkSQL as WorkSQL

def main_menu():
    print("Elige una opcion:")
    print("1. Test conection on DB")
    print("2. Send to a db a query")
    print("3. Commit the data on a xml file to a db")
    print("4. Salir")

condicion = True
while condicion:
  main_menu()
  user_input = input("Enter the option number: ")

  if user_input.isdigit() and int(user_input) in [1, 2, 3, 4]:
    user_input = int(user_input)
    if user_input == 1:
        test="SELECT nombre, precio, precio * 1.11 AS precio_dolares FROM producto;"
        WorkSQL.conection(test)

    elif user_input == 2:
        send_query = input("Introduce el elemento a buscar: ")
        WorkSQL.conection(send_query)
    
    elif user_input == 3:
        sensors = readxml.importxml()
        WorkSQL.insert(sensors)

    elif user_input == 4:
        print("Saliendo...")
        break 
  else:
    print("Opcion no valida. Prueba otra vez")
