
# -*- coding: utf-8 -*import

import sys

#Чтение файла gpx  Запись высот и координат
#Возвращает лист trek
def ElevList(fileName):
 with open(fileName) as f:
   trek = [] #данные трека

   #Временные буферные переменные
   elev = 0 #Высота
   coord = [] # Координаты точки
   date = ""

   #Началась ли основная информация трека
   iCanRead = False

   #Цикл чтения файла
   for lineF in f:
     #тег trk открывает информацию о треке
    if lineF.find('<trk>') != -1:
      iCanRead = True

    if iCanRead:
      #Широта
      isFind = lineF.find('lat')
      if isFind != -1: #Находим широту
           coordIns=''
           isBreak = False
           for i in range(isFind,len(lineF)):
             if lineF[i].isdigit() or lineF[i]=='.': 
               coordIns += (lineF[i])
               isBreak = True
             else:
               if isBreak:
                 break
           if isBreak:
             coord.append(float(coordIns))
           
      #Долгота
      isFind = lineF.find('lon')
      if isFind != -1: #Находим долготу
           coordIns=''
           isBreak = False
           for i in range(isFind,len(lineF)):
             if lineF[i].isdigit() or lineF[i]=='.': 
               coordIns += (lineF[i])
               isBreak = True
             else:
               if isBreak:
                 break
           if isBreak:
             coord.append(float(coordIns))

      #Высота
      if lineF.find('<ele>')!=-1:
           num=lineF.find("<ele>")
           elevTemp=''
           for i in range(num,len(lineF)):
             if lineF[i].isdigit() or lineF[i]=='.': 
               elevTemp+=lineF[i]

           elev = (float(elevTemp))

      #Дата
      isFind = lineF.find("<time>")
      if isFind != -1:
           timeTemp = ''
           isBreak = False
           for i in range(isFind,lineF.find("</time>")):
             if lineF[i].isdigit() or lineF[i]=='-': 
               timeTemp += lineF[i]
               isBreak = True
             else:
               if isBreak:
                 break
           if isBreak: 
             date = timeTemp

      if lineF.find('/trkpt')!=-1:
        add = [coord,elev,date]
        trek.append(add)
        elev = 0
        coord = []
        date = ""
         
 return trek


