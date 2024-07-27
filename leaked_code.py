import pandas as pd
import math
# Reaading the files
careAreas = pd.read_csv("Z:\\KLA Tencor\\2nd\\CareAreas.csv" , header=None)
metaData = pd.read_csv("Z:\\KLA Tencor\\2nd\\metadata.csv" )

#Renaming the colulmns
careAreas.columns = ['Id','Xmin','Xmax','Ymin','Ymax']
metaData.columns = ["MainFieldSize","SubFieldSize"]

class CareArea:
    def __init__(self,xmin,xmax,ymin,ymax,cid):
        self.id = cid
        self.xmin = round(xmin,6)
        self.xmax = round(xmax,6)
        self.ymin = round(ymin,6)
        self.ymax = round(ymax,6)
        self.size = round(xmax-xmin,6)    
    def bottomLeft(self):
        return (self.xmin,self.ymin)
    def bottomRight(self):
        return (self.xmax,self.ymin)
    def topLeft(self):
        return (self.xmin,self.ymax)
    def topRight(self):
        return (self.xmax,self.ymax)
    def __str__(self):
        return "BottomLeft: ("+str(self.xmin)+" , "+str(self.ymin)+")\nTopRight: ("+str(self.xmax)+" , "+str(self.ymax)+")"
    def getAsList(self):
        return [self.id, self.xmin, self.xmax, self.ymin, self.ymax]
        
class MainField:
    size = round(float(metaData['MainFieldSize']),6)
    def __init__(self,xmin,ymin,mid):
        self.id = mid
        self.xmin = round(xmin,6)
        self.ymin = round(ymin,6)
        self.xmax = xmin+self.size
        self.ymax = ymin+self.size
    def bottomLeft(self):
        return (self.xmin,self.ymin)
    def bottomRight(self):
        return (self.xmax,self.ymin)
    def topLeft(self):
        return (self.xmin,self.ymax)
    def topRight(self):
        return (self.xmax,self.ymax)
    def getAsList(self):
        return [self.id, self.xmin, self.xmax, self.ymin, self.ymax]
    def __str__(self):
        return "BottomLeft: ("+str(self.xmin)+" , "+str(self.ymin)+")\nTopRight: ("+str(self.xmax)+" , "+str(self.ymax)+")"
        
class SubField:
    size = round(float(metaData['SubFieldSize']),6)
    def __init__(self,xmin,ymin,cid,mid=-1):
        self.careAreaId = cid
        self.xmin = round(xmin,6)
        self.ymin = round(ymin,6)
        self.xmax = xmin+self.size
        self.ymax = ymin+self.size
        self.mid = mid
    def bottomLeft(self):
        return (self.xmin,self.ymin)
    def bottomRight(self):
        return (self.xmax,self.ymin)
    def topLeft(self):
        return (self.xmin,self.ymax)
    def topRight(self):
        return (self.xmax,self.ymax)
   
    def __str__(self):
        return "BottomLeft: ("+str(self.xmin)+" , "+str(self.ymin)+")\nTopRight: ("+str(self.xmax)+" , "+str(self.ymax)+")"
    
    def setMainFieldId(self,mid):
        self.MainFieldId = mid
    def setId(self,i):
        self.id = i
    def getAsList(self):
        return [self.id, self.xmin, self.xmax, self.ymin, self.ymax, self.MainFieldId]

def isContinuous(field1,field2):
    if field1.xmax >= field2.xmin:
        return True

def getMainField(subField,mainFieldList):
    for mainField in mainFieldList:
        if subField.xmin <= mainField.xmax and subField.xmin >= mainField.xmin and subField.xmax <= mainField.xmax and subField.xmax >= mainField.xmin and subField.ymin <= mainField.ymax and subField.ymin >= mainField.ymin and subField.ymax <= mainField.ymax and subField.ymax >= mainField.ymin :
            return mainField.id
    return -1

def isIn(coord,area):
    if coord[0] < area.xmax and coord[0] > area.xmin and coord[1]<area.ymax and coord[1] > area.ymin :
        return True
    else:
        return False

def isCaring(subField, careArea):
    if isIn(subField.bottomLeft(),careArea):
        return True
    elif isIn(subField.bottomRight(),careArea) :
        return True
    elif isIn(subField.topLeft(),careArea) :
        return True
    elif isIn(subField.topRight()(),careArea):
        return True
    else:
        return False

def getUncoveredSubField(subFieldList,mainFieldList):
    uncovered = []
    for i in subFieldList:
        flag = getMainField(i,mainFieldList)
        if flag==-1:
            uncovered.append(i)
        else:
            i.setMainFieldId(flag)
    return uncovered
            
def fillCareArea(careArea,listLen):
    offset = SubField.size
    subFieldList = []
    n = math.ceil(careArea.size/float(SubField.size))
    for i in range(n):
        for j in range(n):
            temp = SubField(careArea.xmin+j*offset,careArea.ymin+i*offset,careArea.id)
            temp.setId(listLen+i*n+j)
            subFieldList.append(temp)
    return subFieldList

def getHeadSubField(uncovered):
    return min(uncovered,key= lambda x: x.xmin+x.ymin)

def createMainField(subField,mainFieldListLength):
    return MainField(subField.xmin, subField.ymin, mainFieldListLength)
        
careAreaList = []
subFieldList = []
mainFieldList = []

for i in range(len(careAreas)):
    careAreaList.append(CareArea(float(careAreas['Xmin'][i]),float(careAreas['Xmax'][i]),float(careAreas['Ymin'][i]),float(careAreas['Ymax'][i]),i) )   

for i in careAreaList:
    subFieldList.extend(fillCareArea(i,len(subFieldList)))

uncovered = subFieldList

while True:
    uncovered = getUncoveredSubField(uncovered,mainFieldList)
    if len(uncovered)==0:
        break
    tempHead = getHeadSubField(uncovered)
    temp = createMainField(tempHead,len(mainFieldList))
    mainFieldList.append(temp)

writeMainFieldList = list(map(lambda x: x.getAsList(),mainFieldList))
writeSubFieldList = list(map(lambda x: x.getAsList(),subFieldList))

mainFields = pd.DataFrame(writeMainFieldList , columns= ['ID','Xmin','Xmax','Ymin','Ymax'] )
subFields = pd.DataFrame(writeSubFieldList , columns= ['ID','Xmin','Xmax','Ymin','Ymax','Main Field ID'] )

mainFields.to_csv("Z:\\KLA Tencor\\2nd\\MainField_alpha1.csv", index = False , header= None)
subFields.to_csv("Z:\\KLA Tencor\\2nd\\SubField_alpha1.csv",  index = False, header = None)