# 1. Project Title
"""Super Market Bill Project"""

# 2. Get customer name
# Used to get the customer's name.
name = input("PLEASE ENTER YOUR NAME: ")

# 3. List of available items
# Used to display product names and prices.
lists = """
rice    RS 10/kg
sugar   RS 8/kg
oil     RS 30/kg
salt    RS 25/kg
paneer  RS 40/kg
maggie  RS 12/pack
boost   RS 200/bottle
"""

# 4. Store item prices
# Dictionary is used to store product names and prices.
items = {
    "rice": 10,
    "sugar": 8,
    "oil": 30,
    "salt": 25,
    "paneer": 40,
    "maggie": 12,
    "boost": 200
}

# 5. Initialize bill variables
# Empty list stores purchased item details.
# totalprice stores the total bill amount.
pricelist = []
totalprice = 0

# 6. Main menu
# while True is used to repeat the menu until the user exits.
while True:
    option = input("Press 1 for list or 2 for exit: ")

    # 7. Exit option
    # break is used to stop the loop.
    if option == "2":
        print("Thank you for shopping!")
        break

    # 8. Display product list
    elif option == "1":
        print(lists)

        # 9. Shopping loop
        # Allows the customer to purchase multiple items.
        while True:
            inp1 = input("To buy press 1 or press 2 to exit: ")

            if inp1 == "2":
                break

            elif inp1 == "1":
                # 10. Select product
                # lower() converts the input into lowercase.
                item = input("Choose your item: ").lower()

                # 11. Check product availability
                # Checks whether the selected item exists.
                if item in items:

                    # 12. Get quantity
                    # isdigit() checks whether the input contains digits.
                    while True:
                        quantity_input = input("Enter quantity: ")

                        if quantity_input.isdigit():
                            quantity = int(quantity_input)
                            break
                        else:
                            print("Please enter a valid quantity.")

                    # 13. Calculate item price
                    # Quantity is multiplied by the item price.
                    price = quantity * items[item]

                    # 14. Store purchased item details
                    # append() adds item details to the list.
                    pricelist.append(
                        (item, quantity, items[item], price)
                    )

                    # 15. Calculate total price
                    totalprice += price

                    print("Item added successfully!")

                else:
                    # 16. Invalid product message
                    print(
                        "Selected item is not available. "
                        "Sorry for the inconvenience."
                    )

            else:
                print("Please enter 1 or 2.")

        # 17. Generate bill
        # Bill is printed only if the customer purchases items.
        if totalprice > 0:

            # 18. Calculate GST
            # Adds 18% GST to the total amount.
            tax = (totalprice * 18) / 100
            finalamount = totalprice + tax

            # 19. Print bill heading
            print("\n" + "=" * 70)
            print(" " * 25 + "PYTHONLIFE SUPERMARKET")
            print(" " * 30 + "HYDERABAD")
            print("=" * 70)

            # 20. Display customer name
            print("Name:", name)
            print("-" * 70)

            # 21. Display bill column headings
            print(
                "S.No",
                " " * 8,
                "Item",
                " " * 8,
                "Quantity",
                " " * 5,
                "Price"
            )

            # 22. Display purchased items
            # enumerate() provides serial numbers.
            for i, (item, quantity, rate, price) in enumerate(pricelist, 1):
                print(
                    i,
                    " " * 12,
                    item,
                    " " * (12 - len(item)),
                    quantity,
                    " " * 10,
                    "RS",
                    price
                )

            # 23. Display final bill details
            print("-" * 70)
            print("Total Amount : RS", totalprice)
            print("GST (18%)    : RS", tax)
            print("Final Amount : RS", finalamount)

            # 24. Thank you message
            print("=" * 70)
            print(" " * 25 + "THANK YOU! VISIT AGAIN")
            print("=" * 70)