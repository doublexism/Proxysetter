import requests
import re
from bs4 import BeautifulSoup

def getProxyServer():
    proxyPage = BeautifulSoup(requests.get("http://cn-proxy.com/").text, 'lxml')
    Tables = proxyPage("table")
    ServerDict = {'ip':[], 'port':[], 'location':[], 'speed':[], 'date':[]}     
    for table in Tables:
        proxyEntry = table("tr")[2:]
        for server in proxyEntry:
            dataElements = server('td')
            ip = dataElements[0].text
            port = dataElements[1].text
            location = dataElements[2].text
            speed = dataElements[3].div.strong['style']
            speed = re.findall(r'\d+\%', speed)[0]
            date = dataElements[4].text
            ServerDict['ip'].append(ip)
            ServerDict['port'].append(port)
            ServerDict['location'].append(location)
            ServerDict['speed'].append(speed)
            ServerDict['date'].append(date)
    return ServerDict

def autoChooseFast():
    ServerDict = getProxyServer()
    speeds = ServerDict['speed']
    n = speeds.index(max(speeds))
    return ServerDict['ip'][n],ServerDict['port'][n],ServerDict['speed'][n],ServerDict['location'][n]

def chooseFromLocation(loc):
    ServerDict = getProxyServer()
    locations = ServerDict['location']
    print(locations)
    candidate = [i+1 for i in range(len(locations)) if loc in locations[i]]
    print(candidate)
    try:
        first = candidate[0] 
    except IndexError as e:
        print("Locations not found, please change your search term!")
    else:
        speeds = [ServerDict['speed'][i-1] for i in candidate]
        n = candidate[speeds.index(max(speeds))]
        return ServerDict['ip'][n-1],ServerDict['port'][n-1],ServerDict['speed'][n-1],ServerDict['location'][n-1]
    
        
    


