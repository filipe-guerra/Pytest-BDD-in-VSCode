import os, time
from selenium import webdriver

class APP:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def take_screenshot(self, folder):
        name = ''
        name = folder.rsplit('/', 1)[1] if '/' in folder else folder
        
        save_location = "tests/report/screenshots/{}/".format(folder)
        path = os.path.abspath(save_location)
        if not os.path.exists(path):
            os.makedirs(path)
        timestr = time.strftime("%Y%m%d_%H-%M-%S")
        full_path = '{}/{} {}.png'.format(path, name, timestr)

        self.driver.set_window_size(1368, 768)
        time.sleep(0.3)
        self.driver.get_screenshot_as_file(full_path)
        self.driver.maximize_window()
        # return full_path
