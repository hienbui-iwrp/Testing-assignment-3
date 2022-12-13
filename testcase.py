from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase:

    def __init__(self, driver):
        self.driver = driver
        self.logged = False

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
        self.logged = True

        try:
            self.driver.implicitly_wait(1)
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Got it')]"))).click()
        except:
            pass

    def logout(self):
        self.find_element(
            By.CSS_SELECTOR, 'a[aria-label="User menu"]').click()

        self.find_element(By.LINK_TEXT, 'Log out').click()

        self.logged = False

    def go_to_course(self, name, editmode=False):
        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/my/courses.php"]').click()
        try:
            self.driver.implicitly_wait(1)
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'I understand')]"))).click()
        except:
            pass
        course = self.find_element(
            by=By.XPATH, value="//span[contains(text(),'" + name + "')]")
        course.find_element(by=By.XPATH, value='..').click()
        if (editmode):
            self.find_element(by=By.NAME, value='setmode').click()
            try:
                WebDriverWait(self.driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Skip tour')]"))).click()
            except:
                pass

    def reset(self):
        self.find_element(
            by=By.CSS_SELECTOR, value='a[href="http://localhost/my/"]').click()

    def find_element(self, by, value):
        return WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located((by, value)))

        elements = self.driver.find_elements(
            by, value)

        return [element for element in elements]
