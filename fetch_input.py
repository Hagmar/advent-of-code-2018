import sys
import requests as rq
import urllib3


url = 'https://adventofcode.com/2018/day/{}/input'
day = sys.argv[1]

urllib3.disable_warnings()
ses = rq.Session()
ses.cookies.set('session', 'XXXXXXXXXXXXXXXX')
res = ses.get(url.format(day), verify=False)

with open('in_{}'.format(day), 'w') as f:
    f.write(res.text)
