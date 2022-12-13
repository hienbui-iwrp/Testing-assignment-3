from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *


class Boundary:
    def __init__(self, driver):
        self.__driver = driver
        self.__logged = False

    def run_all_test(self):
        print('--------------------------------')
        print('Run Boundary Test:')

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
            self.run_test(BOUNDARY_TESTCASE['test 1'])
            message = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

            assert BOUNDARY_EXPECT['test 1'] in message.text

            print("Test 1: PASS")
        except:
            print("Test 1: FAIL")
        self.reset()

    def test_2(self):
        try:
            current = self.run_test(BOUNDARY_TESTCASE['test 2'])
            if (current != BOUNDARY_TESTCASE['test 2']):
                message = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

                assert BOUNDARY_EXPECT['test 2'] in message.text

            print("Test 2: PASS")
        except:
            print("Test 2: FAIL")
        self.reset()

    def test_3(self):
        try:
            current = self.run_test(BOUNDARY_TESTCASE['test 3'])
            if (current != BOUNDARY_TESTCASE['test 3']):
                message = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

                assert BOUNDARY_EXPECT['test 3'] in message.text

            print("Test 3: PASS")
        except:
            print("Test 3: FAIL")
        self.reset()

    def test_4(self):
        try:
            current = self.run_test(BOUNDARY_TESTCASE['test 4'])
            if (current != BOUNDARY_TESTCASE['test 4']):
                message = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

                assert BOUNDARY_EXPECT['test 4'] in message.text

            print("Test 4: PASS")
        except:
            print("Test 4: FAIL")
        self.reset()

    def test_5(self):
        try:
            current = self.run_test(BOUNDARY_TESTCASE['test 5'])
            if (current != BOUNDARY_TESTCASE['test 5']):
                message = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

                assert BOUNDARY_EXPECT['test 5'] in message.text

            print("Test 5: PASS")
        except:
            print("Test 5: FAIL")
        self.reset()

    def test_6(self):
        try:
            current = self.run_test(BOUNDARY_TESTCASE['test 6'])
            if (current != BOUNDARY_TESTCASE['test 6']):
                message = WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

                assert BOUNDARY_EXPECT['test 6'] in message.text

            print("Test 6: PASS")
        except:
            print("Test 6: FAIL")

        self.reset()

    def test_7(self):
        try:
            self.run_test(BOUNDARY_TESTCASE['test 7'])
            message = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

            assert BOUNDARY_EXPECT['test 7'] in message.text

            print("Test 7: PASS")
        except:
            print("Test 7: FAIL")
        self.reset()

    def run_test(self, max):
        # login
        if (not self.__logged):
            login_btn = self.find_element(
                by=By.CSS_SELECTOR, value='.login a')
            login_btn.click()

            username_input = self.find_element(
                by=By.CSS_SELECTOR, value='input[name="username"]')
            username_input.clear()
            username_input.send_keys(ADMIN_ACCOUNT['username'])

            password_input = self.find_element(
                by=By.CSS_SELECTOR, value='input[name="password"]')
            password_input.clear()
            password_input.send_keys(ADMIN_ACCOUNT['password'])

            login_btn = self.find_element(by=By.ID, value='loginbtn')
            login_btn.click()
            self.__logged = True

        # run test
        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/admin/search.php"]').click()

        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="#linkgrades"]').click()

        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/admin/settings.php?section=gradessettings"]').click()

        grade_point_maximum_input = self.find_element(
            by=By.NAME, value='s__gradepointmax')
        current = grade_point_maximum_input.text
        grade_point_maximum_input.clear()
        grade_point_maximum_input.send_keys(max)

        grade_point_default_input = self.find_element(
            by=By.NAME, value='s__gradepointdefault')
        grade_point_default_input.clear()
        grade_point_default_input.send_keys(1)

        self.find_element(
            by=By.CSS_SELECTOR, value='.row button').click()

        return current

    def logout(self):
        self.find_element(
            By.CSS_SELECTOR, 'a[aria-label="User menu"]').click()

        self.find_element(By.LINK_TEXT, 'Log out').click()

        self.__logged = False

    def reset(self):
        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/my/"]').click()

    def find_element(self, by, value):
        return WebDriverWait(self.__driver, 5).until(
            EC.presence_of_element_located((by, value)))
