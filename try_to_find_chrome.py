import os
import platform
import shutil

def find_chrome_binary():
    system = platform.system()
    chrome_paths = []

    if system == "Windows":
        # Try to find Chrome via registry (requires winreg module)
        try:
            import winreg as reg
            reg_path = r"Software\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
            with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, reg_path) as key:
                chrome_paths.append(reg.QueryValue(key, None))
        except ImportError:
            pass
        except FileNotFoundError:
            pass
        
        # Other common paths on Windows
        chrome_paths.extend([
            os.path.join(os.getenv("LOCALAPPDATA", ""), "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(os.getenv("PROGRAMFILES", ""), "Google", "Chrome", "Application", "chrome.exe"),
            os.path.join(os.getenv("PROGRAMFILES(X86)", ""), "Google", "Chrome", "Application", "chrome.exe")
        ])

    elif system == "Darwin":  # macOS
        # Common macOS Chrome paths
        chrome_paths.append("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

    elif system == "Linux":
        # Common Linux paths
        chrome_paths.extend([
            "/usr/bin/google-chrome",
            "/usr/local/bin/google-chrome",
            "/usr/bin/chromium-browser",
            "/usr/local/bin/chromium-browser",
        ])

    # Check each path to see if it exists
    for path in chrome_paths:
        if os.path.exists(path):
            return path

    # If no paths worked, try using shutil.which as a last resort
    return shutil.which("chrome") or shutil.which("google-chrome") or shutil.which("chromium-browser")

# Example usage
def find_chrome():
    chrome_path = find_chrome_binary()
    if chrome_path:
        print(f"Chrome binary found at: {chrome_path}")
        return chrome_path
    else:
        print("Chrome binary not found.")
        return None
