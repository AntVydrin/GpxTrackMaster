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

    colors = [
              #'aquamarine',
              #'azure',
              #'beige',
              #'bisque',
              'black',
              #'blanchedalmond',
              'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue',
              #'cornsilk',
              #'crimson',
              'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen',
              'darkgrey', 'darkkhaki', 'darkmagenta',              
              'darkolivegreen', 'darkorange', 'darkorchid', 'darkred',
              'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise',
              'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick',
              'aqua',
              #'floralwhite',
              'forestgreen', 'fuchsia',
              #'gainsboro', 'ghostwhite',
              'gold',
              'goldenrod', 'gray', 'green', 'greenyellow',
              'grey',
              #'honeydew',
              'hotpink', 'indianred', 'indigo',
              #'ivory',
              #'khaki', 'lavender', 'lavenderblush',
              'lawngreen',
              #'lemonchiffon',
              'lightblue', 'lightcoral',
              #'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey',
              #'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue',
              #'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid',
              'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred',
              'midnightblue',
              #'mintcream', 'mistyrose',
              #'moccasin',
              #'navajowhite',
              'navy',
              #'oldlace',
              'olive', 'olivedrab',
              'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip',
              'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'rebeccapurple', 'red', 'rosybrown', 'royalblue',
              #'aliceblue',
              #'antiquewhite',
              'yellow', 'yellowgreen',
              'saddlebrown', 'salmon', 'sandybrown', 'seagreen',
              #'seashell',
              'sienna', 'silver', 'skyblue', 'slateblue', 'slategray',
              'slategrey',
              #'snow',
              'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat',
              #'white',
              #'whitesmoke',
              ]
    
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
            plt.plot(x, y, label = oldDate, color=theColor, lw = 4)
            
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
    plt.plot(x, y, label = plotDataDate[len(plotDataDate)-1], color=theColor, lw = 4)
    
    # включаем основную сетку
    plt.grid(which='major')
    plt.yticks(fontsize=17)
    plt.xticks(fontsize=20)
  
    # включаем дополнительную сетку
    # включаем дополнительные отметки на осях
    plt.minorticks_on()
    plt.grid(which='minor', linestyle=':')
    plt.tight_layout()
    # ax = plt.gca()
    # ax.axes.xaxis.set_visible(False)

    # Разрешить двигать легенду
    legend_obj = plt.legend(loc='upper left') #mode='expand', ncol=5
    legend_obj.set_draggable(True)
    #plt.title("Трек")

    plt.show()

