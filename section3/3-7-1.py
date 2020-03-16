import io
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

class NcafeWriteAtt:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        self.driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=r'D:/atom_py/section3/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(5)

    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('516smile')
        self.driver.find_element_by_name('pw').send_keys('12345!')
        self.driver.find_elements_by_xpath('//*[@id="log.login"]').click()
        self.driver.implicitly_wait(5)
