from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\kameswararaop\\AppData\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.Myntra.com/")
driver.maximize_window()
action=ActionChains(driver)
kids_ele=driver.find_element_by_xpath("//a[.='Kids']")
action.move_to_element(kids_ele).perform()
driver.find_element_by_xpath("//a[.='Home & Bath']").click()
try:
    driver.find_element_by_xpath("//input[@type='radio']").click()
except Exception as e:
 print(e,"Elementnotfound exception handled")
finally:
   driver.find_element_by_xpath("//div[@class='product-sliderContainer']").click()



