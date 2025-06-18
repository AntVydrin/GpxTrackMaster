#!/usr/bin/python3
# -*- coding: utf-8 -*import

import ReadRawGpxData as readGPX
import ProcessingOfRawData as PRWD
import CreatePlot as crP
import sys

import easygui

import matplotlib.pyplot as plt
# Импортируем класс кнопки
from matplotlib.widgets import Button

def onButtonAddClicked(event):
    """!!! Обработчик события для кнопки "Добавить"""
    global graph_axes
    global axes_button_add
    global fig
    graph_axes.clear()
    
    #axes_button_add.set_visible(False)
    fileName=''
    fileName = easygui.fileopenbox(default='*.gpx',filetypes='*.gpx')
    if type(fileName) is str:
        processedData = ReadData(fileName)
        crP.CreatePlot(processedData, fig, graph_axes)
        PlotSettings(graph_axes)
    plt.draw()

def onButtonSaveClicked(event):
    #Сохранить в изображение без кнопок
    global axes_button_save
    global axes_button_add
    axes_button_add.set_visible(False)
    axes_button_save.set_visible(False)
    plt.savefig('Trek.png')
    axes_button_add.set_visible(True)
    axes_button_save.set_visible(True)

def PlotSettings(graph_axes):
     # включаем основную сетку
    graph_axes.grid(which='major')
      
    # включаем дополнительную сетку
    # включаем дополнительные отметки на осях
    graph_axes.minorticks_on
    graph_axes.grid(which='minor', linestyle=':')
    
    graph_axes.legend()
    
    # Разрешить двигать легенду
    legend_obj = graph_axes.get_legend()
    if legend_obj!=None:
    #legend_obj = plt.legend(loc='upper left') #mode='expand', ncol=5
        legend_obj.set_draggable(True)
    #legend_obj.set_draggable(True)
        legend_obj.set_loc('upper left')
    
def ReadData(fileName):
    rawData = readGPX.RawDataFind(fileName)
    ProcessedData = PRWD.TrekDataList(rawData)
    return ProcessedData

if __name__ == '__main__':
    fig, graph_axes = plt.subplots()
    
     # Выделим область, которую будет занимать график
    fig.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.15)

    # Создадим оси для кнопки
    axes_button_add = plt.axes([0.5, 0.01, 0.25, 0.075])
    axes_button_save = plt.axes([0.05, 0.01, 0.25, 0.075])


    # Создадим кнопку
    button_add = Button(axes_button_add, 'Трек gpx')
    button_save = Button(axes_button_save, 'Сохранить картинку')

    # !!! Подпишемся на событие обработки нажатия кнопки
    button_add.on_clicked(onButtonAddClicked)
    button_save.on_clicked(onButtonSaveClicked)

    #PlotSettings(graph_axes)

    plt.show()
