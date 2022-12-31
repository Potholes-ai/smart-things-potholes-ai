#import libraries
# import gps
# import detection
import requests


# Global Variables
server_link = 'http://localhost:3000/addPosPothole'
server_data = {"latitude":10.0, "longitude":10, "image":""}

def start():  
    resp = requests.post(server_link, json = server_data)
    print(resp)
start()
    