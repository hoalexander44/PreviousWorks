
#Class is created here
class Socialite():
#The Constructor
    def __init__(self):
        self.__Last_Name = ""
        self.__First_Name = ""
        self.__Picture = ""
        self.__Website = ""
        self.__Description = ""
        self.__UserID = ""
#method that returns a string representation of object
    def str(self):
        a= "Name: "+self.__First_Name+self.__Last_Name+"\nUserID: "+ self.__UserID+"\nPicture: "+self.__Picture+"\nWebsite: "+self.__Website+"\nWebsite Description: "+ self.__Description
        return a
#All the mutator methods below
    def setLastName(self,l):
        self.__Last_Name = l
    def setFirstName(self,f):
        self.__First_Name = f
    def setPicture(self,p):
        self.__Picture = p
    def setWebsite(self,w):
        self.__Website = w
    def setDescription(self,d):
        self.__Description = d
    def setUserID(self,u):
        self.__UserID = u
#all the Accessor Methods below
    def getLastName(self):
        return self.__Last_Name
    def getFirstName(self):
        return self.__First_Name
    def getPicture(self):
        return self.__Picture
    def getWebsite(self):
        return self.__Website
    def getDescription(self):
        return self.__Description
    def UserID(self):
        return self.__UserID
#quick test to see if the class works, will only run if file is main file
if __name__ == "__main__":
    a = Socialite()
    a.setLastName("Drexel")
    a.setFirstName("Anothony")
    a.setPicture(" http : / /www. c s . d r e x el . edu /˜mcs172 /Sp09 / images / a jd . png")
    a.setDescription("St . K a th a rine Drexel ’ s w e b si t e")
    a.setWebsite("h t tp : / /www. k a t h a r i n e d r e x e l . o r g / ")
    a.setUserID("TonyD")
    print(a.str())