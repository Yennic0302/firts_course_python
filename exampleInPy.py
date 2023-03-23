userData ={
    "name": "yender",
    "last_name": "rodriguez",
    "age": 20,
    "mail": "yender.yr45@gmail.com",
    "money": 600
}

products = [{"name":"phone", "price": 200},{"name":"computer", "price": 500}]

if_want_product = True

if if_want_product:
    print(products)
    totalPrice = products[0]['price'] + products[1]['price']
    if totalPrice > userData["money"]:
        print(f"you can not purchase this, the rest of money is {totalPrice - userData['money']}")