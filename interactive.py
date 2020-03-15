# coding=utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.pages.googlePage import GoogleHomePage

driver = webdriver.Chrome()
googleHomePage = GoogleHomePage(driver)
