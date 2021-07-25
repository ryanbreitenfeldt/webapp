
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
        return self.urlbase.insert(self.appID,input)

    def makeRequest(self,input):
        self.responce = requests.get(input)
