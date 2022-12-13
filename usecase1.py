from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


from data import *
from testcase import *


class Usecase1(TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def run_all_test(self):
        print('--------------------------------')
        print('Run Usecase 1 Test:')

        self.setup_data()
        self.path_1()
        self.path_2()
        self.path_3()

        self.logout()
        print('--------------------------------')

    def path_1(self):
        try:
            if (not self.logged):
                self.login(ADMIN_ACCOUNT['username'],
                           ADMIN_ACCOUNT['password'])

            self.find_element(
                by=By.CSS_SELECTOR, value='a[href="http://localhost/my/courses.php"]').click()

            search_box = self.find_element(
                by=By.ID, value='searchinput')
            search_box.clear()
            search_box.send_keys(USECASE1_DATA['course 1']['full name'])
            search_box.send_keys(Keys.ENTER)

            course = self.find_element(
                by=By.XPATH, value="//span[contains(text(),'Môn 1')]")
            course.find_element(by=By.XPATH, value='..').click()

            assert USECASE1_EXPECT['test 1'] in self.find_element(
                by=By.CSS_SELECTOR, value='h1.h2').text

            print("Test 1: PASS")
        except:
            print("Test 1: FAIL")

        self.reset()

    def path_2(self):
        try:
            if (not self.logged):
                self.login(ADMIN_ACCOUNT['username'],
                           ADMIN_ACCOUNT['password'])

            self.find_element(
                by=By.CSS_SELECTOR, value='a[href="http://localhost/?redirect=0"]').click()

            self.find_element(
                by=By.XPATH, value="//a[contains(text(),'"+USECASE1_DATA['course 1']['full name']+"')]").click()

            assert USECASE1_EXPECT['test 1'] in self.find_element(
                by=By.CSS_SELECTOR, value='h1.h2').text

            print("Test 2: PASS")
        except:
            print("Test 2: FAIL")

        self.reset()

    def path_3(self):
        try:
            if (not self.logged):
                self.login(ADMIN_ACCOUNT['username'],
                           ADMIN_ACCOUNT['password'])

            self.go_to_course(USECASE1_DATA['course 1']['full name'])

            assert USECASE1_EXPECT['test 1'] in self.find_element(
                by=By.CSS_SELECTOR, value='h1.h2').text

            print("Test 3: PASS")
        except:
            print("Test 3: FAIL")

        self.reset()

    def setup_data(self):
        # login
        if (not self.logged):
            self.login(ADMIN_ACCOUNT['username'], ADMIN_ACCOUNT['password'])

        for course in USECASE1_DATA:
            self.add_course(
                USECASE1_DATA[course]['full name'], USECASE1_DATA[course]['short name'])

        self.reset()
