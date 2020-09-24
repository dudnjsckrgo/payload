from crawler.entity import Entity
from selenium import webdriver
from time import sleep
from openpyxl import load_workbook
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class Service:
    def __init__(self):
        self.entity = Entity
    @staticmethod
    def get_sichug_url(dong,driver):
        # 정부24의 정부/지자체 운영사이트에서 검색해서 들어감
        # https://www.gov.kr/portal/orgSite?Mcode=11181
    @staticmethod
    def get_corona_page():
        pass