
amount = float(input("Enter the amount in Ksh: "))
if amount >= 1000:
    discount = 0.005 * amount
    final_amount = amount - discount
    print("Discount is ", discount)
else:
    print("No discount applied")
