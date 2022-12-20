from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from data import *
from testcase import *


class DecisionTable(TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def run_all_test(self):
        print('--------------------------------')
        print('Run Decision Table Test:')
        self.setup_data()

        # run test
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
        if (not self.logged):
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
        if (not self.logged):
            self.login(ADMIN_ACCOUNT['username'], ADMIN_ACCOUNT['password'])

        # add course
        self.add_course(
            DECISION_TABLE_DATA['course']['full name'], DECISION_TABLE_DATA['course']['short name'])

        self.go_to_course(DECISION_TABLE_DATA['course']['full name'], True)

        # add event
        for event in DECISION_TABLE_DATA['events']:
            self.find_element(by=By.CSS_SELECTOR,
                              value='button[data-sectionid="' + str(event['topic']) + '"]').click()
            self.find_element(by=By.CSS_SELECTOR,
                              value='a[title="Add a new Assignment"]').click()

            # input data
            self.find_element(by=By.NAME, value='name').send_keys(
                event['name'])
            if 'allow submission' in event:
                self.select_key(self.find_element(
                    by=By.ID, value='id_allowsubmissionsfromdate_day'), str(event['allow submission']['day']))
                self.select_key(self.find_element(
                    by=By.ID, value='id_allowsubmissionsfromdate_month'), str(event['allow submission']['month']))
                self.select_key(self.find_element(
                    by=By.ID, value='id_allowsubmissionsfromdate_year'), str(event['allow submission']['year']))

            if 'due date' in event:
                self.select_key(self.find_element(
                    by=By.ID, value='id_duedate_day'), str(event['due date']['day']))
                self.select_key(self.find_element(
                    by=By.ID, value='id_duedate_month'), str(event['due date']['month']))
                self.select_key(self.find_element(
                    by=By.ID, value='id_duedate_year'), str(event['due date']['year']))

            # self.wait(100)

            if 'remind' in event:
                self.select_key(self.find_element(
                    by=By.ID, value='id_gradingduedate_day'), str(event['remind']['day']))
                self.select_key(self.find_element(
                    by=By.ID, value='id_gradingduedate_month'), str(event['remind']['month']))
                self.select_key(self.find_element(
                    by=By.ID, value='id_gradingduedate_year'), str(event['remind']['year']))

            self.find_element(by=By.ID, value='id_submitbutton2').click()

        self.reset()


# setup
service = ChromeService(executable_path='./chromedriver.exe')
# driver = webdriver.Chrome(service=service)
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)

# run test
testcase = DecisionTable(driver)
driver.get('http://localhost/?lang=en')
testcase.run_all_test()
