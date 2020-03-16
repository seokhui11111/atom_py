import urllib.request as req
import os.path, random
import simplejson as json

#url
url='https://api.github.com/repositories'

#경로 & 파일명
saveName='D:/atom_py/section4/repo.json'

if not os.path.exists(url):
    req.urlretrieve(url,saveName)

items=json.loads(open(saveName,"r",encoding="utf-8").read())

for item in items:
    print(item["full_name"]+" - "+item["owner"]["url"])
