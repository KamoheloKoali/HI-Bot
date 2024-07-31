
from seleniumbase import SB # pip3 install seleniumbase
from dotenv import load_dotenv
import os

# Load environment variables from .env.local
load_dotenv(dotenv_path='.env.local')

# Access variables
password = os.getenv('PASSWORD')
student_email = os.getenv('EMAIL')

url = "https://intranet.hbtn.io/projects/current" # Replace with the actual URL

"""SB Manager using UC Mode for evading bot-detection."""
# text = ''
with SB(uc=True, demo=True) as sb:
    sb.uc_open_with_reconnect(url, reconnect_time=10)
    sb.uc_gui_click_captcha()
    sb.set_messenger_theme(location="top_left")
    sb.post_message("SeleniumBase wasn't detected", duration=5)
    sb.type("input#user_login", student_email)
    sb.type("input#user_password", password)
    sb.click("input.btn.btn-primary")
    sb.post_message("signed in", duration=5)
    # text = sb.get_text("h3#student-home-current-project-title")
    # sb.post_message("text retrieved", duration=5)
    sb.click("div#student-switch-curriculum-dropdown")
    sb.click("a[href='/curriculums/365/observe/37383']") 
    sb.click("span[title='ES6 data manipulation']")
    # sb.assert_element("h3#student-home-current-project-title")
    sb.sleep(4)


# print(text)

    
