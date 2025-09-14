class Human:
    
    def __init__(self,name,lastName,age):
        self.__name = name
        self.__lastName = lastName
        self.__age = age

    def getName(self):
        return self.__name
    def getLastName(self):
        return self.__lastName
    def getAge(self):
        return self.__age
    
    def setName(self,name):
        self.__name = name
    def setName(self,lastName):
        self.__lastName = lastName
    def setName(self,age):
        self.__age = age

    def csv2obj(csv,objList):
        humans = []
        names = csv(csv,"name")
        lastNames = csv(csv,"lastName")
        ages = csv(csv,"age")
        for n,l,a in names,lastNames,ages:
            humans.append(new Human(n,l,a))
        return humans

def csv(csv= "",factor=""):
    sep = ","
    csv += sep
    findex = csv.find(factor)
    sepIndex = csv.find(sep)
    list =[]
    while(findex >= 0 and sepIndex >= 0):
        list.append(csv[findex + len(factor) + 1:sepIndex])
        findex = csv.find(factor,sepIndex)
        sepIndex = csv.find(sep,findex)
    return list

print(csv("name:ali,family:sajjadi,name:ghasem,family:mohamadi","name"))

