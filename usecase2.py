from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

from data import *
from testcase import *


class Usecase2(TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def run_all_test(self):
        print('--------------------------------')
        print('Run Usecase 2 Test:')
        self.setup_data()
        # run test
        self.path_1()
        self.path_2()
        self.path_3()
        self.path_4()

        self.logout()
        print('--------------------------------')

    def path_1(self):
        try:
            self.run_test(quiz=USECASE2_DATA['quizs'][2]['name'])
            self.find_element(by=By.CSS_SELECTOR,
                              value='button[type="submit"]').click()

            assert USECASE2_EXPECT['path 1'] in self.find_element(
                by=By.CSS_SELECTOR, value='input[type="submit"]').get_attribute('value')

            print("Path 1: PASS")
        except:
            print("Path 1: FAIL")

        self.reset()

    def path_2(self):
        try:
            self.run_test(quiz=USECASE2_DATA['quizs'][0]['name'])

            assert USECASE2_EXPECT['path 2'] in self.find_element(
                by=By.CSS_SELECTOR, value='button[type="submit"]').text

            print("Path 2: PASS")
        except:
            print("Path 2: FAIL")

        self.reset()

    def path_3(self):
        try:
            self.run_test(quiz=USECASE2_DATA['quizs'][3]['name'])

            assert USECASE2_EXPECT['path 3'] in self.find_element(
                by=By.CSS_SELECTOR, value='button[type="submit"]').text

            print("Path 3: PASS")
        except:
            print("Path 3: FAIL")

        self.reset()

    def path_4(self):
        try:
            self.run_test(quiz=USECASE2_DATA['quizs'][1]['name'])

            self.wait(10)
            assert USECASE2_EXPECT['path 4'] in self.find_element(
                by=By.CSS_SELECTOR, value='button[type="submit"]').text

            print("Path 4: PASS")
        except:
            print("Path 4: FAIL")

        self.reset()

    def run_test(self, quiz):
        if (not self.logged):
            self.login(USECASE2_DATA['account']['username'],
                       USECASE2_DATA['account']['password'])

        self.go_to_course(USECASE2_DATA['course']['full name'])
        list_quiz = self.find_elements(by=By.LINK_TEXT, value=quiz)
        list_quiz[-1].find_element(By.XPATH, '..').click()

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
                self.wait(1)
                if not show_time:
                    time = self.find_element(
                        by=By.ID, value='collapseElement-1')
                    time.click()
                    show_time = True

                self.wait(1)
                self.find_element(
                    by=By.ID, value='id_timeopen_enabled').click()
                self.select_key(self.find_element(
                    by=By.ID, value='id_timeopen_day'), str(quiz['open']['day']))
                self.select_key(self.find_element(
                    by=By.ID, value='id_timeopen_month'), str(quiz['open']['month']))
                self.select_key(self.find_element(
                    by=By.ID, value='id_timeopen_year'), str(quiz['open']['year']))

            if 'close' in quiz:
                self.wait(1)
                if not show_time:
                    time = self.find_element(
                        by=By.ID, value='collapseElement-1')
                    time.click()
                    show_time = True
                self.wait(1)
                self.find_element(
                    by=By.ID, value='id_timeclose_enabled').click()
                self.select_key(self.find_element(
                    by=By.ID, value='id_timeclose_day'), str(quiz['close']['day']))
                self.select_key(self.find_element(
                    by=By.ID, value='id_timeclose_month'), str(quiz['close']['month']))
                self.select_key(self.find_element(
                    by=By.ID, value='id_timeclose_year'), str(quiz['close']['year']))

            if 'attempt' in quiz:
                self.wait(1)
                grade = self.find_element(by=By.ID, value='collapseElement-2')
                grade.click()
                self.wait(1)
                grade_list = self.find_element(
                    by=By.XPATH, value="//select[@name='attempts']")
                self.select_key(grade_list, str(quiz['attempt']))

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
        self.wait(1)
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
        list_quiz = self.find_elements(by=By.LINK_TEXT, value=quizs[1])

        list_quiz[-1].find_element(By.XPATH, '..').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='button[type="submit"]').click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='input[type="submit"]').click()
        self.find_element(by=By.XPATH,
                          value="//button[contains(text(),'Submit all and finish')]").click()
        self.find_element(by=By.CSS_SELECTOR,
                          value='input[value="Submit all and finish"]').click()

        self.logout()


# setup
service = ChromeService(executable_path='./chromedriver.exe')
# driver = webdriver.Chrome(service=service)
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, chrome_options=options)

# run test
testcase = Usecase2(driver)
driver.get('http://localhost/?lang=en')
testcase.run_all_test()
