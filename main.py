
from seleniumbase import SB # pip3 install seleniumbase
from dotenv import load_dotenv
from create_repo import create_repo
from create_files import get_files
import os

# Load environment variables from .env.local
load_dotenv(dotenv_path='.env.local')

# Access variables
password = os.getenv('STUDENT_PASSWORD')
student_email = os.getenv('STUDENT_EMAIL')

url = "https://intranet.hbtn.io/" # intranet url
github_repo = None
"""SB Manager using UC Mode for evading bot-detection."""
with SB(uc=True, demo=True) as sb:
    sb.uc_open_with_reconnect(url, reconnect_time=10)
    sb.uc_gui_click_captcha()
    sb.set_messenger_theme(location="top_left")
    sb.post_message("SeleniumBase wasn't detected", duration=5)
    sb.type("input#user_login", student_email)
    sb.type("input#user_password", password)
    sb.click("input.btn.btn-primary")
    sb.post_message("signed in", duration=5)
    sb.click("div#student-switch-curriculum-dropdown")
    sb.click("a[href='/curriculums/382/observe/43898']") 
    sb.click("div.project-actions")
    github_repo = get_files(sb.get_page_source())
    sb.sleep(2)

    
# if github_repo is not None:
#     create_repo(github_repo)