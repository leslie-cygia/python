import matplotlib.pyplot as plt
from random import randint
import pygal

# 折线图
def linechart():
	input_squares = [1,2,3,4,5]
	squares = [1,4,9,16,25]
	plt.plot(input_squares,squares,linewidth=5)
	# 设置图表标题，并给坐标轴加上标签
	plt.title('Squares Numbers',fontsize=24)
	plt.xlabel('Value',fontsize=14)
	plt.ylabel('Squares of Value',fontsize=14)
	# 设置刻度标记的大小
	plt.tick_params(axis='both',labelsize=14)

	plt.show()

# 单个散点图
def scatterChart_single():
	plt.scatter(2,4)

	plt.title('Squares Numbers',fontsize=24)
	plt.xlabel('Value',fontsize=14)
	plt.ylabel('Squares of Value',fontsize=14)

	plt.tick_params(axis='both',which='major',labelsize=14)	

	plt.show()

# 散点图
def scatterChart():
	x_values = [1,2,3,4,5]
	y_values = [1,4,9,16,25]
	plt.scatter(x_values,y_values,s=100)

	plt.title('Squares Numbers',fontsize=24)
	plt.xlabel('Value',fontsize=14)
	plt.ylabel('Squares of Value',fontsize=14)
	plt.tick_params(axis='both',which='major',labelsize=14)

	plt.show()

# 自动计算数据
def auto_scatter():
	x_values = list(range(1,1001))
	y_values = [x**2 for x in x_values]
	plt.scatter(x_values,y_values,s=10)

	plt.title('Squares Numbers',fontsize=24)
	plt.xlabel('Value',fontsize=14)
	plt.ylabel('Squares of Value',fontsize=14)

	# 设置每个坐标轴的取值范围
	plt.axis([0,1100,0,1100000])

	plt.show()

# 直方图
# 掷骰子，从1~6中选出一个随机数，多次循环，查看各值的频率
def histogram():
	max_num = 6
	result = []
	for i in range(1,101):
		result.append(randint(1,max_num))
	# print(result)
	frequencies = []
	for i in range(1,max_num+1):
		frequency = result.count(i)
		frequencies.append(frequency)
	# print(frequencies)
	# 对结果进行可视化
	hist = pygal.Bar()
	hist.x_labels = ['1','2','3','4','5','6']
	hist.x_title = 'Result'
	hist.y_title = 'Frequency of Result'

	hist.add('D6',frequencies)
	hist.render_to_file('die_visual.svg')

# 直方图
# 掷两个骰子，从1~6中选出一个随机数，多次循环，查看各值的频率
def histogram_double():
	max_num = 6
	result = []
	for i in range(1,1001):
		result.append(randint(1,max_num)+randint(1,max_num))
	frequencies = []
	for i in range(2,max_num*2+1):
		frequency = result.count(i)
		frequencies.append(frequency)
	# 结果可视化
	hist = pygal.Bar()
	hist.x_labels = range(2,max_num*2+1)
	hist.x_title = 'Result'
	hist.y_title = 'Frequency of Value'

	hist.add('D6 + D6',frequencies)
	hist.render_to_file('die_visual.svg')


# ---------------- 测试 ---------------------#
# linechart()
# scatterChart_single()
# scatterChart()
# auto_scatter()
histogram()
# histogram_double()
