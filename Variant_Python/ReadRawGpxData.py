
# -*- coding: utf-8 -*import

import sys
import RawGPXData

#Чтение файла gpx  Запись высот, координат, даты
#Возвращает лист trek
def RawDataFind(fileName):
 with open(fileName) as f:
   trek = [] #данные трека

   #Временные буферные переменные
   elev = 0 #Высота
   coord = [] # Координаты точки
   date = ""
   rawData = RawGPXData.RawGPX()

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
            rawData.latitude.ReadFromGPX(isFind, lineF)
           
      #Долгота
      isFind = lineF.find('lon')
      if isFind != -1: #Находим долготу
            rawData.longitude.ReadFromGPX(isFind, lineF)

      #Высота
      num=lineF.find("<ele>")
      if num!=-1:
            rawData.elev.ReadFromGPX(num, lineF)

      #Дата
      isFind = lineF.find("<time>")
      if isFind != -1:
            rawData.dateData.ReadFromGPX(isFind, lineF)

      if lineF.find('/trkpt') != -1:
        date = rawData.dateData.value
        elev = rawData.elev.value
        coord.append(rawData.latitude.value)
        coord.append(rawData.longitude.value)
        add = [coord,elev,date]
        trek.append(add)
        elev = 0
        coord = []
        date = ""
         
 return trek


