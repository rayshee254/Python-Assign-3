def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (discount_percent / 100)
        return price - final_price
    else:
        return price
price = float(input("Original price : "))
discount_percent = float(input("Discount percentage: "))
final_price = calculate_discount(price, discount_percent)
print(f"The final price after the discount is: {final_price:.2f}")
