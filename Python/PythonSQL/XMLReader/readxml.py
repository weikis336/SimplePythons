import xml.etree.ElementTree as ET
from pathlib import Path

def importxml():# Print the root element
    script_dir = Path(__file__).parent.resolve()
    tree = ET.parse(script_dir / 'sensors.xml')  # Replace with the path to your XML file
    root = tree.getroot()
    print(f"Root element: {root.tag}")
    print("\n sensores:")
    sensors = []
    for val in root.findall('sensor'):  
        calle = val.find('calle').text  
        valor = float(val.find('valor').text)
        sensor = {
            'calle': calle,
            'valor': valor
        }
        sensors.append(sensor)
    return sensors

