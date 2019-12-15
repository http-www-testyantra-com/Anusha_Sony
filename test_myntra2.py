from selenium import webdriver
from selenium.webdriver import ActionChains


class Test_myntra2():
    def test_verify_allprds(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.myntra.com/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        discover_element = self.driver.find_element_by_xpath("//a[.='Discover']")
        action = ActionChains(self.driver)
        action.move_to_element(discover_element).perform()
        self.driver.find_element_by_xpath("//a[.='Forever21']").click()
        self.driver.find_element_by_xpath("//ul[@class='discount-list']/descendant::li[3]").click()
        product=self.driver.find_elements_by_xpath("//li[@class='product-base']")
        assert ( len(product)) , print("Assertion failed to find the count of products")
        print("All products are available")
        self.driver.close()

cntofprdts=Test_myntra2()
cntofprdts.test_verify_allprds()
