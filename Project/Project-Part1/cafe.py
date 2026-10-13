Cafe_name = "Python Cafe"
tax_rate = 0.08


menu = {
  "expresso": 3.00,
  "latte": 4.50,
  "cappuccino": 4.25,
  "mocha": 5.00,
  "muffin": 2.50,
  "croissant": 3.25
}

order = []

def greet(name):
  print(f"Welcome to {cafe_name}, {name}!")



def show_menu(menu):
  print("---MENU---")
  for item, price in menu.items():
    print(f"{item}: ${price:.2f}")


def show_order(order, menu):
  if len(order) == 0:
    print("Nothing is ordered.")
  else:
    print("--- Your order is ---)
          for item in order:
    print(f"{item}: ${menu[item]:.2f}")
    print(f"Items: {len(order)}")


def calculate_subtotal(order, menu):
  subtotal = o
  for item in order:
    subtotal = subtotal + menu[item]
    return subtotal


def get_discount(subtotal, is_member):
  if is_member and subtotal >= 20:
    return subtotal * 0.15
  else:
    if subtotal >= 10:
      return subtotal * 0.10
    else:
      return 0
else:
if subtotal >= 25:
  return subtotal * 0.5
else:
  return 0
