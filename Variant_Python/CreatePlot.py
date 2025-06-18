
import matplotlib.colors





#TODO: Отобразить снизу на оси дни с помощью text
def CreatePlot(processedData, fig, axes):
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

    #по умолчанию нужно отображать сетку
    #matplotlib.rcParams['axes.grid'] = True



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

             # Выделим область, которую будет занимать график
            #fig.subplots_adjust(left=0.7, right=1.0, top=1.0, bottom=0.8)

            axes.plot(x, y, label = oldDate, color=theColor, lw = 4)
            
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
    
   

    axes.plot(x, y, label = plotDataDate[len(plotDataDate)-1], color=theColor, lw = 4)
    
   




