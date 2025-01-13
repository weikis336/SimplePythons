import readxml as readfile
import searchfile as searchfile
import writejson as writejson
import json

def display_file_content(file_path):
    content = readfile.readfile(file_path)
    print(json.dumps(content, indent=4)) 

def search_text_in_file(file_path, search_text):
    searchfile.search_text_in_file(file_path, search_text )

def save_to_json(file_path):
    content = readfile.readfile(file_path)
    json_file_path = input("Introduce el nombre del archivo: ")
    writejson.write_to_json(json_file_path, content)

def main_menu():
    print("Elige una opcion:")
    print("1. Muestra el contenido del archivo")
    print("2. Busca texto en el archivo")
    print("3. Guardar en json")
    print("4. Salir")

condicion = True
while condicion:
  main_menu()
  user_input = input("Enter the option number: ")

  if user_input.isdigit() and int(user_input) in [1, 2, 3]:
    user_input = int(user_input)
    if user_input == 1:
        display_file_content('commands.xml')

    elif user_input == 2:
        search_text = input("Introduce el elemento a buscar: ")
        search_text_in_file('commands.xml', search_text)
    
    elif user_input == 3:
        save_to_json('commands.xml')

    elif user_input == 4:
        print("Saliendo...")
        break 
  else:
    print("Opcion no valida. Prueba otra vez")
