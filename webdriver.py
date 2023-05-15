from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

class WebDriver(Chrome):

    def __init__(self):
        __driver_options = ChromeOptions()

        # Unnecessary line if you're using regular Chrome
        __driver_options.binary_location = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
        
        __driver_options.add_argument('--start-maximized')
        __driver_options.add_argument('--incognito')

        # ChromeDriver 113.0.5672.63, supports Chrome version 113
        __driver_path = 'chromedriver_win32/chromedriver.exe'

        super().__init__(executable_path=__driver_path, options=__driver_options)