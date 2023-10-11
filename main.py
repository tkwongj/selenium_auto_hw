from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

URL = "https://sparxmaths.com/"
main_page_url = "https://sparxmaths.uk/student/homework"

driver.get(main_page_url)
driver.maximize_window()

while True:
    driver.implicitly_wait(2)
    if driver.find_elements("xpath", "//div[text()[contains(., 'Hey')]]"):
        print("hello")
        break

xp_boost = driver.find_elements("xpath", "//span[text()='XP Boost']")
xp_boost[0].click()

driver.implicitly_wait(3)

exercises = driver.find_elements(
    "xpath", "//button[./div/div[text()[contains(., 'XP Boost for')]]]"
)
current_exercise = exercises[0]
exercises[0].click()
driver.implicitly_wait(2)
curr_task = current_exercise.find_elements(
    "xpath", "//a[@href[contains(., 'student/package')]]"
)
curr_task[0].click()
time.sleep(2)
driver.save_screenshot("image.png")
