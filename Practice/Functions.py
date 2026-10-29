def calculate_order_total(
        price,
        quantity,
        discount=0,
        tax_rate=0.18,
        currency="INR"
):
    if price<0:
        raise ValueError("Price must be greater than 0")
    if quantity<=0:
        raise ValueError("Price must be greater than 0")
    if not 0<=discount<=100:
        raise ValueError("Discount must be between 0 to 100")
    product = price * quantity
    discounted = product * (1-discount/100)
    taxed = product * (1-tax_rate/100)
    final = product-discounted+taxed
    return final
