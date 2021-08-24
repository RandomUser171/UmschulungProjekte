import json
import urllib3
from class_latest_fact import *

print(Latest_fact())
end_chars = '.!'
urlreq = urllib3.PoolManager()
header = {'User-agent': 'Checking for the latest fact'}
url = 'https://www.reddit.com/r/todayilearned/new.json'
req = urlreq.request('GET', url, headers=header)
til_data = json.loads(req.data.decode('utf-8'))
file = open('21. TIL facts.txt', 'r')
file2 = open('21. TIL facts.txt', 'a')
ouga = [x.strip() for x in file.readlines()]
ouga2 = til_data['data']['children'][0]['data']['title']


if 'TIL that' in ouga2:
    ouga2 = ouga2[9].upper()+ouga2[10:]
elif 'TIL: ' in ouga2:
    ouga2[-1] = ouga2[5].upper() + ouga2[6:]
elif 'TIL ' in ouga2:
    ouga2 = ouga2[4].upper() + ouga2[5:]
if ouga2[-1] in end_chars:
    ouga2 = ouga2[:-1] + '!'
else:
    ouga2 = ouga2 + '!'
try:
    if ouga[-1] == ouga2:
        print('fact already there')
    else:
        file2.write(ouga2+'\n')
except IndexError:
    print('file empty')
    file2.write(ouga2+ '\n')
file.close()
file2.close()


