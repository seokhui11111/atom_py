from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

url="https://finance.naver.com/sise/"
res=req.urlopen(url).read().decode('cp949')
# print(res)
soup=BeautifulSoup(res,"html.parser")

hot=soup.select("ul#popularItemList>li>a")
print(hot)

for i,e in enumerate(hot,1):
    print('순위 : {}, 이름 : {}'.format(i,e.string) )
