
class ReadDataStruct:
    def __init__(self, value):
        self.value = value
        self.isRead = False
    def ReadFromGPX(self, num, lineF):
        valueString = ''
        isBreak = False
        for i in range(num,len(lineF)):
           if lineF[i].isdigit() or lineF[i]=='.': 
             valueString += (lineF[i])
             isBreak = True
           else:
             if isBreak:
               break
        if isBreak:
            self.value = (float(valueString))
        #self.isBreak = isBreak
        #return self.isBreak

class ReadDate(ReadDataStruct):
    def ReadFromGPX(self, num, lineF):
        valueString = ''
        isBreak = False
        for i in range(num,len(lineF)):
           if lineF[i].isdigit() or lineF[i]=='-': 
             valueString += (lineF[i])
             isBreak = True
           else:
             if isBreak:
               break
        if isBreak:
            self.value = valueString
        #self.isBreak = isBreak
        #return isBreak

class RawGPX:
    def __init__(self):
        self.latitude = ReadDataStruct(0.0)
        self.longitude = ReadDataStruct(0.0)
        self.elev = ReadDataStruct(0.0)
        self.dateData = ReadDate("2000-01-01")

#readDataStruct = ReadDataStruct()

#print(readDataStruct.ReadFromGPX(3, "hj 2.5 k"))


#rawData = RawGPX()
#if rawData.elev.ReadFromGPX(3, "hj 2.05645685 9.254 k"):
    #print(rawData.elev.valueString)

#if (rawData.dateData.ReadFromGPX(0, "2021-07-24T12:20:55Z")):
  #   print(rawData.dateData.valueString)


