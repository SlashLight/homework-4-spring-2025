from selenium.webdriver.common.by import By
from .base_page import BasePage

class SurveysPage(BasePage):
    SURVEY_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[1]/span[2]/div/div/input')
    LOGO_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[3]/div')
    COMPANY_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[5]/span[2]/div/div/input')
    SURVEY_HEADER_INPUT = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[5]/span[2]/div/div/input')
    SURVEY_DESCRIPTION_INPUT = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[6]/span[2]/div/div/textarea')
    SURVEY_STYLE = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[8]/div[2]')
    SURVEY_THEME = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div[1]/div[1]/div')
    SURVEY_FORMAT = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div[1]/div[2]/div')
    NEXT_QUESTIONS_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/button')

    def __init__(self, driver):
        super().__init__(driver)
        self.BASE_URL = 'https://ads.vk.ru/hq/leadads/surveys'

    def open_survey_page(self):
        self.open(self.BASE_URL)
        return self

    def enter_survey_name(self, survey_name: str):
        self.fill(self.SURVEY_NAME_INPUT, survey_name)
        return self