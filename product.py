import os # operating system, 

读取档案
products = []
if os.path.isfile('products.csv'):#同样的资料夹有没有
#path is a module,这个查一下就可以只要可以查就不用背
	with open('products.csv','r', encoding='utf-8') as f:
		for line in f:
			if 'product, price' in line:
				continue #跳到下一回
			name, price = line.strip().split(',') 
			products.append([name, price])
	print(products)
else:
	print('file no found')


#让用户输入
while True:
	name = input('please input the name of product:')
	if name == 'q':
		break
	price = input('please input the price of products')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], 'price is', p[1])

#read file,
with open('products.csv', 'w', encoding='utf-8') as f:#help write Chinese) as f: # it is fine we dont have the file, because we are writing
	f.write('product, price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')# combine them to a bigger str
#when we add element, only same type of data could be added, and hence we need to convert price to str, or we cannot use +

















































