# coding=utf-8
import time

from tests.framework.app import APP

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.pages.googlePage import GoogleHomePage

app = APP()

googleHomePage = GoogleHomePage(app)
