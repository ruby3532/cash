products = []

while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ') # 如果商品是 q 就不用問 price
	#p = []
	#p.append(name)
	#p.append(price)
	# 將 9~10 簡化為 p = [name , price] 
	products.append([name , price])
print(products)

pp = products[0][0]
print(pp)