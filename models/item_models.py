# Importa el tipo Union desde el módulo typing. 
# Esto se utiliza para especificar que un tipo de variable puede ser uno de varios tipos.
from typing import Union
# Importa la clase BaseModel desde el módulo pydantic.
# BaseModel es una clase base para definir modelos de datos con validación de tipos,
# serialización y documentación integradas. Es ampliamente utilizado con FastAPI
# para definir modelos de solicitud y respuesta, asegurando que los datos cumplan
# con un formato específico.
from pydantic import BaseModel

# Define una clase `Item` que hereda de `BaseModel` de Pydantic.
# Esta clase representa un modelo de datos para un ítem, con validación de tipos,
# serialización y documentación integradas gracias a Pydantic.
class Item(BaseModel):
    # Define un atributo `name` que debe ser de tipo string (str).
    name: str
    
    # Define un atributo `price` que debe ser de tipo flotante (float).
    price: float
    
    # Define un atributo `is_offer` que puede ser de tipo booleano (bool) o None.
    # Si `is_offer` no se proporciona al crear una instancia de `Item`, su valor predeterminado será None.
    # Nota: Hay un error tipográfico en "Unio". Debería ser "Union".
    is_offer: Union[bool, None] = None