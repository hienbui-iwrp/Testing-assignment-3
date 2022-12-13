from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *
from testcase import *


class EquivalentClass(TestCase):
    def __init__(self, driver):
        self.driver = driver
        self.logged = False

    def run_all_test(self):
        print('--------------------------------')
        print('Run Equivalent Class Test:')

        self.setup_data()
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
        site_admin_btn = self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/admin/search.php"]')
        site_admin_btn.click()

        users_btn = self.find_element(
            by=By.LINK_TEXT, value='Users')
        users_btn.click()

        add_btn = self.find_element(
            by=By.LINK_TEXT, value='Add a new user')
        add_btn.click()

        # add user
        username_input = self.find_element(
            by=By.NAME, value='username')
        username_input.clear()
        username_input.send_keys(EQUIVALENT_CLASS_DATA['username'])

        password_btn = self.find_element(
            by=By.CSS_SELECTOR, value='.form-control[data-passwordunmask="edit"]')
        password_btn.click()

        newpassword_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "newpassword")))
        newpassword_input.clear()
        newpassword_input.send_keys(EQUIVALENT_CLASS_DATA['password'])

        firstname_input = self.find_element(
            by=By.NAME, value='firstname')
        firstname_input.clear()
        firstname_input.send_keys(EQUIVALENT_CLASS_DATA['first name'])

        lastname_input = self.find_element(
            by=By.NAME, value='lastname')
        lastname_input.clear()
        lastname_input.send_keys(EQUIVALENT_CLASS_DATA['surname'])

        email_input = self.find_element(by=By.NAME, value='email')
        email_input.clear()
        email_input.send_keys(EQUIVALENT_CLASS_DATA['email'])

        submit_btn = self.find_element(
            by=By.NAME, value='submitbutton')
        submit_btn.click()

        self.logout()
