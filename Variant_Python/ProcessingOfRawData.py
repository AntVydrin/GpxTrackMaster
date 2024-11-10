import Distance
import RawGPXData

def FindDistance(rawData):
    rd = RawGPXData.RawGPX() #список точек трека
    rd = rawData
    for i in range(0, len(rd)):
        print(rd[i]["elev"])
    print(rd[0]["coord"]["lon"])
    
