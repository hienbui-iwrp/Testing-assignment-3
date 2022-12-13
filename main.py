from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


from boundary import *
from equivalentClass import *
from decisionTable import *
from usecase1 import *
from usecase2 import *


# setup
service = ChromeService(executable_path='./chromedriver.exe')
# driver = webdriver.Chrome(service=service)
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, chrome_options=options)


boundary = Boundary(driver)
equivalentClass = EquivalentClass(driver)
decisionTable = DecisionTable(driver)
usecase1 = Usecase1(driver)
usecase2 = Usecase2(driver)

driver.get("http://localhost/")

# run
boundary.run_all_test()
equivalentClass.run_all_test()
decisionTable.run_all_test()
usecase1.run_all_test()
usecase2.run_all_test()

driver.quit()
