import socket
import requests
from bs4 import BeautifulSoup

URL = "https://api.ipify.org"
PRIVATE_IP_ADDR = ""
PUBLIC_IP_ADDR = ""
LOCATION = ""

#Check private IP using socket connect to "DNS", "PORT"
def privateIP():
    value = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 53))
    value = s.getsockname()[0]
    s.close()
    return value

#GO TO https://api.ipify.org check public IP and using BeautifulSoup for parsing
def PUBLIC_IP():
    req = requests.get(URL)
    html = BeautifulSoup(req.content, "html.parser")
    return html
    

print("Public IP", PUBLIC_IP_ADDR.join(PUBLIC_IP()))
print("Private IP: ", PRIVATE_IP_ADDR.join(privateIP()))