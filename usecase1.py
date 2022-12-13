from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


from data import *


class Usecase1:
    def __init__(self, driver):
        self.__driver = driver
        self.__logged = False

    def run_all_test(self):
        print('--------------------------------')
        print('Run Usecase 1 Test:')

        self.setup_data()
        self.test_1()
        self.test_2()
        self.test_3()

        self.logout()
        print('--------------------------------')

    def test_1(self):
        try:
            if (not self.__logged):
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

    def test_2(self):
        try:
            if (not self.__logged):
                self.login(ADMIN_ACCOUNT['username'],
                           ADMIN_ACCOUNT['password'])

            self.find_element(
                by=By.CSS_SELECTOR, value='a[href="http://localhost/?redirect=0"]').click()

            self.find_element(
                by=By.XPATH, value="//a[contains(text(),'Môn 1')]").click()

            assert USECASE1_EXPECT['test 1'] in self.find_element(
                by=By.CSS_SELECTOR, value='h1.h2').text

            print("Test 2: PASS")
        except:
            print("Test 2: FAIL")

        self.reset()

    def test_3(self):
        try:
            if (not self.__logged):
                self.login(ADMIN_ACCOUNT['username'],
                           ADMIN_ACCOUNT['password'])

            self.find_element(
                by=By.CSS_SELECTOR, value='a[href="http://localhost/my/courses.php"]').click()

            course = self.find_element(
                by=By.XPATH, value="//span[contains(text(),'Môn 1')]")
            course.find_element(by=By.XPATH, value='..').click()

            assert USECASE1_EXPECT['test 1'] in self.find_element(
                by=By.CSS_SELECTOR, value='h1.h2').text

            print("Test 3: PASS")
        except:
            print("Test 3: FAIL")

        self.reset()

    def setup_data(self):
        # login
        if (not self.__logged):
            self.login(ADMIN_ACCOUNT['username'], ADMIN_ACCOUNT['password'])

        for course in USECASE1_DATA:
            # go to add course
            self.find_element(
                by=By.CSS_SELECTOR, value='a[href="http://localhost/admin/search.php"]').click()
            self.find_element(by=By.LINK_TEXT, value='Courses').click()
            self.find_element(
                by=By.LINK_TEXT, value='Add a new course').click()

            # add course
            self.find_element(by=By.ID, value='id_fullname').send_keys(
                USECASE1_DATA[course]['full name'])
            self.find_element(by=By.ID, value='id_shortname').send_keys(
                USECASE1_DATA[course]['short name'])
            self.find_element(by=By.NAME, value='saveanddisplay').click()

        self.reset()

    def login(self, username, password):
        login_btn = self.find_element(
            by=By.CSS_SELECTOR, value='.login a')
        login_btn.click()

        username_input = self.find_element(
            by=By.CSS_SELECTOR, value='input[name="username"]')
        username_input.clear()
        username_input.send_keys(username)

        password_input = self.find_element(
            by=By.CSS_SELECTOR, value='input[name="password"]')
        password_input.clear()
        password_input.send_keys(password)

        login_btn = self.find_element(by=By.ID, value='loginbtn')
        login_btn.click()
        self.__logged = True

    def logout(self):
        self.find_element(
            By.CSS_SELECTOR, 'a[aria-label="User menu"]').click()

        self.find_element(By.LINK_TEXT, 'Log out').click()

        self.__logged = False

    def reset(self):
        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/my/"]').click()

    def find_element(self, by, value):
        return WebDriverWait(self.__driver, 50).until(
            EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        return WebDriverWait(self.__driver, 2).until(
            EC.presence_of_all_elements_located((by, value)))
