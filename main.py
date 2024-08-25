import logging
from stock import Stock
from protafolio import Portafolio
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Inicio del programa")

        # Crear stocks
        stock1 = Stock("AAPL")
        stock1.add_price(datetime(2021, 1, 1), 150)
        stock1.add_price(datetime(2024, 1, 1), 200)
        logging.info(f"Stock {stock1.symbol} creado con precios {stock1.prices}")

        stock2 = Stock("GOOGL")
        stock2.add_price(datetime(2022, 1, 1), 1800)
        stock2.add_price(datetime(2024, 1, 1), 2200)
        logging.info(f"Stock {stock2.symbol} creado con precios {stock2.prices}")

        stock3 = Stock("JPB")
        stock3.add_price(datetime(2023, 1, 1), 100)
        stock3.add_price(datetime(2024, 1, 1), 2300)
        logging.info(f"Stock {stock3.symbol} creado con precios {stock3.prices}")

        # Crear un portafolio y agregar las acciones
        portfolio = Portafolio()
        portfolio.add_stock(stock1)
        portfolio.add_stock(stock2)
        portfolio.add_stock(stock3)
        logging.info(f"Portafolio creado con {len(portfolio.stock)} stocks")

        # Definir las fechas de inicio y fin para el cálculo
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2024, 1, 1)

        # Calcular el beneficio y el retorno anualizado
        try:
            profit = portfolio.profit(start_date, end_date)
            annualized_return = portfolio.annualized_return(start_date, end_date)
            logging.info(f"Profit calculado: {profit:.2f}")
            logging.info(f"Annualized Return calculado: {annualized_return:.2%}")
        except ValueError as e:
            logging.error(f"Error calculando el beneficio o el retorno anualizado: {e}")
            return
        except KeyError as e:
            logging.error(f"Error de clave en los datos de precios: {e}")
            return

        logging.info(f"Profit between {start_date.date()} and {end_date.date()}: {profit:.2f}")
        logging.info(f"Annualized Return between {start_date.date()} and {end_date.date()}: {annualized_return:.2%}")

    except Exception as e:
        logging.error(f"Un error inesperado ocurrió: {e}")

if __name__ == "__main__":
    main()
