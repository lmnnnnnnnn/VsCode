from matplotlib import pyplot
#横坐标
year=[2010,2012,2014,2016]
#纵坐标
perple=[20,40,60,100]
perple2=[49,59,69,79]
#生成折线图：函数polt
pyplot.plot(year,perple)
pyplot.plot(year,perple2)
#设置横坐标说明
pyplot.xlabel('year')
#设置纵坐标说明
pyplot.ylabel('population')
#添加标题
pyplot.title('Population year correspondence')
#设置纵坐标刻度
pyplot.yticks([0, 25, 50, 75, 90])
#显示图表
pyplot.show()