from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename="D:/atom_py/section4/forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url,savename)

#BeautifulSoup 로 분석
xml=open(savename,'r',encoding='utf-8').read()
soup=BeautifulSoup(xml,"html.parser")
# print(soup)
info={}
for location in soup.find_all("location"):
    loc=location.find("city").string
    # print(loc)
    weather=location.find_all("tmn")
    # print(weather)
    if not (loc in info):
        info[loc]=[] #keys
    for tmn in weather:
        info[loc].append(tmn.string) #values (2,7)
# print(info)
# print(list(info.keys()))
# print(info.values())

with open("D:/atom_py/section4/Fcast.txt","wt",encoding='utf-8') as f:
    for loc in sorted(info.keys()):
        print("지역 : ",loc) #consol
        f.wrtie(str(loc)+'\n') #file
        for num in info[loc]:
            print("기옵 : ",num)
            f.write('\t'+str(num)+'\n')
