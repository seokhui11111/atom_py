from urllib.parse import urljoin

baseURL="http://test.com/com/html/a.html"
print(urljoin(baseURL,"b.html"))
print(urljoin(baseURL,"sub/c.html"))
print(urljoin(baseURL,"../index.html"))
print(urljoin(baseURL,"../img/hong.png"))
