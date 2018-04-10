'''
总目标：希尔排序
	针对列表[90,34,-23,18,12]从小到大进行排序，
	第一趟: 90 18 ,34 12, -23 -----> 18,12,-23,90,34
'''
list1 = [90,34,-23,18,12]
'''
# 第一趟移动算法
for x in range(len(list1)-3):
	if list1[x] > list1[x+3]:
		c = list1[x]
		list1[x] = list1[x+3]
		list1[x+3] = c
		print(list1[x])
		print(list1[x+3])
		print("********************")
else:
	continue
'''
# 声明一个变量记录移动次数
sum = 0
# 外层循环控制增量
for y in range(3,0,-1):
	# 内层循环控制次数
	for x in range(len(list1)-y):
		if list1[x] > list1[x+y]:
			# 交换位置
			c = list1[x]
			list1[x] = list1[x+y]
			list1[x+y] = c
			print(list1[x])
			print(list1[x+y])
			print("第%s趟中的移动" %((len(list1)-1)-y))
			sum += 1
			print("********************")
	else:
		continue
print("从小到大的序列为:")
for b in list1:
	print(b,'  ',end = '')
print("共经过了%s次移动" %sum)
