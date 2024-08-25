# Stock Portfolio Management

Este proyecto proporciona una implementación básica para gestionar un portafolio de acciones y calcular el rendimiento y el retorno anualizado basado en las fechas de precios disponibles para cada acción.

## Clases

### `Stock`

La clase `Stock` representa una acción con un símbolo y un diccionario de precios asociados a fechas.

#### Métodos

- **`__init__(symbol: str)`**
  - Inicializa un objeto `Stock` con el símbolo de la acción.
  
- **`add_price(fecha: datetime, amount: Union[int, float])`**
  - Añade un precio para una fecha específica. Acepta `amount` como `int` o `float`.
  - Lanza un `ValueError` si `fecha` no es un objeto `datetime` o `amount` no es un número.

- **`price_on_date(fecha: datetime)`**
  - Devuelve el precio de la acción en la fecha especificada. Retorna `None` si la fecha no está disponible.

### `Portafolio`

La clase `Portafolio` representa una colección de acciones y permite calcular el rendimiento total y el retorno anualizado del portafolio.

#### Métodos

- **`__init__()`**
  - Inicializa un objeto `Portafolio`.

- **`add_stock(stock: Stock)`**
  - Añade un objeto `Stock` al portafolio.

- **`profit(fecha_inicial: datetime, fecha_final: datetime) -> float`**
  - Calcula el rendimiento total del portafolio entre las fechas especificadas.
  - Lanza un `ValueError` si `fecha_inicial` no es menor que `fecha_final`.

- **`annualized_return(fecha_inicial: datetime, fecha_final: datetime) -> float`**
  - Calcula el rendimiento anualizado del portafolio entre las fechas especificadas.
  - Lanza un `ValueError` si `fecha_inicial` no es menor que `fecha_final`.

## Ejemplos de Uso

```python
from datetime import datetime
from stock import Stock
from portafolio import Portafolio

# Crear objetos Stock
stock_jp = Stock("JPB")
stock_jp.add_price(fecha=datetime(2023, 2, 1), amount=100)
stock_jp.add_price(fecha=datetime(2023, 3, 1), amount=500)

stock_da = Stock("DSA")
stock_da.add_price(fecha=datetime(2024, 2, 1), amount=100)
stock_da.add_price(fecha=datetime(2024, 4, 1), amount=9342)

# Crear y añadir stocks al portafolio
portafolio = Portafolio()
portafolio.add_stock(stock_jp)
portafolio.add_stock(stock_da)

# Calcular profit
profit = portafolio.profit(fecha_inicial=datetime(2023, 1, 1), fecha_final=datetime(2023, 3, 1))
print(f"Profit: {profit}")

# Calcular annualized return
annualized_return = portafolio.annualized_return(fecha_inicial=datetime(2023, 1, 1), fecha_final=datetime(2024, 3, 1))
print(f"Annualized Return: {annualized_return}")
