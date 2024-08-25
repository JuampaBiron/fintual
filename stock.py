from datetime import datetime

class Stock:
    def __init__(self, symbol:str):
        self.symbol = symbol
        self.prices = {}
    
    def add_price(self, fecha, amount):
        if isinstance(amount, (int,float)):
            if isinstance(fecha, datetime):
                self.prices[fecha] = amount
            else:
                raise ValueError("El formato de la fecha debe ser 'datetime(yyyy,mm,dd)'")
        else:
            raise ValueError("El precio debe ser un número")
    
    def price_on_date(self, fecha: datetime):
        if isinstance(fecha, datetime):
            if fecha in self.prices:
                price = self.prices[fecha]
                return price
            else:
                print("El stock no tiene precios para esa fecha")
                return None
        else:
            raise ValueError("El formato de la fecha debe ser 'datetime(yyyy,mm,dd)'")
    
if __name__ == "__main__":
    stock = Stock("JPB")
    for i in range(1,12):
        stock.add_price(datetime(2024,i,1),11)
    print(stock.prices)
    print(stock.price_on_date(datetime(2024,2,1)))