import sys
import io
import requests
import json

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

# r=requests.get('https://api.github.com/events')
# r.raise_for_status() #raise : 에러시 장애발생코드 출력
# print(r.text)

jar=requests.cookies.RequestsCookieJar()
# jar.set('name','kim',domain='httpbin.org',path='/cookies')
jar.set('name','kim')

r=requests.get('https://httpbin.org/cookies',cookies=jar)
# print(r.text)

list4=[1,2,['a','b']]
print(list4[2][0])
