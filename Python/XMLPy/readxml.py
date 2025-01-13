import xml.etree.ElementTree as ET
import os
def parse_json(element):
    """"
    En esta funcion se define un diccionario que recibira el archivo xml que se lee 
    dentro del bucle de la funcion readfile
    Este fucnion puede ser reciclada y llamada para otros usos si fuera necesario.

    Explicacion de como usa un diccionario en python
        tag esta es la lectura de la etiqueta del archivo xml. 
        Nos interesa guardarlo para posteriormente tener una estructura solida e identificable de que leemos.

        attrib Si el xml tuviera, no es el caso pero puede tenerlos. Atributos tendriamos que guardarnos los valores.add

        children si el xml tuviera elementos anidados necesitamos ir recorriendo recursivamente recogiendo informacion de los hijos.

    """
    element_dict = {
        'tag': element.tag,
        'attrib': element.attrib,
        'children': [parse_json(subchild) for subchild in element]
    }
    if element.text and element.text.strip():
        element_dict['text'] = element.text.strip()
    return element_dict

def readfile(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: El archivo '{file_path}' no se encontró.")
        return {}
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        jsonformat = {}

        for child in root:
            if child.tag in jsonformat:
                if not isinstance(jsonformat[child.tag], list):
                    jsonformat[child.tag] = [jsonformat[child.tag]]
                jsonformat[child.tag].append(parse_json(child))
            else:
                jsonformat[child.tag] = parse_json(child)

        return jsonformat 
    except ET.ParseError:
        print("Error: El archivo 'commands.xml' no es valido.")
        return {}
    except Exception as e:
        print(f"Error inesperado: {e}")
        return {}
