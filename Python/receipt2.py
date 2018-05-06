def main():
    
    # Calculate total owed, assuming 8% tax / 15% tip
    subtotal = int(input("What was the meal cost? $"))
    tax = subtotal * .08
    tip = subtotal * .15
    total = subtotal + tax + tip
    
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Tip:", tip)
    print("Total:", total)

main()
