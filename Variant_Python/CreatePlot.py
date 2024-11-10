import matplotlib.pyplot as plt
import matplotlib.colors

#TODO: Отобразить снизу на оси дни с помощью text
def CreatePlot(processedData):
    _processedData = [{"elev": 0.0, "Length": 0.0, "date": "21-10-2005"}]
    _processedData = processedData
    plotDataElev = []
    plotDataDistance = []
    plotDataDate = []
    oldDate = _processedData[0]["date"]
    newDay = False
    dayCount = 0

    #TODO: сделать проверку превышения размера и выбрать нормальные цвета
    colors = list(matplotlib.colors.CSS4_COLORS.keys()) #перечисление цветов
    
    for thePD in _processedData:
        insData = list(thePD.values())

        plotDataElev.append(insData[0])
        plotDataDistance.append(insData[1]/1000)
        plotDataDate.append(insData[2])
        
        if thePD["date"] != oldDate:
            newDay = True
        if newDay:
            newDay = False
            theColor = colors[dayCount]
            dayCount += 1
            #Вставляем график для каждого дня
            x = plotDataDistance.copy()
            y = plotDataElev.copy()
            plt.plot(x, y, label = oldDate, color=theColor)
            
            oldDate = insData[2]
            plotDataElev = []
            plotDataDistance = []
            plotDataDate = []
            plotDataDay = []

            plotDataElev.append(insData[0])
            plotDataDistance.append(insData[1]/1000)
            plotDataDate.append(insData[2])

    x = plotDataDistance.copy()
    y = plotDataElev.copy()
    theColor = colors[dayCount]
    plt.plot(x, y, label = plotDataDate[len(plotDataDate)-1], color=theColor)
    
    # включаем основную сетку
    plt.grid(which='major')
    # включаем дополнительную сетку
    # включаем дополнительные отметки на осях
    plt.minorticks_on()
    plt.grid(which='minor', linestyle=':')
    plt.tight_layout()
    # ax = plt.gca()
    # ax.axes.xaxis.set_visible(False)

    # Разрешить двигать легенду
    legend_obj = plt.legend(loc='upper left')
    legend_obj.set_draggable(True)
    #plt.title("Трек")

    plt.show()

