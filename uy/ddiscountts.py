pprice = float(input("product price: "))
discount = float(input("discoint: " ))
vat = pprice * 0.77
ddiscount = pprice * (discount / 100)
dprice = pprice - ddiscount 
print("price = ", pprice, "discount = ", discount, "vat = 23%")
print("vat amount = ",pprice - vat,"price without vat =", vat, "discount amount = ", ddiscount, "price after discount = ", dprice)