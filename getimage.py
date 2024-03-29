''' In the master run the server that is sending the file
Run the server.js in D:/Rohit/Sudisa/opl/server.js in my laptop then run this
'''
import shutil
import requests
import configparser
from requests.exceptions import ConnectionError
import time
from utilities import WORKDIR
class HTTPClient:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(WORKDIR+'config.ini')
        self.host = config["ADMIN"]["URL"]
        self.port = config["ADMIN"]["PORT"]
        self.endpoint = config["ADMIN"]["API"]
        self.deviceid = config["DEVICE"]["ID"]
        self.api = str('http://'+self.host+':'+self.port+self.endpoint+'/'+self.deviceid)
        print("[x] Initiating HTTP Client at "+self.host)
    
    def getresponse(self):
        #url = 'http://10.12.1.131:3000/file/1'
        #print(url == self.api)
        print("[x] Sending Request to"+self.api)
        while(True):
            try:
                self.response = requests.get(self.api,stream=True)
                #print(self.response.headers["content-type"].split("/")[1])
                break
            except ConnectionError:
                print("[x] Can't reach HTTP Server")
                time.sleep(5)
                print("[x] Retrying after 5 seconds")
        print("[x] Response Recieved from "+self.api)

    def saveimage(self):
        print("[x] Creating temporary file temp.png")
        fileext = self.response.headers["content-type"].split("/")[1]
        filename = "temp."+fileext
        print(filename)
        with open(filename,'wb') as out_file:
            print("[x] Writing HTTP response to temp image")
            self.response.raw.decode_content = True
            shutil.copyfileobj(self.response.raw,out_file)
        del self.response
        print("[x] Clearing response")
        return filename

if __name__== "__main__":
    client = HTTPClient()
    client.getresponse() # Make this as context manager
    client.saveimage()
