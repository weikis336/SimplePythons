import readxml as readfile
def search_text_in_file(file_path, search_text):
    """Busca un texto dentro del fichero json creado a partir del xml"""
    content = readfile.readfile(file_path) 
    found = False
    def search_dict(d):
        nonlocal found #Creamos la variable found dentro de la funcion pero en modo global. 
        if isinstance(d, dict):
            for key, value in d.items():
                if search_text in str(key) or (isinstance(value, str) and search_text in value):
                    print(f"Encontrado '{search_text}' en el elemento: {key}, valor: {value}")
                    found = True
                elif isinstance(value, (dict, list)):
                    search_dict(value)
        elif isinstance(d, list):
            for item in d:
                search_dict(item)
    search_dict(content)
    if not found:
        print(f"'{search_text}' No encontrado en el archivo.")