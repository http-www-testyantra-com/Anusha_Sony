from selenium import webdriver

class Recipes:
    driver = webdriver.Chrome(executable_path="C:\\Users\\kameswararaop\\AppData\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.allrecipes.com/recipes/")
    driver.maximize_window()
    try:
        driver.find_element_by_id('bx-close-inside-1066816').click()
    except Exception as NoSuchWindow:
        print("handled")
    finally:

     driver.find_element_by_xpath("//div[@class='hamburger-nav']").click()


