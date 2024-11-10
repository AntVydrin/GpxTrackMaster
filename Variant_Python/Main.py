#!/usr/bin/python3
# -*- coding: utf-8 -*import

import ReadRawGpxData as readGPX
import ProcessingOfRawData as PRWD
import CreatePlot as crP
import sys


def main(fileName):
    
    rawData = readGPX.RawDataFind(fileName)
    """
    n = min(5,len(rawData))
    for i in range(0,n):
        print(rawData[i])
    """
    ProcessedData = PRWD.TrekDataList(rawData)
    
    crP.CreatePlot(ProcessedData)

if __name__ == '__main__':
    if len (sys.argv) > 1:
       fileName = sys.argv[1]
    else:
       print("Не введён путь к файлу трека!!!")
       fileName = 'testFiles/Трек_Памир2021.gpx'#Трек_Памир_2#trek_small  Трек_Памир2021

    main(fileName)
