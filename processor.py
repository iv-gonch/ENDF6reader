#!/usr/bin/python
# -*- coding: utf-8 -*-

# Считывает строки с конкретными MF и MT из конвертированного файла. 
# Записывает в папку /processed/filename/MF**_MT***/NK**_NE*** функцию p_i(theta) для каждой энергии налетающей альфа частицы

from __future__ import print_function
from __future__ import division
import numpy as np
import math
import sys
import os

import constants
import converter
import polynomials

def processData(fname, MF, MT):

    if not os.path.isfile('converted/' + fname):    # проверка наличия конвертированного файла
        print('There is no converted', fname, 'file!', file=sys.stdout)
        converter.convertENDF(fname)
    f = open('converted/' + fname)

    f1 = open('converted/' + fname) # тут мы просто открываем любой файл. Потом, в цикле, 
    # будем открывать нужные файлы, когда узнаем их расположение. (Цикл начинается с закрытия файла, для этого нужна эта строка)

    if not os.path.isdir('processed'):  # проверка наличия директории
        os.mkdir('processed')
    
    if not os.path.isdir('processed/' + fname): # проверка наличия директории
        os.mkdir('processed/' + fname)

    if not os.path.isdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT)): # проверка наличия директории
        os.mkdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT))

    NWlineNumber = [0]  # номер подтаблицы (каждая соответствует своей энергии налетающей частицы E_in)
    tmp = 0     # тк в ENDF таблицы размазанны в строки по 6 элементов, иногда несколько ячеек в строке остаются пустыми.
                # Эта переменная позволяет не записывать пустые ячейки в память 
    counter = 0 # счётчик номера NW (всего их NE штук)
    NP = 0      # нужен чтобы правильно определять номер строки с NE 
    
    for line in f.readlines():  # считываем построчно
        word = np.zeros(10, dtype = float)  # каждый элемент строки файла будем записывать в виде float в массив numpy. Изначально всё - вещественны нули
        if (line[83:85] != ' 0' and line[83:85] != ' 1'):   # отсекаем строки с текстом (те. с MF=' 1' или =' 0', MT=' 451')
            for i in range(10): # цикл нужен чтобы под float() попали только элементы строки, состоящие из цифр (иначе ошибка)
                if (line.strip('|').split('|')[i].strip() != ''):   # пустые слова остаются вещественными нулями в word[]
                    word[i] = float(line.strip('|').split('|')[i].strip())  # в конвертированных файлах разделителем является '|' 

        if (int(word[constants.ENDF.MFindex]) == MF and int(word[constants.ENDF.MTindex]) == MT): # читаем только нужные строчки по MF, MT

            # ниже просто запоминаем шапку таблицы, может потом пригодится. Вид первых трёх строк всегда одинаков (в MF6 точно)
            # подробнее про смысл констант см. файл constants.py (краткая справка) или ENDF6 formats manual 
            # https://www-nds.iaea.org/public/endf/endf-manual.pdf
            if (int(word[constants.ENDF.NSindex]) == 1):    # ищем NK. Он всегда 
                ZA = int(word[constants.ENDF.ZAindex])
                AWR = float(word[constants.ENDF.AWRindex])
                JP = int(word[constants.ENDF.JPindex])
                LCT = int(word[constants.ENDF.LCTindex])
                NK = int(word[constants.ENDF.NKindex])
            
            if (int(word[constants.ENDF.NSindex]) == 2):    # ищем NP. Он всегда на 2й строчке
                ZAP = int(word[constants.ENDF.ZAPindex])
                AWP = float(word[constants.ENDF.AWPindex])
                LIP = int(word[constants.ENDF.LIPindex])
                LAW = int(word[constants.ENDF.LAWindex])
                if (LAW != 2): print('LAW != 2 for', fname)
                # NR = int(word[constants.ENDF.NRindex])      # встречается ещё один NR. Но оба не используются
                NP = int(word[constants.ENDF.NPindex])
            
            if (int(word[constants.ENDF.NSindex]) == 3): 
                NBT = int(word[constants.ENDF.NBTindex])    # не уверен что это NBT
                INT = int(word[constants.ENDF.INTindex])    # не уверен что это INT
            
            # if (int(word[constants.ENDF.NSindex]) <= 3): # вывод шапки таблицы в консоль

            if (int(word[constants.ENDF.NSindex]) == 4 + math.ceil(NP/3)):   # если номер строки таков, то в ней лежит NE
                NE = int(word[constants.ENDF.NEindex])  # записываем чему равно NE
                NWlineNumber[0] = int(word[constants.ENDF.NSindex] + 2) # записываем в какой строке ожидать следующее значение NW

            if (int(word[constants.ENDF.NSindex]) == int(NWlineNumber[counter])): # номер строоки с очередным NW

                counter += 1    # счётчик номера E_in                 
                NWlineNumber.append(NWlineNumber[counter-1] + math.ceil(int(word[constants.ENDF.NWindex])/6) + 1)
                # записываем в какой строке ожидать следующее значение NW

                f1.close()

                if not os.path.isdir('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT)):
                    os.mkdir ('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT))
                f1 =     open('processed/' + fname + '/MF' + str(MF) + '_MT' + str(MT) + '/NK' + str(NK) + '_NE' + str(counter), 'w')
                # создаём и открываем файл на пути /processed/C13/MF6_MT50/NK1_NE47 (пример)
                f1.write('MF = ' + str(MF) + '\tMT = ' + str(MT) + '\nAmount of files in directory: ' + str(NE) + '\n')
                # записываем MF, MT и число табличек с разными энергиями влетающих частиц E_in
                f1.write('\nIncident particle energy (eV) = \n' + str(word[constants.ENDF.IncidentEnergyindex]) + '\n\nAmount of points: ' + str(int(word[constants.ENDF.NWindex])) + '\n')
                # записываем E_in и число точек

                if (int(word[constants.ENDF.LANGindex]) != 0): print('LANG != 0 for', fname, 'line', int(word[constants.ENDF.NSindex]))
                tmp = int(word[constants.ENDF.NWindex]) # счётчик количества точек для конкретного E_in
                # print ('NW', counter, 'found:', NWlineNumber[counter])

            if (counter > 0 and int(word[constants.ENDF.NSindex]) > NWlineNumber[counter-1]):
                for i in range(6):
                    if(i < tmp):    # чтобы не выводить нули из строки, которые являются не значениями, а символами пустых ячеек                      
                        f1.write(str(word[i]) + '\n')   # записываем в файл экспериментальное значение без изменений
                tmp -= 6    # строка прошла, значит количество оставшихся значений уменьшилось на 6            

    f.close()