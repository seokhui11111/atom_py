import io
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

driver = webdriver.Chrome('D:/atom_py/section3/webdriver/chrome/chromedriver')

driver.set_window_size(1920,1080)
driver.implicitly_wait(5)
driver.get('http://www.encar.com/dc/dc_carsearchlist.do?carType=kor#!%7B%22action%22%3A%22(And.Hidden.N._.(C.CarType.Y._.Manufacturer.%ED%98%84%EB%8C%80.))%22%7D')
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="sr_photo"]/li[1]/a/span[1]/span[1]/span').click()
