from seleniumbase import SB # pip3 install seleniumbase
from dotenv import load_dotenv
import os

# Load environment variables from .env.local
load_dotenv(dotenv_path='.env.local')

# Access variables
github_password = os.getenv('GITHUB_PASSWORD')
github_email = os.getenv('GITHUB_EMAIL')

def create_repo(repo_name=None):
    """
    create a repository on github
    
    Args:
        repo_name (str): name of the repository to create
    """
    
    url = "https://github.com/" # github url
    repositories_url = url
    
    """SB Manager using UC Mode for evading bot-detection."""
    with SB(uc=True, demo=True) as sb:
        sb.uc_open_with_reconnect(url, reconnect_time=10)
        sb.set_messenger_theme(location="top_left")
        sb.click("div.position-relative.HeaderMenu-link-wrap.d-lg-inline-block")
        sb.type("input#login_field", github_email)
        sb.type("input#password", github_password)
        sb.click("input.btn.btn-primary.btn-block.js-sign-in-button")
        sb.assert_text("Dashboard", "span.AppHeader-context-item-label")
        sb.post_message("signed in", duration=4)
        sb.click("a[href='/new']")
        sb.type("input.UnstyledTextInput-sc-14ypya-0.cDLBls", repo_name)
        sb.assert_text("Create repository", "button.types__StyledButton-sc-ws60qy-0.lkyss")
        sb.post_message("repository created", duration=4)
        sb.sleep(2)