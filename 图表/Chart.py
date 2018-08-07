import matplotlib.pyplot as plt

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



# linechart()
# scatterChart_single()
scatterChart()