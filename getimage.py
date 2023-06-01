''' In the master run the server that is sending the file
Run the server.js in D:/Rohit/Sudisa/opl/server.js in my laptop then run this
'''
import shutil
import requests

url = 'http://10.12.1.131:3000/file/bubu.jpg'
response = requests.get(url,stream=True)
with open('bubu.jpg','wb') as out_file:
    shutil.copyfileobj(response.raw,out_file)
del response
