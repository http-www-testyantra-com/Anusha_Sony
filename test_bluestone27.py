from selenium import webdriver

class Test_bluestone27():
 def test_verifyamt_email(self):
  self.driver=webdriver.Chrome()
  self.driver.get("https://www.bluestone.com/")
  self.driver.implicitly_wait(10)
  self.driver.maximize_window()
  self.driver.find_element_by_xpath("//a[.='10+1 Monthly Plan']").click()
  self.driver.find_element_by_id("gmsStart").click()
  amt_expt_msg="Amount is required"
  amt_actl_msg=self.driver.find_element_by_xpath("//li[text()='Amount is required']").text
  assert amt_expt_msg==amt_actl_msg,print("Amount field Assertion failed")
  print("Amount field Assertion passed")
  email_expt_msg="Email is required"
  email_actl_msg=self.driver.find_element_by_xpath("//li[text()='Email is required']").text
  assert  email_expt_msg==email_actl_msg, print("Email field Assertion failed")
  print("Email field Assertion passed")
  self.driver.close()

ob=Test_bluestone27()
ob.test_verifyamt_email()








