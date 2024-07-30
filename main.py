import requests
from seleniumbase import Driver

url = "https://intranet.hbtn.io/projects/2348"

driver = Driver(uc=True)
try:
    driver.get(url)
    driver.sleep(4)
finally:
    driver.quit()