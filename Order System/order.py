import logging

logging.basicConfig(
    filename="system.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class OutOfStockError(Exception):
    pass


def load_stock(filename):
    stock = {}
    try:
        logging.debug("Loading stock file")

        with open(filename, "r") as file:
            for line in file:
                if ":" not in line:
                    raise ValueError("Invalid stock file format")

                item, qty = line.strip().split(":")
                stock[item] = int(qty)

        return stock

    except FileNotFoundError:
        logging.critical("Stock file missing!")
        raise

    except ValueError as e:
        logging.error(f"Stock file error: {e}")
        raise


def update_stock(filename, stock):
    with open(filename, "w") as file:
        for item, qty in stock.items():
            file.write(f"{item}:{qty}\n")

    logging.debug("Stock updated in file")


def process_order(product, quantity):
    try:
        stock = load_stock("stock.txt")
        logging.info(f"User placed order: {product}, Quantity: {quantity}")

        if product not in stock:
            logging.warning("Product does not exist")
            return False

        if quantity < 1:
            logging.error("Invalid quantity entered")
            return False

        if quantity > stock[product]:
            raise OutOfStockError("Insufficient stock")

        if stock[product] - quantity <= 5:
            logging.warning(f"Low stock warning for {product}")

        stock[product] -= quantity
        logging.info("Order processed successfully")

        update_stock("stock.txt", stock)
        logging.debug(f"{product} stock reduced to {stock[product]}")

        return True

    except OutOfStockError as e:
        logging.error(str(e))
        return False

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return False

    finally:
        logging.debug("Order processing completed")

if __name__ == "__main__":
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    success = process_order(product, quantity)

    if success:
        print("Order placed successfully!")
        print("Updated stock saved.")

    print("Operation completed. Check system.log for details.")
