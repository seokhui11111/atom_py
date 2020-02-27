from bs4 import BeautifulSoup
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

html="""
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://tistory.com">tistory</a></li>
    </ul>
</body><html>
"""
soup=BeautifulSoup(html,'html.parser')
# print('soup : ',type(soup))
links=soup.find_all("a")
# print('links : ',type(links))
a=soup.find_all("a",string="daum")
print('a : ',a)
b=soup.find("a")
print('b : ',b)
