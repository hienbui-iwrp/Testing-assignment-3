from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


from data import *
from testcase import *


class Usecase2(TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def run_all_test(self):
        print('--------------------------------')
        print('Run Usecase 2 Test:')

        self.setup_data()
        # self.test_1()

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

    def setup_data(self):
        # login
        if (not self.logged):
            self.login(ADMIN_ACCOUNT['username'], ADMIN_ACCOUNT['password'])

        # go to add user
        self.add_user(USECASE2_DATA['account']['username'], USECASE2_DATA['account']['password'], USECASE2_DATA['account']
                      ['first name'], USECASE2_DATA['account']['surname'], USECASE2_DATA['account']['email'])

        # go to add course
        self.add_course(
            USECASE2_DATA['course']['full name'], USECASE2_DATA['course']['short name'])

        # go to course
        self.go_to_course(USECASE2_DATA['course']['full name'], True)

        topic = 1
        # add quiz
        for quiz in USECASE2_DATA['quizs']:
            self.find_element(by=By.CSS_SELECTOR,
                              value='button[data-sectionid="'+str(topic)+'"]').click()
            self.find_element(by=By.CSS_SELECTOR,
                              value='a[title="Add a new Quiz"]').click()
            # input data
            self.find_element(by=By.NAME, value='name').send_keys(
                quiz['name'])

            show_time = False
            if 'open' in quiz:
                if not show_time:
                    time = self.find_element(
                        by=By.ID, value='collapseElement-1')
                    time.click()
                    show_time = True
                self.driver.implicitly_wait(2)
                self.find_element(
                    by=By.ID, value='id_timeopen_enabled').click()
                self.find_element(
                    by=By.ID, value='id_timeopen_day').send_keys(quiz['open']['day'])
                self.find_element(
                    by=By.ID, value='id_timeopen_month').send_keys(quiz['open']['month'])
                self.find_element(
                    by=By.ID, value='id_timeopen_year').send_keys(quiz['open']['year'])

            if 'close' in quiz:
                if not show_time:
                    time = self.find_element(
                        by=By.ID, value='collapseElement-1')
                    time.click()
                    show_time = True
                self.driver.implicitly_wait(2)
                self.find_element(
                    by=By.ID, value='id_timeclose_enabled').click()
                self.find_element(
                    by=By.ID, value='id_timeclose_day').send_keys(quiz['close']['day'])
                self.find_element(
                    by=By.ID, value='id_timeclose_month').send_keys(quiz['close']['month'])
                self.find_element(
                    by=By.ID, value='id_timeclose_year').send_keys(quiz['close']['year'])

            if 'attempt' in quiz:
                grade = self.find_element(by=By.ID, value='collapseElement-2')
                grade.click()
                self.driver.implicitly_wait(2000)
                grade_list = self.find_element(
                    by=By.XPATH, value="//select[@name='attempts']")
                grade_list.click()
                Select(grade_list).select_by_value(str(quiz['attempt']))

            self.find_element(
                by=By.ID, value='id_submitbutton2').click()
            topic += 1

        # add question
        quizs = [quiz['name'] for quiz in USECASE2_DATA['quizs']]
        for quiz in quizs:

            list_quiz = self.find_elements(by=By.LINK_TEXT, value=quiz)
            list_quiz[-1].find_element(by=By.XPATH, value='..').click()

            self.find_element(by=By.LINK_TEXT, value='Add question').click()
            self.find_element(by=By.CSS_SELECTOR,
                              value='a[aria-label="Add"]').click()
            self.find_element(by=By.CSS_SELECTOR,
                              value='a[data-action="addquestion"]').click()

            self.find_element(by=By.CSS_SELECTOR,
                              value='input[value="truefalse"]').click()
            self.find_element(by=By.CSS_SELECTOR,
                              value='input[name="submitbutton"]').click()
            self.find_element(by=By.CSS_SELECTOR,
                              value='input[name="name"]').send_keys(USECASE2_DATA['question']['name'])

            self.find_element(by=By.ID,
                              value='id_questiontexteditable').send_keys(USECASE2_DATA['question']['text'])

            self.find_element(by=By.NAME,
                              value='submitbutton').click()

            self.find_element(by=By.LINK_TEXT,
                              value='Môn 3').click()

        # enrol user
        self.find_element(by=By.LINK_TEXT, value='Participants').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='input[value="Enrol users"]').click()
        search_input = self.find_element(
            by=By.CSS_SELECTOR, value='.modal-content input[placeholder="Search"]')
        search_input.send_keys(USECASE2_DATA['account']['email'])
        try:
            self.find_element(
                by=By.CSS_SELECTOR, value='.modal-content li').click()
        except:
            pass

        self.wait(1)

        self.find_element(by=By.CSS_SELECTOR,
                          value='button[data-action="save"]').click()

        self.logout()
        self.login(USECASE2_DATA['account']['username'],
                   USECASE2_DATA['account']['password'])

        # do quiz
        self.go_to_course(USECASE2_DATA['course']['full name'])
        list_quiz = self.find_elements(by=By.LINK_TEXT, value=quizs[2])

        list_quiz[-1].find_element(By.XPATH, '..').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='button[type="submit"]').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='input[type="submit"]').click()
        self.find_element(by=By.XPATH,
                          value="//button[contains(text(),'Submit all and finish')]").click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='input[value="Submit all and finish"]').click()
