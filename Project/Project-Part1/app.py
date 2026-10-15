
import streamlit as st

cafe_name = "Python Cafe"
tax_rate = 0.08

menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25
}

st.title("☕ Python Cafe")
st.write("Welcome to Python Cafe!")

name = st.text_input("What is your name?")
is_member = st.checkbox("Are you a member?")

st.subheader("Our Menu")

for item in menu:
    st.write(item.title() + " - $" + format(menu[item], ".2f"))

st.subheader("Place Your Order")

item = st.selectbox("Choose an item", list(menu.keys()))
quantity = st.number_input("Quantity", min_value=1, max_value=20, value=1)

if st.button("Add to Order"):
    if "order" not in st.session_state:
        st.session_state.order = []

    for number in range(quantity):
        st.session_state.order.append(item)

if "order" not in st.session_state:
    st.session_state.order = []

st.subheader("Your Order")

if len(st.session_state.order) > 0:
    subtotal = 0

    for item in st.session_state.order:
        st.write(item.title() + " - $" + format(menu[item], ".2f"))
        subtotal = subtotal + menu[item]

    discount = 0

    if is_member and subtotal >= 20:
        discount = subtotal * 0.15
    elif subtotal >= 20:
        discount = subtotal * 0.05

    discounted_subtotal = subtotal - discount
    tax = discounted_subtotal * tax_rate
    total = discounted_subtotal + tax

    st.write("Subtotal: $" + format(subtotal, ".2f"))
    st.write("Discount: -$" + format(discount, ".2f"))
    st.write("Tax: $" + format(tax, ".2f"))
    st.write("Total: $" + format(total, ".2f"))

    if st.button("Remove Last Item"):
        st.session_state.order.pop()
        st.rerun()

    if st.button("Checkout"):
        st.success("Thank you for visiting, " + name + "!")
else:
    st.write("Your order is empty.")

