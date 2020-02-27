import io
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

driver=webdriver.Chrome('D:/atom_py/section3/webdriver/chrome/chromedriver')

driver.set_window_size(1920,1080)
driver.implicitly_wait(5)
driver.get('https://www.wishket.com/accounts/login/')
time.sleep(5)
driver.implicitly_wait(3)
driver.find_element_by_name('identification').send_keys('smile516')
driver.implicitly_wait(3)
driver.find_element_by_name('password').send_keys('three1126@')
driver.implicitly_wait(3)
#로그인
driver.find_element_by_xpath('//*[@id="submit"]').click()




print("스크린샷 완료")
