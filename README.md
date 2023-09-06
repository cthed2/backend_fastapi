# backend_fastapi

## Notas

### Video 12 
- Tipos de parámetros de una ruta:
 - Ruta: /
 - Consulta: ?, &

### Video 15:

Las class de BaseModel: 
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

Pueden ir en otra carpeta, por ejemplo en una que se llama models

- Además tenemos que crear un archivo __init__.py, para models (item_models) se identifique como MODULO. Y en ese archivo se pueden hacer operaciones rutinarias importaciones y operaciones que van orientadas al modulo.