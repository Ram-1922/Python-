#Shopping Cart Program

products=[]
prices=[]
total=0

while True:
    product= input("Enter the Product you want to buy (Enter q to quit):")
    if product.lower() == "q":
        break
    else:
        price=float(input(f"Enter the Price of the {product}: Rs."))
        products.append(product)
        prices.append(price)
print("---------Shopping Cart---------")
for i in range(0,len(products)):
    print(f"{products[i]:>10} - {prices[i]:<10.2f}")
for i in prices:
    total+=i
print(f"The Total price is Rs.{total:.2f}")