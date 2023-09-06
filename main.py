# Importa el tipo Union desde el módulo typing. 
# Esto se utiliza para especificar que un tipo de variable puede ser uno de varios tipos.
from typing import Union
from models.item_models import Item

# Importa la clase FastAPI desde el módulo fastapi. 
# Esta clase se utiliza para crear una instancia de una aplicación FastAPI.
from fastapi import FastAPI

# Crea una instancia de la aplicación FastAPI.
# Esta instancia será el punto central para definir rutas y configuraciones.
app = FastAPI()
    
@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    """
    Actualiza un ítem basado en su ID y la información proporcionada.

    Parámetros:
    - item_id: El ID del ítem a actualizar, que se espera sea un entero (int).
    - item: Una instancia del modelo `Item` que contiene la información del ítem a actualizar.

    Retorna:
    Un diccionario con la clave 'item_name' conteniendo el nombre del ítem y la clave 'item_id' con el ID del ítem.

    Ejemplo:
    Si envías una solicitud PUT a `/items/5` con el cuerpo de la solicitud conteniendo 
    {"name": "NuevoNombre", "price": 10.5}, 
    obtendrás una respuesta que se verá más o menos así: `{"item_name": "NuevoNombre", "item_id": 5}`.
    """
    return {'item_name': item.name, 'item_id': item_id}

    

# Define una ruta para la URL raíz ("/") de la aplicación.
# Cuando se accede a esta URL, se ejecutará la función read_root.
@app.get('/')
def read_root():
    # Devuelve un diccionario como respuesta JSON.
    return {'Hello12': 'World'}

# Define una ruta que acepta un parámetro dinámico (item_id) en la URL.
# Por ejemplo, "/items/5" hará que item_id sea 5.
@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    # El parámetro item_id se espera que sea un entero (int).
    # El parámetro q es opcional y puede ser una cadena (str) o None.
    # Si q no se proporciona en la URL como un parámetro de consulta, su valor predeterminado será None.

    # Devuelve un diccionario con los valores de item_id y q como respuesta JSON.
    return {'item_id': item_id, 'q': q}

@app.get('/calculadora')
def calcular(operando_1: float, operando_2: float):
    """
    Función que suma dos operandos y devuelve el resultado en formato JSON.

    Parámetros:
    - operando_1: Primer operando de tipo flotante.
    - operando_2: Segundo operando de tipo flotante.

    Retorna:
    Un diccionario con la clave 'suma' y el valor siendo la suma de operando_1 y operando_2.

    Ejemplo:
    Si accedes a `/calculadora?operando_1=1.5&operando_2=2.5`, 
    obtendrás una respuesta que se verá más o menos así: `{"suma": 4.0}`.
    """
    return {'suma': operando_1 + operando_2}
