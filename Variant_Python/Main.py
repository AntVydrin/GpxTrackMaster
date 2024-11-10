#!/usr/bin/python3
# -*- coding: utf-8 -*import

import ReadRawGpxData as readGPX
import ProcessingOfRawData as PRWD

def main():
    FileName = 'testFiles/Трек_Памир_2.gpx'#Трек_Памир_2#trek_small
    RawData = readGPX.RawDataFind(FileName)
    n = min(5,len(RawData))
    for i in range(0,n):
        print(RawData[i])
    #dist = Distance.Dist(theElev[0][0][0],theElev[0][0][1],theElev[2][0][0],theElev[2][0][1])
    #print(dist)

    #ProcessedData =

    #CreatePlot(ProcessedData)
    

if __name__ == '__main__':
    main()
