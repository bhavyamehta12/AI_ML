while True:
    user_input = input("Enter Your Input : ")
    user = user_input.split(",")
    quantity = int(user[0])
    price=int(user[1])
    discount = int(user[2])
    discount_price = quantity-round(quantity*(discount/100))
    tax = quantity*0.05
    final = discount_price+tax
    if "done" in user.lower().strip():
        break
    if user == "":
        continue
    if len(user)!=3:
        print("Invalid input")
        continue
    print("Original amount : ₹"+quantity)
    print("Discount : ₹"+discount_price)
    print("Discounted Amount : ₹",discount_price)
    print("Tax : ₹",tax)
    print("Final price : ₹",final)
    

