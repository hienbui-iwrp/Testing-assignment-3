from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *


class DecisionTable:
    def __init__(self, driver):
        self.__driver = driver
        self.__logged = False

    def run_all_test(self):
        print('--------------------------------')
        print('Run Decision Table Test:')

        self.setup_data()
        self.test_1()
        self.test_2()
        self.test_3()
        self.test_4()
        self.test_5()
        self.test_6()
        self.test_7()
        self.test_8()
        self.test_9()
        self.test_10()
        self.test_11()
        self.test_12()

        self.logout()
        print('--------------------------------')

    def test_1(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 1']['filter'], sort=DECISION_TABLE_TESTCASE['test 1']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 1']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 1: PASS")
        except:
            print("Test 1: FAIL")

    def test_2(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 2']['filter'], sort=DECISION_TABLE_TESTCASE['test 2']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 2']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()

            print("Test 2: PASS")
        except:
            print("Test 2: FAIL")

    def test_3(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 3']['filter'], sort=DECISION_TABLE_TESTCASE['test 3']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 3']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 3: PASS")
        except:
            print("Test 3: FAIL")

    def test_4(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 4']['filter'], sort=DECISION_TABLE_TESTCASE['test 4']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 4']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 4: PASS")
        except:
            print("Test 4: FAIL")

    def test_5(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 5']['filter'], sort=DECISION_TABLE_TESTCASE['test 5']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 5']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 5: PASS")
        except:
            print("Test 5: FAIL")

    def test_6(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 6']['filter'], sort=DECISION_TABLE_TESTCASE['test 6']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 6']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 6: PASS")
        except:
            print("Test 6: FAIL")

    def test_7(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 7']['filter'], sort=DECISION_TABLE_TESTCASE['test 7']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 7']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 7: PASS")
        except:
            print("Test 7: FAIL")

    def test_8(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 8']['filter'], sort=DECISION_TABLE_TESTCASE['test 8']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 8']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 8: PASS")
        except:
            print("Test 8: FAIL")

    def test_9(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 9']['filter'], sort=DECISION_TABLE_TESTCASE['test 9']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 9']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 9: PASS")
        except:
            print("Test 9: FAIL")

    def test_10(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 10']['filter'], sort=DECISION_TABLE_TESTCASE['test 10']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 10']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 10: PASS")
        except:
            print("Test 10: FAIL")

    def test_11(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 11']['filter'], sort=DECISION_TABLE_TESTCASE['test 11']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 11']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 11: PASS")
        except:
            print("Test 11: FAIL")

    def test_12(self):
        try:
            self.run_test(
                filter=DECISION_TABLE_TESTCASE['test 12']['filter'], sort=DECISION_TABLE_TESTCASE['test 12']['sort'])
            courses = self.find_elements(
                by=By.CSS_SELECTOR, value='.event-name-container a')
            for expect in DECISION_TABLE_EXPECT['test 12']:
                have = False
                for course in courses:
                    if expect in course.text:
                        have = True
                        break
                if (not have):
                    raise Exception()
            print("Test 12: PASS")
        except:
            print("Test 12: FAIL")

    def run_test(self, filter, sort):
        if (not self.__logged):
            self.login(ADMIN_ACCOUNT['username'],
                       ADMIN_ACCOUNT['password'])

        # run test
        self.find_element(
            By.CSS_SELECTOR, 'button[title="Filter timeline by date"]').click()
        self.find_element(
            by=By.XPATH, value="//a[contains(text(),'" + filter + "')]").click()

        self.find_element(
            By.CSS_SELECTOR, 'button[title="Sort timeline items"]').click()
        self.find_element(
            by=By.XPATH, value="//a[contains(text(),'" + sort + "')]").click()

        try:
            self.find_element(
                by=By.CSS_SELECTOR, value='button[data-action="more-events"]').click()
        except:
            pass

    def setup_data(self):
        # login
        if (not self.__logged):
            self.login(ADMIN_ACCOUNT['username'], ADMIN_ACCOUNT['password'])

        # go to add course
        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/admin/search.php"]').click()
        self.find_element(by=By.LINK_TEXT, value='Courses').click()
        self.find_element(by=By.LINK_TEXT, value='Add a new course').click()

        # add course
        self.find_element(by=By.ID, value='id_fullname').send_keys(
            DECISION_TABLE_DATA['course']['full name'])
        self.find_element(by=By.ID, value='id_shortname').send_keys(
            DECISION_TABLE_DATA['course']['short name'])
        self.find_element(by=By.NAME, value='saveanddisplay').click()
        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/my/courses.php"]').click()
        course = self.find_element(
            by=By.XPATH, value="//span[contains(text(),'Môn 4')]")
        course.find_element(by=By.XPATH, value='..').click()

        self.find_element(by=By.NAME, value='setmode').click()
        try:
            WebDriverWait(self.__driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Skip tour')]"))).click()
        except:
            pass

        # add event 1
        self.find_element(by=By.CSS_SELECTOR,
                          value='button[data-sectionid="1"]').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='a[title="Add a new Assignment"]').click()
        # input data
        self.find_element(by=By.NAME, value='name').send_keys(
            DECISION_TABLE_DATA['overdue']['name'])
        self.find_element(by=By.ID, value='id_allowsubmissionsfromdate_day').send_keys(
            DECISION_TABLE_DATA['overdue']['allow submission']['day'])
        self.find_element(by=By.ID, value='id_allowsubmissionsfromdate_month').send_keys(
            DECISION_TABLE_DATA['overdue']['allow submission']['month'])
        self.find_element(by=By.ID, value='id_allowsubmissionsfromdate_year').send_keys(
            DECISION_TABLE_DATA['overdue']['allow submission']['year'])

        self.find_element(by=By.ID, value='id_duedate_day').send_keys(
            DECISION_TABLE_DATA['overdue']['due date']['day'])
        self.find_element(by=By.ID, value='id_duedate_month').send_keys(
            DECISION_TABLE_DATA['overdue']['due date']['month'])
        self.find_element(by=By.ID, value='id_duedate_year').send_keys(
            DECISION_TABLE_DATA['overdue']['due date']['year'])

        self.find_element(by=By.ID, value='id_submitbutton2').click()

        # add event 2
        self.find_element(by=By.CSS_SELECTOR,
                          value='button[data-sectionid="2"]').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='a[title="Add a new Assignment"]').click()
        # input data
        self.find_element(by=By.NAME, value='name').send_keys(
            DECISION_TABLE_DATA['7 dates']['name'])
        self.find_element(by=By.ID, value='id_submitbutton2').click()

        # add event 3
        self.find_element(by=By.CSS_SELECTOR,
                          value='button[data-sectionid="3"]').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='a[title="Add a new Assignment"]').click()
        # input data
        self.find_element(by=By.NAME, value='name').send_keys(
            DECISION_TABLE_DATA['30 dates']['name'])
        self.find_element(by=By.ID, value='id_duedate_day').send_keys(
            DECISION_TABLE_DATA['30 dates']['due date']['day'])
        self.find_element(by=By.ID, value='id_duedate_month').send_keys(
            DECISION_TABLE_DATA['30 dates']['due date']['month'])
        self.find_element(by=By.ID, value='id_duedate_year').send_keys(
            DECISION_TABLE_DATA['30 dates']['due date']['year'])
        self.find_element(by=By.ID, value='id_gradingduedate_day').send_keys(
            DECISION_TABLE_DATA['30 dates']['remind']['day'])
        self.find_element(by=By.ID, value='id_gradingduedate_month').send_keys(
            DECISION_TABLE_DATA['30 dates']['remind']['month'])
        self.find_element(by=By.ID, value='id_gradingduedate_year').send_keys(
            DECISION_TABLE_DATA['30 dates']['remind']['year'])
        self.find_element(by=By.ID, value='id_submitbutton2').click()

        # add event 4
        self.find_element(by=By.CSS_SELECTOR,
                          value='button[data-sectionid="4"]').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='a[title="Add a new Assignment"]').click()
        # input data
        self.find_element(by=By.NAME, value='name').send_keys(
            DECISION_TABLE_DATA['3 months']['name'])
        self.find_element(by=By.ID, value='id_duedate_day').send_keys(
            DECISION_TABLE_DATA['3 months']['due date']['day'])
        self.find_element(by=By.ID, value='id_duedate_month').send_keys(
            DECISION_TABLE_DATA['3 months']['due date']['month'])
        self.find_element(by=By.ID, value='id_duedate_year').send_keys(
            DECISION_TABLE_DATA['3 months']['due date']['year'])
        self.find_element(by=By.ID, value='id_gradingduedate_day').send_keys(
            DECISION_TABLE_DATA['3 months']['remind']['day'])
        self.find_element(by=By.ID, value='id_gradingduedate_month').send_keys(
            DECISION_TABLE_DATA['3 months']['remind']['month'])
        self.find_element(by=By.ID, value='id_gradingduedate_year').send_keys(
            DECISION_TABLE_DATA['3 months']['remind']['year'])
        self.find_element(by=By.ID, value='id_submitbutton2').click()

        # add event 5
        self.find_element(by=By.CSS_SELECTOR,
                          value='button[data-sectionid="4"]').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='a[title="Add a new Assignment"]').click()
        # input data
        self.find_element(by=By.NAME, value='name').send_keys(
            DECISION_TABLE_DATA['6 months']['name'])
        self.find_element(by=By.ID, value='id_duedate_day').send_keys(
            DECISION_TABLE_DATA['6 months']['due date']['day'])
        self.find_element(by=By.ID, value='id_duedate_month').send_keys(
            DECISION_TABLE_DATA['6 months']['due date']['month'])
        self.find_element(by=By.ID, value='id_duedate_year').send_keys(
            DECISION_TABLE_DATA['6 months']['due date']['year'])
        self.find_element(by=By.ID, value='id_gradingduedate_day').send_keys(
            DECISION_TABLE_DATA['6 months']['remind']['day'])
        self.find_element(by=By.ID, value='id_gradingduedate_month').send_keys(
            DECISION_TABLE_DATA['6 months']['remind']['month'])
        self.find_element(by=By.ID, value='id_gradingduedate_year').send_keys(
            DECISION_TABLE_DATA['6 months']['remind']['year'])
        self.find_element(by=By.ID, value='id_submitbutton2').click()

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
        return WebDriverWait(self.__driver, 1).until(
            EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        WebDriverWait(self.__driver, 1).until(
            EC.visibility_of_element_located((by, value)))

        elements = self.__driver.find_elements(
            by, value)

        return [element for element in elements]
