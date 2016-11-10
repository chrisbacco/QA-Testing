#python w/ selenium webdriver test for .edu login page
#setUp/test_log_in/tearDown



import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

#Testing environment: Chrome or Firefox 

    def setUp(self):
       	#self.driver = webdriver.Chrome()	
	 self.driver = webdriver.Firefox()

#test case: edit for email address and password
#send keys 
#don't forget to close


    def test_log_in(self):
        driver = self.driver
        driver.get("https://webmail.towson.edu/")
        elem = driver.find_element_by_name('Username')
        elem.send_keys("email@email.com")
        elem.send_keys(Keys.RETURN)
        elem2 = driver.find_element_by_name('password')
        elem2.send_keys("p4ssw0rd")
        elem2.send_keys(Keys.RETURN)
        assert driver.find_element_by_xpath('/html/body/script[4]')

        def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    unittest.main()
