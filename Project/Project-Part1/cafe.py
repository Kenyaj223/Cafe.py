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
  print(f"Welcom to {cafe_name}, {name}!")



def show_menu(menu):
  print("---MENU---")
  for item, price in menu.items():
    print(f"{item}: ${price:.2f}")

