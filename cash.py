products = []

while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ') # 如果商品是 q 就不用問 price
	price = int(price)
	#p = []
	#p.append(name)
	#p.append(price)
	# 將 9~10 簡化為 p = [name , price] 
	products.append([name , price])
print(products)

for p in products:
	print(p[0] , '價格是' , p[1])


with open('prodcts.csv','w', encoding= 'utf-8') as f:  #寫入和讀取檔案都會遇到編碼問題
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')