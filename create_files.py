from bs4 import BeautifulSoup as bs # pip3 install beautifulsoup4
import os

github_repo = None

def get_files(source):
    """
    Get the names of the files listed in page source and create them in the specified GitHub repo.
    
    Args:
        source (str): Page source of the Holberton School intranet (current project).
    """
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path to the target GitHub repository
    relative_repo_path = None
    target_repo_path = None
    
    directory = None
    soup = bs(source, "html.parser")
    group_list = soup.select("div.list-group-item")
    
    for element in group_list:
        children_of_group_list = element.select("li")
        for li_tag in children_of_group_list:
            split_li_tag = li_tag.get_text().split()
            
            for elem in split_li_tag:
                if "GitHub" in elem:
                    github_repo = split_li_tag[-1]
                    relative_repo_path = "../" + github_repo
                    target_repo_path = os.path.abspath(os.path.join(script_dir, relative_repo_path))
                if "Directory" in elem:
                    directory = split_li_tag[-1]
                if "File:" in elem:
                    if directory is not None:
                        if relative_repo_path is not None:
                            create_file(split_li_tag[-1], directory, target_repo_path)
                        else:
                            print("Please specify repository path")
                    else:
                        if relative_repo_path is not None:
                            create_file(split_li_tag[-1], target_repo_path)
                        else:
                            print("Please specify repository path")
                        
    return github_repo


def create_file(file, directory=None, target_repo_path=None):
    """
    Create a file in the specified directory within the target GitHub repository.
    
    Args:
        file (str): Filename.
        directory (str): Directory name (optional).
        target_repo_path (str): The path to the target GitHub repository.
        
    Return:
        None if file already exists in the target directory.
    """
    if target_repo_path is None:
        target_repo_path = os.getcwd()

    # Construct the full directory path
    if directory is not None:
        full_dir = os.path.join(target_repo_path, directory)
        os.makedirs(full_dir, exist_ok=True)
        file_path = os.path.join(full_dir, file)
    else:
        file_path = os.path.join(target_repo_path, file)
    
    readme_file = os.path.join(full_dir, "README.md")
    print(f"Creating file at: {file_path}")
    
    if os.path.exists(file_path):
        return None
    
    if not os.path.exists(readme_file):
        with open(readme_file, "w", encoding="utf-8") as file:
            file.write(f"<h1 align='center'>{directory}</h1>")
        print(f"{readme_file} created successfully.")
    
    with open(file_path, "w", encoding="utf-8"):
        pass