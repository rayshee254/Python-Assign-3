
def calculate_discount(price, discount_percent):
    """Calculate final price after applying discount if eligible"""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price

while True:
    try:
        price = float(input("Enter original price: "))
        if price <= 0:
            print("Price must be a positive number. Try again.")
            continue
            
        discount_percent = float(input("Enter discount percentage: "))
        if discount_percent < 0 or discount_percent > 100:
            print("Discount must be between 0-100%. Try again.")
            continue
            
        break 
        
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"\n🎉 {discount_percent:.1f}% discount applied!")
    print(f"Original price: \t${price:.2f}")
    print(f"Final price: \t\t${final_price:.2f}")
else:
    print(f"\nℹ️  No discount applied (needs 20%+ discount)")
    print(f"Final price remains: \t${final_price:.2f}")
