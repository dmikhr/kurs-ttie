# -*- coding: utf-8 -*-

# Расчёт зависимостей температур горячего и холодного теплоносителей от площади теплообмена 

import numpy
import matplotlib.pyplot as pl
from pylab import *

# Для работы программы на ОС Windows, в дополнение к модулям matplotlib и numpy
# необходимо установить модули dateutil, pyparsing и six
# установочные файлы модулей могут быть загружены с сайта
# http://www.lfd.uci.edu/~gohlke/pythonlibs
# работоспособность программы тестировалась с модулями %название_модуля%.win32-py2.7.exe

direct = True # прямоточная схема
#direct = False # противоточная схема

ROUND = 1 # округление до 1 знака после запятой

r = lambda x: round(x, ROUND) # округление результата

# температурный напор
delta = lambda x,y: [x[0] - x[1], y[0] - y[1]]

t1 = 120; t2 = 60 # температуры теплоносителей на входе теплообменного аппарата
t11 = 90; t22 = 80 # температуры теплоносителей на выходе теплообменного аппарата

F = numpy.arange(0,1.1,0.1) # нормированная площадь теплообмена от 0 до 1 с шагом 0.1

plotdata = {'t1F':[], 't2F':[]} # словарь массивов с результатами расчётов температур

if direct:
 # прямоточная схема
 # разница температур на входе и выходе
 dtin, dtout = delta([t1,t2], [t11,t22]) 
else:
 # противоточная схема
 # разница температур на входе и выходе
 dtin, dtout = delta([t11,t2], [t1,t22]) 

# разница температур горячего теплоносителя на входе и выходе
dt1 = abs(t11 - t1)
# разница температур холодного теплоносителя на входе и выходе
dt2 = abs(t22 - t2)

# расчёт теператур теплоносителя в зависимости от площади теплообмена
for f in F:

 # разница температур при заданной площади теплообмена
 dtF = dtin*(dtout/(dtin*1.0))**f

 # температура горячего теплоносителя при заданной площади теплообмена
 t1F = t1 + (dtF - dtin)/(1+dt2/(dt1*1.0)) 
 # температура холодного теплоносителя при заданной площади теплообмена
 t2F = t1F - dtF

 print f, r(dtF), r(t1F), r(t2F) # вывод расчётных значений для заданной площади теплообмена

 plotdata['t1F'].append(t1F)
 plotdata['t2F'].append(t2F)
 
# построение графика
Figure()
pl.xlabel('F')
pl.ylabel('t')
pl.plot(F, plotdata['t1F'], "-s", label='Hot heat carrier', color='black')
pl.plot(F, plotdata['t2F'], "--o", label='Cold heat carrier', color='blue')
legend(loc='lower center', prop={'size':8})
pl.grid()
pl.show() # вывод графика
