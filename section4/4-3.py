from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1135059500"
savename="D:/atom_py/section4/forecast2.xml"
if not os.path.exists(savename):
    req.urlretrieve(url,savename)

#BeautifulSoup 로 분석
xml=open(savename,'r',encoding='utf-8').read()
soup=BeautifulSoup(xml,"html.parser")
# print(soup)
info={}
for data in soup.find_all("data"):
    dat=data.find("hour").string
    # print(dat)
    weather=data.find("temp").string
    # print(weather)
    print("시간 : {}, 기온 : {}".format(dat,weather))
    # if not (dat in info):
    #     info[dat]=[] #keys
    # for temp in weather:
    #     info[dat].append(temp.string) #values (2,7)
# print(info)
# print(list(info.keys()))
# print(info.values())

with open("D:/atom_py/section4/Fcast2.txt","wt",encoding='utf-8') as f:
    for dat in sorted(info.keys()):
        print("시간 : ",dat) #consol
        f.write(str(dat)+'\n') #file
        for num in info[dat]:
            print("기온 : ",num)
            f.write('\t'+str(num)+'\n')
