from seleniumbase import SB  # pip3 install seleniumbase
from dotenv import load_dotenv
# from create_repo import create_repo
from create_files import get_files
from parse_text import parse
import os
import sys
from try_to_find_chrome import find_chrome

# try to find chrome
chrome_path = find_chrome()

if chrome_path is None:
    print(f"Could not find Google Chrome. \nIf you don't have it, please install it, but if you do have it, try running the Bot again with >>> python3(or python) main.py <curriculum you want> <full path to chrome.exe on your computer>")
    sys.exit(1)

# Load environment variables from .env.local
try:
    load_dotenv(dotenv_path='.env.local')
except Exception as e:
    print(f"Error loading environment variables: {e}")
    sys.exit(1)

# Access variables
password = os.getenv('STUDENT_PASSWORD')
student_email = os.getenv('STUDENT_EMAIL')

# Ensure environment variables are set
if not password or not student_email:
    print("Error: Missing student email or password in environment variables.")
    sys.exit(1)

url = "https://intranet.hbtn.io/"  # intranet url
github_repo = None

# Check for command-line arguments
if len(sys.argv) < 3:
    print("Error: Curriculum argument missing.\n")
    print("Example: \npython3 main.py part 3")
    sys.exit(1)

curriculum = sys.argv[1] + " " + sys.argv[2]

"""SB Manager using UC Mode for evading bot-detection."""
try:
    with SB(uc=True, binary_location=chrome_path) as sb:
        try:
            sb.uc_open_with_reconnect(url, reconnect_time=10)
        except Exception as e:
            print(f"Error opening URL: {e}")
            sys.exit(1)

        try:
            sb.uc_gui_click_captcha()
        except Exception as e:
            print(f"Error handling CAPTCHA: {e}")
            sys.exit(1)

        sb.set_messenger_theme(location="top_left")
        sb.post_message("SeleniumBase wasn't detected", duration=5)

        try:
            sb.type("input#user_login", student_email)
            sb.type("input#user_password", password)
            sb.click("input.btn.btn-primary")
        except Exception as e:
            print(f"Error during login: {e}")
            sys.exit(1)

        sb.post_message("signed in", duration=5)

        try:
            sb.click("div#student-switch-curriculum-dropdown")
            sb.click(f"span:contains('{parse(curriculum)}')")
        except Exception as e:
            print(f"Error selecting curriculum: {e}")
            sys.exit(1)

        try:
            sb.click("div.project-actions")
        except Exception as e:
            print(f"Error navigating to project actions: {e}")
            sys.exit(1)

        try:
            github_repo = get_files(sb.get_page_source())
        except Exception as e:
            print(f"Error getting files: {e}")
            sys.exit(1)

        sb.sleep(2)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
