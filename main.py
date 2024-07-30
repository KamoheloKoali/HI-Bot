
from seleniumbase import SB # pip3 install seleniumbase

url = "https://intranet.hbtn.io"# Replace with the actual URL

student_email = "enter email" # actual stduent email

password = "password" # password 

"""SB Manager using UC Mode for evading bot-detection."""
text = ''
with SB(uc=True, test=True, demo=True) as sb:
    sb.uc_open_with_reconnect(url, reconnect_time=2)
    sb.uc_gui_click_captcha() sb.set_messenger_theme(location="top_left")
    sb.post_message("SeleniumBase wasn't detected", duration=5)
    sb.type("input#user_login", student_email)
    sb.type("input#user_password", password)
    sb.click("input.btn.btn-primary")
    sb.post_message("signed in", duration=5)
    text = sb.get_text("h3#student-home-current-project-title")
    sb.post_message("text retrieved", duration=5)


print(text)

    
