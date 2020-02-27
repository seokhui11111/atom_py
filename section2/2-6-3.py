from bs4 import BeautifulSoup
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

fp=open("d:/atom_py/section2/cars.html",encoding="utf-8")
soup=BeautifulSoup(fp,"html.parser")

def car_func(selector):
    print("car_func ",soup.select_one(selector).string)

car_func("#gr")
