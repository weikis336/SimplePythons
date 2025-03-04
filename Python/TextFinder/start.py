import readfiletext as readfile

def find_file_content(file_path, find_txt):
    content = readfile.readfile(file_path)
    return readfile.search_text(content, find_txt)
    
def main_menu():
    print("Elige una opcion:")
    print("1. Busca el texto en el archivo y muestra la linea donde se encuentra")
    print("2. Salir")
find_txt = ""
condicion = True
while condicion:
  main_menu()
  user_input = input("Enter the option number: ")

  if user_input.isdigit() and int(user_input) in [1, 2, 3]:
    user_input = int(user_input)
    if user_input == 1:
        find_txt = input("Introduce el texto que quieres buscar dentro del archivo txt: ")
        print(find_file_content('sample.txt', find_txt))

    elif user_input == 2:
        print("Saliendo...")
        break 
  else:
    print("Opcion no valida. Prueba otra vez")
