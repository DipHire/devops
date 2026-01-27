import logging
import os

# =======================
# Logging Configuration
# =======================
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# =======================
# Functions
# =======================
def add(a, b):
    logging.debug(f"add() called with {a}, {b}")
    return a + b

def divide(a, b):
    logging.info(f"divide() called with {a}, {b}")
    try:
        result = a / b
        logging.info(f"Division result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero error")
        return None

def read_file(filename):
    logging.info(f"Trying to read file: {filename}")
    if not os.path.exists(filename):
        logging.warning("File not found")
        return

    with open(filename, "r") as f:
        logging.info("File opened successfully")
        data = f.read()
        logging.debug("File read completely")
        print(data)

# =======================
# Main Program
# =======================
logging.info("Application started")

x = add(10, 20)
logging.info(f"Addition result: {x}")

y = divide(10, 0)

read_file("data.txt")

logging.critical("Application finished")
