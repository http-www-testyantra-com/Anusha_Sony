from selenium import webdriver
from selenium.webdriver import ActionChains


class FlipKart():

 driver=webdriver.Chrome("C:\\Users\\kameswararaop\\AppData\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
 driver.implicitly_wait(10)
 driver.get("https://www.flipkart.com/")
 driver.maximize_window()

 try:
  driver.find_element_by_xpath("//button[.='✕']").click()
 except Exception as e:
     print("Exception handled")

 a = ActionChains(driver)
 we = driver.find_element_by_xpath("//ul[@class='_114Zhd']/li[4]")
 a.move_to_element(we).perform()
 ethnicEle = driver.find_element_by_xpath("(//a[@title='Ethnic Wear'])[1]").click()
 slider = driver.find_element_by_xpath("//div[@class='_3G9WVX _2N3EuE']")
 act = ActionChains(driver)
 act.drag_and_drop_by_offset(slider, -50, 0).perform()

