# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class PapagoApi:
    def __init__(self):
        self.base_url = 'https://papago.naver.com/?sk=en&tk=ko&hn=1'
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument('headless') # 화면 출력 없이 작업
        options.add_argument('ignore-certificate-errors') # 인증서 관련 에러 무시
        options.add_argument("ignore-ssl-errors")
        options.add_argument('window-size=1920x1080') # 브라우저 윈도우 사이즈
        options.add_argument("disable-gpu")

        self.driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        self.driver.implicitly_wait(5)

        self.driver.get(self.base_url)

    def get_trans(self, text):
        if text == 'exit':
            return self.driver.quit()
        self.driver.find_element(By.XPATH, '//*[@id="txtSource"]').click()
        self.driver.find_element(By.ID, "txtSource").clear()
        self.driver.find_element(By.ID, "txtSource").send_keys(text)
        time.sleep(2)
        data = self.driver.find_element(By.XPATH, '//*[@id="txtTarget"]/span').text
        self.driver.find_element(By.XPATH, '//*[@id="txtSource"]').click()
        self.driver.find_element(By.ID, "txtSource").clear()

        if data:
            print(data)
            return PapagoApi.get_trans(self, input())
        else:
            return ''

