from bs4 import BeautifulSoup as bs # pip3 install beautifulsoup4
import os

def get_files(source):
    """
    get the names of the files listed in page source
    
    Args:
        source (str): page source of the holberton school intranet (current project)
    """
    github_repo = None
    soup = bs(source, "html.parser")
    group_list = soup.select("div.list-group-item")
    for element in group_list:
        children_of_group_list = element.select("li")
        for li_tag in children_of_group_list:
            split_li_tag = li_tag.get_text().split()
            
            for elem in split_li_tag:
                # print(elem)
                if "GitHub" in elem:
                    github_repo = split_li_tag[-1]
                    print(github_repo)
                if "File:" in elem:
                    create_file(split_li_tag[-1])
    return github_repo

def create_file(file):
    """
    create file
    
    Args:
        files (list): filename
        
    Return:
        None if file already exists in current dir
    """
    if os.path.exists(file):
        return None
    
    with open(file, "w", encoding="utf-8") as file:
        pass