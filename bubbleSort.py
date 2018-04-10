# 声明列表
list1 = [90,34,-23,18,12,334,-33]
# 外层循环控制比较的趟数
for x in range(0, len(list1)-1):
	# 内层循环控制 控制每趟比较的次数
	for y  in range(0, len(list1)-x-1):
		# 依次进行比较
		if list1[y] > list1[y+1]: # 小于号是降序排列 大于号是升序排列
			# 交换位置
			typ = list1[y]
			list1[y] = list1[y+1]
			list1[y+1] = typ

# 遍历排序后的列表
for z in list1:
	print(z)
