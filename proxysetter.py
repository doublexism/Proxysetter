import json
import os
import proxygetter as pg
import sys

path = os.path.expanduser('~')

#getting system variables
if sys.argv[1] == 'a':
    ip, port,speed,location=pg.autoChooseFast()
elif sys.argv[1] == 'l':
    try:
        ip, port,speed,location=pg.chooseFromLocation(sys.argv[2])
    except IndexError as e:
        print("Please specify a location: e.g. $ proxysetter l 北京 ")
else:
    print("Invalid keywords. Use '$ proxysetter a' for autoselect or \n '$ proxysetter l [location]' for location setting")
    ip, port,speed,location=pg.autoChooseFast()
    
#show informations
print("{}:{},{},{}".format(ip, port, speed, location))

with open(path + '/.netease-musicbox/config.json', 'r+') as f:
    data = json.load(f)
    data['mpg123_parameters']['value'][1] = ''.join(('http://',ip,':',port))   
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
