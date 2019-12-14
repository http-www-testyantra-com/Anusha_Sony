from selenium import webdriver
from selenium.webdriver import ActionChains

class Test_blueStoneTop():

 def test_check_topicon(self):
  self.driver=webdriver.Chrome()
  self.driver.get("https://www.bluestone.com/")
  self.driver.maximize_window()
  self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
  action=ActionChains(self.driver)
  top_icon_elmt=self.driver.find_element_by_xpath("//li[@class='menuparent repb']/a[@title='Rings']")
  action.move_to_element(top_icon_elmt).perform()
  assert top_icon_elmt.is_displayed(), print("Assertion failed")
  print("Top icon Assertion  is passed")
  self.driver.close()

obj=Test_blueStoneTop()
obj.test_check_topicon()



