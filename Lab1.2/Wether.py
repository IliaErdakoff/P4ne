from matplotlib import pyplot
from openpyxl.reader.excel import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
x = sheet['A'][1:]
y1 = sheet['C'][1:]
y2 = sheet['D'][1:]

def getvalue (x):
    return x.value

list_x = list(map(getvalue,x))
list_y1 = list(map(getvalue,y1))
list_y2 = list(map(getvalue,y2))

pyplot.xlabel('Годы')
pyplot.ylabel('Относительная температура/Активность')


pyplot.plot(list_x,list_y1,label="Относительная температура")
pyplot.plot(list_x,list_y2,label="Активность")
pyplot.legend(loc='upper left')
pyplot.show()
