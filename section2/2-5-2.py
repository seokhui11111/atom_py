from bs4 import BeautifulSoup
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')
# """ 줄바꿈 포함
html="""
<html><body>
    <h1>Find VS Select 차이</h1>
    <p>CSS 선택자를 사용 및 다중반환</p>
    <p>태그선택자 사용 및 단일반환</p>
</body>/</html>
"""
soup=BeautifulSoup(html,'html.parser')
print('soup',soup)
a=soup.prettify()
print(a)

h1=soup.html.body.h1
print('h1',h1)

p1=soup.html.body.p
print('p1',p1)

p2=
