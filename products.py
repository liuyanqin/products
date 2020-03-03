products = []  #装商品的清单
while True:
	name = input('请输入商品名称：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	#p = []  #装商品名称和价格的小清单   1
	#p.append(name)   1
	#p.append(price)   1
	#p = [name, price]  2
	products.append([name, price])  # 3
print(products)