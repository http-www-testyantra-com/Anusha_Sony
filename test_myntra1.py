from selenium import  webdriver
from selenium.webdriver import ActionChains


class Test_myntra1_wishlist():

    def test_verify_productIn_wishlist(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.myntra.com/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        men_element=self.driver.find_element_by_xpath("//a[.='Men']")
        action=ActionChains(self.driver)
        action.move_to_element(men_element).perform()
        self.driver.find_element_by_xpath("//a[.='Sweatshirts']").click()
        self.driver.find_element_by_xpath("//ul[@class='brand-list']/descendant::li[3]").click()
        self.driver.find_element_by_xpath("//a[.='ESS FZ FL Hooded Sweatshirt']").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        #self.driver.find_element_by_xpath("//span[@class='myntraweb-sprite pdp-whiteBag sprites-whiteBag pdp-flex pdp-center']").click()
        self.driver.find_element_by_xpath("//div[.='WISHLIST']").click()
        self.driver.find_element_by_name("email").send_keys("*********mail.com")
        self.driver.find_element_by_name("password").send_keys("********")
        self.driver.find_element_by_xpath("//button[.='Log in']").click()
        self.driver.find_element_by_xpath("//span[.='Wishlist']").click()
        expected_prdt='Puma Men Black Solid ESS FZ FL Hooded Sweatshirt'
        actual_product=self.driver.find_element_by_xpath("//p[.='Puma Men Black Solid ESS FZ FL Hooded Sweatshirt']").text
        print(actual_product)
        assert  expected_prdt==actual_product, print(" Products are not same Assertion failed")
        print(" Both products are same ,assertion passed")
        self.driver.close()

o=Test_myntra1_wishlist()
o.test_verify_productIn_wishlist()





