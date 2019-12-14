from selenium import  webdriver

class Amazon:

 driver=webdriver.Chrome("C:\\Users\\kameswararaop\\AppData\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
 driver.implicitly_wait(10)
 driver.get("https://www.Amazon.com/")
 driver.maximize_window()
 try:
  driver.find_element_by_xpath("(//input[@type='submit'])[2]").click()
 except Exception as e:
  print(e,"Exception handled")
 driver.find_element_by_xpath("//a[.='Help']").click()







