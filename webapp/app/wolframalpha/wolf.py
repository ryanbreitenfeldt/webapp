
import requests
from appid import appID

class wolframAlpha():
    def __init__(self):
        self.appID = appID
        self.urlbase = "http://api.wolframalpha.com/v1/simple?appid={}&i={}"
        self.responce = None
    
    
    def stringConverter(self,input):
        input = input.replace(" ","+")
        input = input.replace("?", "%3F")
        return input

    def questionAssembler(self,input):
        return self.urlbase.format(self.appID,input)

    def makeRequest(self,input):
        self.responce = requests.get(input)

    def dumpToFile(self):
        tempFile = open("temp.gif","wb")
        tempFile.write(self.responce.content)

    def doItAll(self,input):
        self.makeRequest(self.questionAssembler(self.stringConverter(input)))
        self.dumpToFile()
