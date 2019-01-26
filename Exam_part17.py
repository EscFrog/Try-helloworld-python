product_list = ["풀", "가위", "크레파스"]
price_list = [800, 2500, 5000]
product_dict = {name : price for name, price in zip(product_list, price_list)}

print(product_dict)