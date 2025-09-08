# Shopping products using dictionary

products = {
    "VIVO": 25000,
    "OPPO": 20000,
    "IPHONE": 85000,
    "ONEPLUS": 65000,
    "REDMI": 18000,
    "MOTOROLA": 26000,
    "SAMSUNG": 55000,
    "REALME": 22000,
    "POCO": 20000,
    "GOOGLEPIXEL": 70000,
    "NOKIA": 15000,
    "HONOR": 28000,
    "ASUS": 30000,
    "INFINIX": 12000,
    "TECNO": 14000,
    "IQOO": 30000,
    "SONY": 60000,
    "LAVA": 10000,
    "MICROMAX": 9000,
    "LENOVO": 15000,
    "Q":0
}
quantity=[]
total=0
bproducts = {}
i=0
while True:
    product = input("Enter the Product You want to buy (Q to Quit): ").upper()
    while True:
        if product not in products:
            print(f"{"":8}The Mobile is not available....")
            product = input("Enter the Product You want to buy (Q to Quit): ").upper()
        else:
            break
    if product == "Q":
        break
    else:
        qty = int(input("Quantity: "))
        quantity.append(qty)
        total+=(qty*products.get(product))
        bproducts.update({product:(qty*products.get(product))})
print("--------------------------INVOICE---------------------------")
print(f"{"BRAND":^15} {"QTY":^10} {"PRICE":^10} {"TOTAL":^10}")
for key,value in bproducts.items():
    print(f'{key:^15} {quantity[i]:^10} {products.get(key):^10} Rs.{value:>10}')
    i+=1
print("---------------------------------------------------------")
print("The Total Price for the products on Cart is Rs.",total)