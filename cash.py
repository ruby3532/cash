import os # 作業系統 operating system 

# 讀取檔案
products = [] # 不管檔案在不在，都要執行此程式且等等也會用到。

# 檢查檔案在不在
if os.path.isfile('prodcts.csv'):
	print('yeah 找到檔案了')
	with open('prodcts.csv', 'r', encoding= 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name , price])	
	print(products)
else:
	print('找不到檔案....')


# 讓使用者輸入
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

# 印出所有購買記錄
for p in products:
	print(p[0] , '價格是' , p[1])

# 寫入檔案
with open('prodcts.csv','w', encoding= 'utf-8') as f:  #寫入和讀取檔案都會遇到編碼問題
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')