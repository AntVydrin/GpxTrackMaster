#!/usr/bin/python3
# -*- coding: utf-8 -*import

import ReadGpxFile1 as readGPX
import Distance

FileName = 'testFiles/trek_small.gpx'#Трек_Памир_2

theElev = readGPX.ElevList(FileName)

n = min(5,len(theElev))
for i in range(0,n):
    print(theElev[i])

dist = Distance.Dist(theElev[0][0][0],theElev[0][0][1],theElev[2][0][0],theElev[2][0][1])
print(dist)
