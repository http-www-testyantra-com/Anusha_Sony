from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class Test_myntra3():
    def test_searchproduts(self):
     self.driver=webdriver.Chrome()
     self.driver.get("https://www.myntra.com/")
     self.driver.implicitly_wait(15)
     self.driver.maximize_window()
     self.driver.find_element_by_xpath("//input[@class='desktop-searchBar']").send_keys("shoes", Keys.ENTER)
     pricesort_dpdwn=self.driver.find_element_by_xpath("//span[.='Recommended']")
     action=ActionChains(self.driver)
     action.move_to_element(pricesort_dpdwn).perform()
     self.driver.find_element_by_xpath("//ul[@class='sort-list']/descendant::li[5]").click()
     try:
      assert self.driver.title ,print("Assertion failed")
      print("the page is displayed searched products")
     except Exception as e:
         print("Excetion handled",e)
     finally:self.driver.close()


search=Test_myntra3()
search.test_searchproduts()
