# coding=utf-8
import time

from tests.framework.fixture import APP as app

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.pages.googlePage import GoogleHomePage

googleHomePage = GoogleHomePage(app.driver)
