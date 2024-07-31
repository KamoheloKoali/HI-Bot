
from seleniumbase import SB
from dotenv import load_dotenv
import os

# Load environment variables from .env.local
load_dotenv(dotenv_path='.env.local')

# Access variables
db_password = os.getenv('DB_PASSWORD')
secret_key = os.getenv('SECRET_KEY')

url = "https://intranet.hbtn.io"# Replace with the actual URL

"""SB Manager using UC Mode for evading bot-detection."""
text = ''
with SB(uc=True, test=True, demo=True) as sb:
    sb.uc_open_with_reconnect(url, reconnect_time=2)
    sb.uc_gui_click_captcha()
    # sb.assert_element("img#captcha-success", timeout=3)
    sb.set_messenger_theme(location="top_left")
    sb.post_message("SeleniumBase wasn't detected", duration=5)
    sb.type("input#user_login", "email")
    sb.type("input#user_password", "pass")
    sb.click("input.btn.btn-primary")
    sb.post_message("signed in", duration=5)
    text = sb.get_text("h3#student-home-current-project-title")
    sb.post_message("text retrieved", duration=5)


print(text)

    
