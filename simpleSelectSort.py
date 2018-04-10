'''
总目标：简单选择排序
	针对列表[90,34,-23,18,12]从小到大进行排序，
	每趟找出最小的/最大的第一个数换位置
	第一趟:[-23,34,90,18,12]
'''

# 声明列表
list1 = [90,34,-23,18,12]


'''
# 第一趟排序算法
mi = list1[0]
for a in range(len(list1)):
	if mi > list1[a]:
		mi = list1[a]
		num = a
		print(mi)
c = list1[0] 
list1[0] = mi 
list1[num] = c

for y in list1:
	print(y)
'''

for x in range(0,len(list1)):
	mi = list1[x]
	for a in range(x,len(list1)):
		if mi > list1[a]:
			mi = list1[a]
			num = a
			print("第%s次循环---->当前最小值:%s" %((x+1),mi))
	print("\n")
	c = list1[x] 
	list1[x] = mi 
	list1[num] = c

print("从小到大的序列为:")
for b in list1:
	print(b,'  ',end = '')
