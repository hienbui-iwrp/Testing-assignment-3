from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


from data import *
from testcase import *


class Usecase2(TestCase):
    def __init__(self, driver):
        pass

    def run_all_test(self):
        print('--------------------------------')
        print('Run Usecase 2 Test:')

        self.setup_data()
        # self.test_1()

        self.logout()
        self.find_element(by=By.CLASS_NAME, value='asdas')
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
        username_input.send_keys(USECASE2_DATA['account']['username'])

        password_btn = self.find_element(
            by=By.CSS_SELECTOR, value='.form-control[data-passwordunmask="edit"]')
        password_btn.click()

        newpassword_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "newpassword")))
        newpassword_input.clear()
        newpassword_input.send_keys(USECASE2_DATA['account']['password'])

        firstname_input = self.find_element(
            by=By.NAME, value='firstname')
        firstname_input.clear()
        firstname_input.send_keys(USECASE2_DATA['account']['first name'])

        lastname_input = self.find_element(
            by=By.NAME, value='lastname')
        lastname_input.clear()
        lastname_input.send_keys(USECASE2_DATA['account']['surname'])

        email_input = self.find_element(by=By.NAME, value='email')
        email_input.clear()
        email_input.send_keys(USECASE2_DATA['account']['email'])

        submit_btn = self.find_element(
            by=By.NAME, value='submitbutton')
        submit_btn.click()

        # go to add course
        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/admin/search.php"]').click()
        self.find_element(by=By.LINK_TEXT, value='Courses').click()
        self.find_element(by=By.LINK_TEXT, value='Add a new course').click()

        # add course
        self.find_element(by=By.ID, value='id_fullname').send_keys(
            USECASE2_DATA['course']['full name'])
        self.find_element(by=By.ID, value='id_shortname').send_keys(
            USECASE2_DATA['course']['short name'])
        self.find_element(by=By.NAME, value='saveanddisplay').click()

        # go to course
        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/my/courses.php"]').click()
        try:
            self.driver.implicitly_wait(2)
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'I understand')]"))).click()
        except:
            pass
        course = self.find_element(
            by=By.XPATH, value="//span[contains(text(),'" + USECASE2_DATA['course']['full name'] + "')]")
        course.find_element(by=By.XPATH, value='..').click()

        # turn on edit mode
        self.find_element(by=By.NAME, value='setmode').click()
        try:
            self.driver.implicitly_wait(2)
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Skip tour')]"))).click()
        except:
            pass

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
        self.find_element(
            by=By.CSS_SELECTOR, value='.modal-content li').click()

        self.find_element(by=By.CSS_SELECTOR,
                          value='button[data-action="save"]').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='button[data-action="save"]').click()
        self.logout()
        self.login(USECASE2_DATA['account']['username'],
                   USECASE2_DATA['account']['password'])

        # do quiz
        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/my/courses.php"]').click()
        course = self.find_element(
            by=By.XPATH, value="//span[contains(text(),'" + USECASE2_DATA['course']['full name'] + "')]")
        course.find_element(by=By.XPATH, value='..').click()
        list_quiz = self.find_elements(by=By.LINK_TEXT, value=quizs[2])
        list_quiz[-1].click()
        self.find_elements(by=By.CSS_SELECTOR,
                           value='button[type="submit"]').click()
        self.find_elements(by=By.CSS_SELECTOR,
                           value='input[type="submit"]').click()
        self.find_elements(by=By.LINK_TEXT,
                           value='Submit all and finish').click()
