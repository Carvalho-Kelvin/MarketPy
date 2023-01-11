from typing import List, Dict
from time import sleep
from models.product import Product
from utils.helper import format_float_str_currency

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('****************************')
    print("Welcome to the Kelvin's Shop")
    print('****************************')

    print('Choose an option:')
    print('1 - Register Product')
    print('2 - List products')
    print('3 - Buy product')
    print('4 - View cart')
    print('5 - Finish order')
    print('6 - Close the system')

    try:
        option: int = int(input())
        if option == 1:
            register_product()
        elif option == 2:
            list_products()
        elif option == 3:
            buy_product()
        elif option == 4:
            view_cart()
        elif option == 5:
            finish_order()
        elif option == 6:
            print('You finished our system. See you soon!')
            sleep(2)
            exit()
        else:
            print('Choose a valid option!')
            sleep(2)
            menu()
    except ValueError:
        print('Choose a valid option!')
        sleep(2)
        menu()


def register_product() -> None:
    print('Registration of products')
    print('************************')

    name = input('Digit the product name: ')
    price = float(input('Digit the product price: '))

    if len(products) > 0:
        for product in products:
            if name == product.name:
                print('This product was already registered!')
                sleep(2)
                menu()
        prod = Product(name, price)
        products.append(prod)
        print(f'The product {name} was registered with success!')
        sleep(2)
        menu()
    else:
        prod = Product(name, price)
        products.append(prod)
        print(f'The product {name} was registered with success!')
        sleep(2)
        menu()


def list_products() -> None:
    if len(products) > 0:
        print('List of products:')
        for product in products:
            print(product)
            print('-------------------------')
            sleep(2)
    else:
        print("There's no product registered.")
    sleep(2)
    menu()


def buy_product() -> None:
    if len(products) > 0:
        print('Products available: ')
        for product in products:
            print(product)
            print('-------------------------')
            sleep(2)
        code: int = int(input('Digit the code of the product that you want to buy: '))

        product: Product = get_product_for_code(code)

        if product:
            if len(cart) > 0:
                there_is_in_the_cart: bool = False
                for item in cart:
                    quantity: int = item.get(product)
                    if quantity:
                        quantity += 1
                        print(f'{product.name} now have {quantity} units in your cart.')
                        there_is_in_the_cart = True
                        sleep(2)
                        menu()
                if not there_is_in_the_cart:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'The product {product.name} was added to your cart.')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'The product {product.name} was added to your cart.')
                sleep(2)
                menu()
        else:
            print(f'The product with code {code} was not found.')
            sleep(2)
            menu()
    else:
        print("There's no product registered.")
    sleep(2)
    menu()


def view_cart() -> None:
    if len(cart) > 0:
        print('Your cart:')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Unities: {data[1]}')
                print('-------------------------')
                sleep(2)
    else:
        print('Your cart is empty.')
    sleep(2)
    menu()


def finish_order() -> None:
    if len(cart) > 0:
        total_value: float = 0

        print('Products in your cart:')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                total_value += data[0].price * data[1]
                sleep(1)
        print(f'Your bill is {format_float_str_currency(total_value)}')
        cart.clear()
        sleep(4)
    else:
        print('Your cart is empty. Please, add an item to continue shopping.')
    sleep(1)
    menu()


def get_product_for_code(code: int) -> Product:
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p


if __name__ == '__main__':
    main()
