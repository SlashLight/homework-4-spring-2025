from selenium.webdriver.common.by import By
from .base_page import BasePage

class SurveysPage(BasePage):
    CREATE_SURVEY_BUTTON = (By.XPATH, '//*[@id="leadads.surveys"]/div/div[2]/div[1]/div[1]/button')

    SURVEY_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[1]/span[2]/div/div/input')
    COMPANY_NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[5]/span[2]/div/div/input')
    SURVEY_HEADER_INPUT = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[5]/span[2]/div/div/input')
    SURVEY_DESCRIPTION_INPUT = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[6]/span[2]/div/div/textarea')

    SURVEY_THEME_LIGHT = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div[1]/div[1]/div/label[1]/input')
    SURVEY_THEME_DARK = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div[1]/div[1]/div/label[2]/input')

    SURVEY_FORMAT_PHONE = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div[1]/div[2]/div/label[1]/input')
    SURVEY_FORMAT_DESKTOP = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[2]/div/div/div[1]/div[2]/div/label[2]/input')


    LOGO_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[3]/div')


    SURVEY_STYLE_NONE = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[8]/div[2]/div[1]')
    SURVEY_STYLE_YELLOW = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[1]/section/div/div[8]/div[2]/div[3]')

    NEXT_QUESTIONS_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/form/div[2]/div[1]/div[2]/div/button')

    def __init__(self, driver):
        super().__init__(driver)
        self.BASE_URL = 'https://ads.vk.ru/hq/leadads/surveys'

    def open_survey_page(self):
        self.open(self.BASE_URL)
        self.click(self.CREATE_SURVEY_BUTTON)
        return self

    def enter_survey_name(self, survey_name: str):
        self.fill(self.SURVEY_NAME_INPUT, survey_name)
        return self

    def enter_company_name(self, name: str):
        self.fill(self.COMPANY_NAME_INPUT, name)
        return self

    def enter_survey_header(self, name: str):
        self.fill(self.SURVEY_HEADER_INPUT, name)
        return self

    def enter_description(self, name: str):
        self.fill(self.SURVEY_NAME_INPUT, name)
        return self

    def change_survey_style(self, style: str):
        styles = {
            -1: self.SURVEY_STYLE_NONE,
            2: self.SURVEY_STYLE_YELLOW
        }
        self.select_radio(styles[style])

    def change_survey_theme(self, theme: str):
        themes = {
            "light": self.SURVEY_THEME_LIGHT,
            "dark": self.SURVEY_THEME_DARK
        }

        self.select_radio(themes[theme])

    def change_survey_format(self, format: str):
        formats = {
            "mobile": self.SURVEY_FORMAT_PHONE,
            "desktop": self.SURVEY_FORMAT_DESKTOP
        }
        self.select_radio(formats[format])