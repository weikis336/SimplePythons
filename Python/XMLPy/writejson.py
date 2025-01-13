import json
def write_to_json(file_path, content):
    """
    Escribe el contenido en un archivo json.
        file_path (str): La ruta del archivo json.
        content (dict): El contenido del archivo.

    Returns:
        None
    """
    try:
        with open(file_path, 'w') as json_file:
            json.dump(content, json_file, indent=4)
        print(f"Content written to {file_path} successfully.")
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")