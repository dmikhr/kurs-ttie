# -*- coding: utf-8 -*-

# Расчёт зависимостей температур горячего и холодного теплоносителей от площади теплообмена 

import numpy
import matplotlib.pyplot as pl
from pylab import *

ROUND = 1 # округление до 1 знака после запятой

r = lambda x: round(x, ROUND) # округление результата

t1 = 120; t2 = 60 # температуры теплоносителей на входе теплообменного аппарата
t11 = 90; t22 = 80 # температуры теплоносителей на выходе теплообменного аппарата

F = numpy.arange(0,1.1,0.1) # нормированная площадь теплообмена от 0 до 1 с шагом 0.1

plotdata = {'t1F':[], 't2F':[]} # словарь массивов с результатами расчётов температур

# разница температур на входе
dtin = t1 - t2 
# разница температур на выходе
dtout = t11 - t22

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
pl.xlabel(u'Зависимость температуры теплоносителя от площади теплообмена, F')
pl.ylabel(u't')
pl.plot(F, plotdata['t1F'], "-s", label=u'Горячий теплоноситель', color='black')
pl.plot(F, plotdata['t2F'], "--o", label=u'Холодный теплоноситель', color='blue')
legend(loc='lower center', prop={'size':8})
pl.grid()
pl.show() # вывод графика
