#main.py
"""
Requirements : We are a clothing store currently running sales. Our clothes have sizes (S, M, L) , 
price and color(Red, Yellow, Green). The discount is 10% of the base price. Prices are $29.99, $39.99, $49.99 respectively And its based on promo codes of 
Xasd1q2341, Casqwe12&, as&*&*HAG. If a user enters a promo code that doesn't match. 
Let the user know via error message. Also ensure to keep track of every successfull transaction by logging the size, color, price in a file call
to transaction.txt

"""

import logging


DISCOUNT = 10/100 # 10% discount

PROMO_CODES = ["Xasd1q2341", "Casqwe12&", "as&*&*HAG"]


# Create a named logger
logger = logging.getLogger('Best Ecommerce')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('transaction.log')
file_handler.setLevel(logging.INFO)

# Set the formatter for the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')

file_handler.setFormatter(formatter)
# Add the file handler to the logger

logger.addHandler(file_handler)



class Cloth:
    STANDARD_PRICES = {"S":29.99, "M":39.99, "L":49.99 }
    def __init__(self, size:str,  color:str) -> None:
        self.validate_size(size)
        self.size = size
        self.color = color
    
    def validate_size(self,size:str):
        """ Ensure that the user enters a valid size of S, M or L"""
        if size not in self.STANDARD_PRICES.keys():
            raise Exception("Invalid Size, Please enter S, M , L")
    
    def __str__(self) -> str:
        """
        Converts the object to a string
        """
        return f"size : {self.size}, color:{self.color}"
    
    @property
    def price(self):
        return self.STANDARD_PRICES.get(self.size)

def calculate_total(price:float):
    return price - (DISCOUNT * price)
    

def validate_promo(promo:str):
    """
    Ensures that the user enters a valid promo code
    """
    if promo not in PROMO_CODES:
        raise Exception("Invalid Promo Code")
    
def record_transaction(cloth:Cloth , total:float):
    logger.info(f"Purchased {cloth} for a total of :${total}")

def purchase(cloth:Cloth, promo_code:str):
    validate_promo(promo_code)
    total = calculate_total(cloth.price)
    record_transaction(cloth, total)


def main():
    print("Welcome to best online store")
    size = input("Enter the size of your cloth: ")
    color = input("Enter the color of your cloth: ")
    promo_code = input("Enter the your promo code: ")
    try :
        cloth = Cloth(size,color)
        purchase(cloth, promo_code)
        print("Purchase successful ")
    except Exception as e:
        print(e)
        

# Run the script when we call python stage1.py
if __name__ == "__main__":
    main()
