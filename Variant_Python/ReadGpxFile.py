#!/usr/bin/python3
# -*- coding: utf-8 -*import

import sys


#Чтение файла gpx  Запись высот в elev_in
def ElevList(fileName, elevIn,x):
  with open(fileName) as f:
    elev=[]
    ind=0;
    for lineF in f:
      lineSTR=lineF.split('trkpt')
      for line in lineSTR:
         #print(len(line))
         if line.find('<ele>')!=-1:
           #print("Вот")
           num=line.find("<ele>")
           #print(num)
           #print(line.find("</ele>"))
           elevTemp=''
           for i in range(num,line.find("</ele>")):
             if line[i].isdigit() or line[i]=='.': 
               elevTemp+=line[i]
           elev.append(float(elevTemp))
           x.append(ind)
           ind+=1
           elevIn.append(float(elevTemp))        
  return elev
