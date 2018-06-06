#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 排序的稳定性是指排序前后相同的两个元素的相对位置不发生变化

# 算法的五大思想：
# 1、分治
# 2、动态规划算法
# 3、贪心算法
# 4、回溯
# 5、分支限界

#  冒泡排序
#  基本思想：
#  重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序不满足则互相交换，直到无需交换。
#  
#  复杂度：O(n^2)
def bubbleSort(arry):
	# 外部循环从i开始，遍历整个数据
	for i in range(0, len(arry) - 1):
		# 在已经排序的序列里进行比较找到需要两两互换的元素
		# 排好的序列会随i值增加，内层循环不必每次比较n次，只需比较n-i次
		for j in range(0, len(arry) - i - 1):
			if arry[j] > arry[j + 1]:
				arry[j], arry[j + 1] = arry[j + 1], arry[j]
	return arry

def bubbleSort2(arry):
    length = len(arry)
    # 外层循环控制遍历全数据序列
    while length > 0:
        for i in range(length - 1):
            if arry[i] > arry[i+1]:
                arry[i] , arry[i+1] = arry[i+1], arry[i]
        length -= 1
    return arry

#  选择排序
#  基本思想：
#  每一次从待排序的数据元素中选出最小（或最大）的一个元素
#  存放在序列的起始位置
#  直到全部待排序的数据元素排完。 
#  
#  复杂度：O(n^2)，不稳定的排序方法（比如序列[5， 5， 3]第一次就将第一个[5]与[3]交换，导致第一个5挪动到第二个5后面）
def selectSort(arry):
	# 外部循环从i开始，遍历整个数据
	for i in range(0, len(arry) - 1):
		# 可以最大或最小排序
		min = i
		for j in range(i + 1, len(arry)):
			if arry[j] < arry[min]:
				min = j
		arry[i], arry[min] = arry[min], arry[i]
	return arry

#  插入排序
#  基本思想：
#  把待排序的记录按其关键码值的大小逐个插入到一个已经排好序的序列中
#  直到所有的记录插入完为止，得到一个新的有序序列。
#  
#  复杂度：O(n^2)
def insertSort(arry):
	# 外部循环从i开始，遍历整个数据
	for i in range(1, len(arry)):
		# 内层循环从0~i，遍历查找比arry[i]
		j = i
		# 遍历查找合适的数据位置
		# 如果待比较的arry[j]小于已序列的数据，则循环移位替换已经比较的值；
		# 如果找到了需要插入的位置，则把temp插入到对应下标数据位置
		while (j > 0 and arry[j] < arry[j - 1]):
			arry[j], arry[j - 1] = arry[j - 1], arry[j]
			j -= 1
	return arry

#  希尔排序，是插入排序的一种又称“缩小增量排序”（Diminishing Increment Sort）是直接插入排序算法的一种更高效的改进版本。
#  基本思想：
#  把记录按下标的一定增量分组
#  对每组使用直接插入排序算法排序
#  随着增量逐渐减少，每组包含的关键词越来越多
#  当增量减至1时，整个文件恰被分成一组，算法便终止
#  
#  复杂度：O(n^2)，非稳定排序算法
def shellSort(arry, dividTo):
	n = len(arry)
	deltaT = 1
	while deltaT < n / dividTo:
		# 排序的趟数，当前不是最优，排序趟数应为log2(n+1)的整数部分
		deltaT = dividTo * deltaT + 1
	while deltaT >= 1:
		# 进行插入排序
		for i in range(deltaT, n):
			j = i
			while j >= deltaT and arry[j] < arry[j - deltaT]:
				arry[j], arry[j - deltaT] = arry[j - deltaT], arry[j]
				j -= deltaT
		# 进行下一分组的排序
		deltaT = deltaT // dividTo
	return arry

#  快速排序由C. A. R. Hoare在1962年提出。
#  基本思想：
#  1、通过一趟排序将要排序的数据分割成独立的两部分
#  2、其中一部分的所有数据都比另外一部分的所有数据都要小
#  3、然后再按此方法对这两部分数据分别进行快速排序
#  4、整个排序过程可以递归进行
#  以此达到整个数据变成有序序列。
#  
#  复杂度：通常O(nlog₂n)，最坏情况仍然是O(n^2)
def quickSort(arry, low, high):
	# 如果左边索引大于或者等于右边的索引就代表已经整理完成一个组了
	if low >= high:
		return
	i = low
	j = high
	key = arry[i]
	# 控制在当组内寻找一遍
	while i < j:
		# 结束的条件就是，
		# 1、找到一个小于或者大于key的数（大于或小于取决于你想升序还是降序）
		# 2、没有符合条件1的，并且i与j的大小没有反转
		while i < j and key <= arry[j]:
			# 向前寻找
			j -= 1
		# 找到一个这样的数后就把它赋给前面的被拿走的i的值
		# 如果第一次循环且key是 a[left]，那么就是给key
		arry[i] = arry[j]
		# i在当组内向前寻找，同上，不过注意与key的大小关系停止循环和上面相反，
		# 因为排序思想是把数往两边扔，所以左右两边的数大小与key的关系相反
		while i < j and key >= arry[i]:
			i += 1
		arry[j] = arry[i]
	# 当在当组内找完一遍以后就把中间数key回归
	arry[i] = key
	# 最后用同样的方式对分出来的左边的小组进行同上的做法
	quickSort(arry, low, i - 1)
	# 用同样的方式对分出来的右边的小组进行同上的做法
	quickSort(arry, i + 1, high)
	# 最后可能会出现很多分左右，直到每一组的i = j 为止
	return arry

#  堆排序
#  基本思想：是选择排序的一种
#  利用数组的特点快速定位指定索引的元素
#  堆分为大根堆和小根堆，是完全二叉树
#  树中任一非叶子结点的关键字均不大于（或不小于）其左右孩子（若存在）结点的关键字。
#  大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]
#  根据大根堆的要求可知，最大的值一定在堆顶
#  
#  发明过程：
#  1991年的计算机先驱奖获得者、斯坦福大学计算机科学系教授罗伯特·弗洛伊德(Robert W．Floyd）和威廉姆斯(J．Williams）
#  在1964年共同发明了著名的堆排序算法（ Heap Sort )
#  
#  时间复杂度：O(nlog₂n)，非稳定排序算法
def heapSort(arry):
	# 构建大根堆，只需要遍历树的 n / 2 - 1次即可完成有序树的创建
	for start in range(int(len(arry)/2) - 1, -1, -1):
		sink(arry, start, len(arry) - 1)
 	# 调整堆结构+交换堆顶元素与末尾元素
	for end in range(len(arry) - 1, 0, -1):
		# 交换堆顶最大值和最小叶子节点
		arry[0], arry[end] = arry[end], arry[0]
		# 重新建堆，每次找到一个最大值
		sink(arry, 0, end - 1)

	return arry
 
 # 根节点下沉，比上浮算法效率高
 # 时间复杂度：O(n) 
def sink(arry, start, end):
	root = start
	while True:
		# 左子节点的下标等于根节点 * 2 + 1
		leftChild = 2 * root + 1
		# 右子节点的下标等于根节点 * 2 + 2，即child + 1
		rightChild = leftChild + 1
		# 当前已无树可以构建，循环结束
		if leftChild > end:
			break
		# 保证右子节点不超过构建范围
		if rightChild <= end and arry[leftChild] < arry[rightChild]:
			# 获取到最大子节点，用于和根节点比较
			leftChild += 1
		if arry[root] < arry[leftChild]:
			# 根节点小于左子树，交换
			arry[root], arry[leftChild] = arry[leftChild], arry[root]
			# 构建下一个左子节点的子树节点
			root = leftChild
		else:
			break

#  二分查找
#  基本思想：
#  首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较
#  如果两者相等，则查找成功；否则利用中间位置记录将表分成前、后两个子表
#  如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表
#  否则进一步查找后一子表。
#  重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
#  
#  比较次数复杂度：a < log₂n < b (a,b,n ∈ Z+)
#  当顺序表有n个关键字时：
#  查找失败时，至少比较关键字a次；
#  查找成功时，最多比较关键字b次。
#  
#  时间复杂度：O(h)=O(log₂n)
def binarySearch(arry, key):
	low = 0
	high = len(arry) - 1
	while low <= high:
		mid = int((low + high)/2)
		if arry[mid] == key:
			return mid
		elif arry[mid] > key:
			high = mid - 1
		else:
			low = mid + 1
	return

a = [25, 26, 2, 6, 12, 23, 44, 77, 101, 33, 99, 88]
# a = ['z', 'b', 'c', 'a', 'm', 'h', 'f']
# print("冒泡排序：", bubbleSort(a))
# print("冒泡排序：", bubbleSort2(a))
# print("选择排序：", selectSort(a))
print("插入排序：", insertSort(a))
# print("希尔排序：", shellSort(a, 2))
# print("堆排序：", heapSort(a))
# print("快速排序：", quickSort(a, 0, len(a) - 1))
# print("二分查找：", a[binarySearch(a, 101)])

