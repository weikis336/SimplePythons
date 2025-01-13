def readfile():
  try:
    with open("file.txt", "r",  encoding="utf-8") as f:  
      file = f.read()
      print(file) 
  except FileNotFoundError:
      print("Error: El archivo 'file.txt' no se encontró.")
  except IOError:
      print("Error: Ocurrió un error al leer el archivo.")
  except Exception as e:
      print(f"Error inesperado: {e}")