from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class GoogleHomePage():

    def __init__(self, driver):
        self.driver = driver

    def getHomePageItens(self):
        self.SEARCH_INPUT = self.driver.find_element(By.CSS_SELECTOR, 
        "#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")   
   
    def iamOnGoogleSearchPage(self):
        self.driver.get("https://www.google.com.br/")
        time.sleep(3)
        self.getHomePageItens()

    def putTextOnSearchInput(self, text):
        self.SEARCH_INPUT.send_keys(text)

    def pressEnterToSearch(self):
        self.SEARCH_INPUT.send_keys(Keys.RETURN)
        
    def seeResults(self, txtResult):
        assert (txtResult in self.driver.page_source) 
        time.sleep(2)
        self.driver.quit()