def readfile(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Error: El archivo no fue encontrado."
    except Exception as e:
        return f"Error: {str(e)}"
def search_text(content, search_term):
    occurrences = []
    lines = content.splitlines()
    for line_num, line in enumerate(lines, 1):
        start = 0
        while True:
            position = line.find(search_term, start)
            if position == -1:
                break
            occurrences.append({
                'linea': line_num,
                'posicion': position + 1,
                'texto': line.strip()
            })
            start = position + 1
    return occurrences