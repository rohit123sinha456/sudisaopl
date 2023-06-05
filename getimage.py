''' In the master run the server that is sending the file
Run the server.js in D:/Rohit/Sudisa/opl/server.js in my laptop then run this
'''
import shutil
import requests
import configparser

class HTTPClient:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.host = config["ADMIN"]["URL"]
        self.port = config["ADMIN"]["PORT"]
        self.endpoint = config["ADMIN"]["API"]
        self.deviceid = config["DEVICE"]["ID"]
        self.api = str('http://'+self.host+':'+self.port+self.endpoint+'/'+self.deviceid)
        print("[x] Preparing to send request to "+self.api)
    
    def getresponse(self):
        #url = 'http://10.12.1.131:3000/file/1'
        #print(url == self.api)
        print("[x] Sending Request to"+self.api)
        self.response = requests.get(self.api,stream=True)
        print("[x] Response Recieved from "+self.api)

    def saveimage(self):
        print("[x] Creating temporary file temp.jpg")
        with open('temp.jpg','wb') as out_file:
            print("[x] Writing HTTP response to temp image")
            shutil.copyfileobj(self.response.raw,out_file)
        del self.response
        print("[x] Clearing response")

if __name__== "__main__":
    client = HTTPClient()
    client.getresponse() # Make this as context manager
    client.saveimage()
