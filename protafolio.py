from datetime import datetime
from stock import Stock
from dateutil import relativedelta

class Portafolio:
    def __init__(self):
        self.stock = {}
    
    def add_stock(self, stock: Stock):
        self.stock[stock.symbol] = stock.prices

    def buscar_fechas_ajustadas(fechas_ordenadas, fecha_inicial, fecha_final):
        """
        Función auxiliar para encontrar la fecha inicial y final más cercana dentro de un rango de fechas.
        """
        fecha_inicial_ajustada = None
        fecha_final_ajustada = None
        
        for fecha in fechas_ordenadas:
            if fecha >= fecha_inicial and fecha_inicial_ajustada is None:
                fecha_inicial_ajustada = fecha
            if fecha <= fecha_final:
                fecha_final_ajustada = fecha
                
        return fecha_inicial_ajustada, fecha_final_ajustada

    
    def profit(self, fecha_inicial, fecha_final):
        total_inicial = 0
        total_final = 0
        if fecha_inicial >= fecha_final:
            raise ValueError("La fecha inicial debe ser menor que la fecha final.")
        for stock in self.stock.values():
            # Ordenar las fechas disponibles para el stock
            fechas_ordenadas = sorted(stock.keys())

            # Buscar las fechas inicial y final ajustadas usando la función auxiliar
            fecha_inicial_ajustada, fecha_final_ajustada = Portafolio.buscar_fechas_ajustadas(fechas_ordenadas, fecha_inicial, fecha_final)

            # Calcular los valores iniciales y finales ajustados
            try:
                start_value = stock[fecha_inicial_ajustada]
                final_value = stock[fecha_final_ajustada]
                total_inicial += start_value
                total_final += final_value
            except KeyError:
                pass

        return total_final - total_inicial
    
    def annualized_return(self, fecha_inicial, fecha_final):
        total_inicial = 0
        total_final = 0
        if fecha_inicial >= fecha_final:
            raise ValueError("La fecha inicial debe ser menor que la fecha final.")

        for stock in self.stock.values():
            fechas_ordenadas = sorted(stock.keys())

            # Buscar las fechas inicial y final ajustadas usando la función auxiliar
            fecha_inicial_ajustada, fecha_final_ajustada = Portafolio.buscar_fechas_ajustadas(fechas_ordenadas, fecha_inicial, fecha_final)

            try:
                start_value = stock[fecha_inicial_ajustada]
                final_value = stock[fecha_final_ajustada]
                total_inicial += start_value
                total_final += final_value
            except KeyError:
                pass

        # Calcular rendimiento total
        if total_inicial == 0:
            return None  # Evita la división por cero
        total_return = total_final / total_inicial

        # Calcular número de años entre las dos fechas
        diferencia = relativedelta.relativedelta(fecha_final, fecha_inicial)
        numero_anos = diferencia.years + diferencia.months / 12 + diferencia.days / 365

        # Calcular rendimiento anualizado
        annualized_return = (total_return ** (1 / numero_anos)) - 1
        annualized_return = round(annualized_return,2)

        return annualized_return



if __name__ == "__main__":
    stock_jp = Stock("JPB")
    stock_jp.add_price(fecha = datetime(2023,2,1),amount=100)
    stock_jp.add_price(fecha = datetime(2023,3,1),amount=500)
    stock_da = Stock("DSA")
    stock_da.add_price(fecha = datetime(2024,2,1),amount=100)
    stock_da.add_price(fecha = datetime(2024,4,1),amount=9342)
    portafolio = Portafolio()
    portafolio.add_stock(stock_jp)
    portafolio.add_stock(stock_da)
    #print(portafolio.stock)

    print(portafolio.profit(fecha_inicial=datetime(2024,1,1), fecha_final=datetime(2025,3,1)))
    print(portafolio.annualized_return(fecha_inicial=datetime(2024,1,1), fecha_final=datetime(2025,3,1)))
        