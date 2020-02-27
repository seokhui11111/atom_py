from bs4 import BeautifulSoup
import sys
import io
import requests
from fake_useragent import UserAgent

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

#요청
URL='https://www.wishket.com/accounts/login/'

with requests.Session() as s:
    #URL요청
    s.get(URL)

    #fake_useragent
    ua=UserAgent()


    #Login 정보 Payload
    Login_info={
        'identification':'smile516',
        'password':'three1126@',
        'csrfmiddlewaretoken':s.cookies['csrftoken']
    }
    # print('token',s.cookies['csrftoken'])

#요청
response=s.post(URL,data=Login_info,headers={'User-Agent':str(ua.chrome),'Referer':'https://www.wishket.com/mywishket/client/'})
#html 결과 확인
# print('response',response.text)
if response.status_code==200 and response.ok:
    soup=BeautifulSoup(response.text,'html.parser')
    project=soup.select("div.contract>div")
    print(project)
    for i in project:
        print(i.text)
