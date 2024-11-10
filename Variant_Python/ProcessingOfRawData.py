import Distance
import RawGPXData



def FindDistance(rawData):
    trekData = RawGPXData.RawGPX() #список точек трека
    trekData = rawData
    returnLength = []
    n = len(trekData)
    for i in range(1, n):
        returnLength.append(Distance.Dist(trekData[i-1]["coord"]["lat"], trekData[i-1]["coord"]["lon"], trekData[i]["coord"]["lat"], trekData[i]["coord"]["lon"]))
    return returnLength

def TrekDataList(rawData):
    trekData = RawGPXData.RawGPX() #список точек трека
    trekData = rawData
    dist = []
    dist = FindDistance(rawData)
    processedData = []
    processedData.append({"elev": trekData[0]["elev"], "Length": 0, "date": trekData[0]["date"]})
    n = len(trekData)
    distSum = 0
    for i in range(1, n):
        distSum += dist[i-1]
        processedData.append({"elev": trekData[i]["elev"], "Length": distSum, "date": trekData[i]["date"]})
    return processedData
