from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from data import *
from testcase import *


class EquivalentClass(TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def run_all_test(self):
        print('--------------------------------')
        print('Run Equivalent Class Test:')

        self.setup_data()
        # run test
        self.test_1()
        self.test_2()
        self.test_3()
        self.test_4()
        self.test_5()
        self.test_6()
        self.test_7()

        self.logout()
        print('--------------------------------')

    def test_1(self):
        try:
            self.run_test(current=EQUIVALENT_CLASS_TESTCASE['test 1']['current'],
                          new_password=EQUIVALENT_CLASS_TESTCASE['test 1']['new password'],
                          confirm=EQUIVALENT_CLASS_TESTCASE['test 1']['confirm'])
            message = self.find_element(By.ID, "id_error_password")
            assert EQUIVALENT_CLASS_EXCEPT['test 1'] in message.text
            print("Test 1: PASS")
        except:
            print("Test 1: FAIL")

        self.reset()

    def test_2(self):
        try:
            self.run_test(current=EQUIVALENT_CLASS_TESTCASE['test 2']['current'],
                          new_password=EQUIVALENT_CLASS_TESTCASE['test 2']['new password'],
                          confirm=EQUIVALENT_CLASS_TESTCASE['test 2']['confirm'])
            message = self.find_element(By.ID, "id_error_newpassword1")
            assert EQUIVALENT_CLASS_EXCEPT['test 2'] in message.text
            print("Test 2: PASS")
        except:
            print("Test 2: FAIL")

        self.reset()

    def test_3(self):
        try:
            self.run_test(current=EQUIVALENT_CLASS_TESTCASE['test 3']['current'],
                          new_password=EQUIVALENT_CLASS_TESTCASE['test 3']['new password'],
                          confirm=EQUIVALENT_CLASS_TESTCASE['test 3']['confirm'])
            message = self.find_element(By.ID, "id_error_newpassword1")
            assert EQUIVALENT_CLASS_EXCEPT['test 3'] in message.text
            print("Test 3: PASS")
        except:
            print("Test 3: FAIL")

        self.reset()

    def test_4(self):
        try:
            self.run_test(current=EQUIVALENT_CLASS_TESTCASE['test 4']['current'],
                          new_password=EQUIVALENT_CLASS_TESTCASE['test 4']['new password'],
                          confirm=EQUIVALENT_CLASS_TESTCASE['test 4']['confirm'])
            message = self.find_element(By.ID, "id_error_newpassword1")
            assert EQUIVALENT_CLASS_EXCEPT['test 4'] in message.text
            print("Test 4: PASS")
        except:
            print("Test 4: FAIL")

        self.reset()

    def test_5(self):
        try:
            self.run_test(current=EQUIVALENT_CLASS_TESTCASE['test 5']['current'],
                          new_password=EQUIVALENT_CLASS_TESTCASE['test 5']['new password'],
                          confirm=EQUIVALENT_CLASS_TESTCASE['test 5']['confirm'])
            message = self.find_element(By.ID, "id_error_newpassword1")
            assert EQUIVALENT_CLASS_EXCEPT['test 5'] in message.text
            print("Test 5: PASS")
        except:
            print("Test 5: FAIL")

        self.reset()

    def test_6(self):
        try:
            self.run_test(current=EQUIVALENT_CLASS_TESTCASE['test 6']['current'],
                          new_password=EQUIVALENT_CLASS_TESTCASE['test 6']['new password'],
                          confirm=EQUIVALENT_CLASS_TESTCASE['test 6']['confirm'])
            message = self.find_element(By.ID, "id_error_newpassword1")
            assert EQUIVALENT_CLASS_EXCEPT['test 6'] in message.text
            print("Test 6: PASS")
        except:
            print("Test 6: FAIL")

        self.reset()

    def test_7(self):
        try:
            self.run_test(current=EQUIVALENT_CLASS_TESTCASE['test 7']['current'],
                          new_password=EQUIVALENT_CLASS_TESTCASE['test 7']['new password'],
                          confirm=EQUIVALENT_CLASS_TESTCASE['test 7']['confirm'])
            message = self.find_element(By.ID, "id_error_newpassword1")
            assert EQUIVALENT_CLASS_EXCEPT['test 7'] in message.text
            print("Test 7: PASS")
        except:
            print("Test 7: FAIL")

        self.reset()

    def run_test(self, current, new_password, confirm):
        if (not self.logged):
            self.login(EQUIVALENT_CLASS_DATA['username'],
                       EQUIVALENT_CLASS_DATA['password'])

        # run test
        # go to change password
        self.find_element(
            By.CSS_SELECTOR, 'a[aria-label="User menu"]').click()

        self.find_element(By.LINK_TEXT, 'Preferences').click()

        self.find_element(By.LINK_TEXT, 'Change password').click()

        # change password
        self.find_element(By.ID, 'id_password').send_keys(current)
        self.find_element(By.ID, 'id_newpassword1').send_keys(new_password)
        self.find_element(By.ID, 'id_newpassword2').send_keys(confirm)
        self.find_element(By.NAME, 'submitbutton').click()

    def setup_data(self):
        # login
        if (not self.logged):
            self.login(ADMIN_ACCOUNT['username'], ADMIN_ACCOUNT['password'])

        # go to add user
        self.add_user(EQUIVALENT_CLASS_DATA['username'],
                      EQUIVALENT_CLASS_DATA['password'], EQUIVALENT_CLASS_DATA['first name'], EQUIVALENT_CLASS_DATA['surname'], EQUIVALENT_CLASS_DATA['email'])
        self.logout()


service = ChromeService(executable_path='./chromedriver.exe')
# driver = webdriver.Chrome(service=service)
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, chrome_options=options)

testcase = EquivalentClass(driver)
driver.get('http://localhost/?lang=en')
testcase.run_all_test()
