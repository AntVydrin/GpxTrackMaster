
# -*- coding: utf-8 -*import

import sys
import RawGPXData #функционал поиска и хранения сырых данных из трека

#Чтение файла gpx  Запись высот, координат, даты
#Возвращает данные трека (trek)
def RawDataFind(fileName):
 with open(fileName) as f:
   trek = [] #данные трека

   #Временные буферные переменные
   elev = 0 #Высота
   coord = {"lat": 0.0, "lon": 0.0} # Координаты точки
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
        coord["lat"] = rawData.latitude.value
        coord["lon"] = rawData.longitude.value
        add = {"coord": coord.copy(), "elev": elev,"date": date}

        #Данные текущей точки записываем
        trek.append(add)

        #"обнуляем" временные переменные
        elev = 0
        date = ""
         
 return trek


