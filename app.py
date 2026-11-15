# CIS 211 Lab 5 - Bright Bakery Interactive Order Calculator
# Complete the TODO sections using the Lab 5 instructions.
# Add at least THREE explanatory comments of your own.

import streamlit as st

# Supplied data: keep these products, prices and sample counts unchanged.
menu = {
    "cupcake": 3.75,
    "cookie": 2.00,
    "muffin": 2.75,
    "scone": 3.25,
    "brownie": 3.00,
}

sample_sales = {
    "Product": ["cupcake", "cookie", "muffin", "scone", "brownie"],
    "Units sold": [18, 30, 12, 10, 15],
}


def apply_discount(subtotal):
    """Return the remaining item subtotal after any eligible discount."""
    # TODO 1: Follow Step 4. Replace pass with your calculation and return.
    if subtotal >= 50:
        return round (subtotal * 0.90, 2)
    return subtotal


def shipping_fee(subtotal):
    """Return the Delivery fee, using the ORIGINAL item subtotal."""
    # TODO 2: Follow Step 4. Replace pass with your decision and return.
    if subtotal >= 40:
        return 0.00
    return 5.00


st.title("Bright Bakery Interactive Order Calculator")
st.caption("A class practice app that calculates a quote.")


# TODO 3 - Step 5: Put the required controls in a sidebar.
# Collect customer_name, product, quantity, fulfillment and show_chart.
# Keep quantity an integer from 1 through 30.
with st.sidebar:
    customer_name = st.text_input("Customer Name")
    product = st.selectbox("Product", list(menu.keys()))
    quantity = st.number_input("Quantity", min_value=1, max_value=30, value=1, step=1)
    fulfillment = st.radio("Fulfillement", ["Pickup", "Delivery"])
    show_chart = st.checkbox("Show Sample Sales Chart")

# TODO 4 - Step 6: Calculate unit_price, subtotal and discounted_subtotal.
# Call your functions. Calculate discount_amount, delivery_fee and total.
# Pickup costs 0; Delivery uses shipping_fee(subtotal).
unit_price = menu[product]
subtotal = unit_price * quantity
discounted_subtotal = apply_discount(subtotal)
discount_amount = subtotal - discounted_subtotal
if fulfillment == "Delivery":
    delivery_fee = shipping_fee(subtotal)
else:
    delivery_fee =0.00
total = discounted_subtotal + delivery_fee

# TODO 5 - Step 7: Show the quote in two columns with dollars to 2 decimals.
# Include product, quantity, unit price, fulfillment, subtotal, discount,
# delivery fee and final total. Keep this outside the button block.
st.subheader("Your Order Quote")
col1, col2 = st.columns(2)
with col1:
    st.write(f"Product: {product.title()}")
    st.write(f"Quantity: {quantity}")
    st.write(f"Unit Price: ${unit_price:.2f}")
    st.write(f"Fulfillment: {fulfillment}")
with col2:
    st.write(f"Subtotal: ${subtotal:.2f}")
    st.write(f"Discount: ${discount_amount:.2f}")
    st.write(f"Delivery Fee: ${delivery_fee:.2f}")
    st.write(f"Final Total: ${total:.2f}")

# TODO 6 - Step 8: Build and display the menu table from the menu dictionary.
# Add a clearly labeled fictional sample-sales chart controlled by show_chart.
st.subheader("Bakery Menu")
menu_data = {
    "Product": list(menu.keys()),
    "Price": list(menu.values())
}
st.table(menu_data)
if show_chart:
    st.subheader("Fictional Sample Sales")
    st.bar_chart(sample_sales, x="Product", y="Units sold")

# TODO 7 - Step 9: Add a Check quote button.
# Warn if customer_name is blank or spaces only. Otherwise show a check message.
# Do not claim that an order was saved, submitted or paid for.
if st.button("Check Quote"):
    if not customer_name.strip():
        st.warning("Please enter your name.")
    else:
        st.success(f"Quote checked for {customer_name}!")

# TODO 8: Test, add your own comments and remove the starter info message.
# Do not upload your submission report or screenshots to this public repository.

# The discount helps customers save money on larger orders.
# The calculator adds the bakery items and delivery fee.
# The sales chart displays fictional bakery sales.
