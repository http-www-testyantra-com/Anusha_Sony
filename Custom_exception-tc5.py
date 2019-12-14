from selenium import  webdriver


class Cust_exception(Exception):
    def __init__(self,age=12):
        self.age=age
        if self.age>=18:
         print("Eligible to vote")
        if self.age<=18:
         raise Cust_exception
         print("handled")



