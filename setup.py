from setuptools import setup, find_packages

setup(
    name="pcslib",
    version="0.1",
    packages=find_packages(),  # finds the 'pcslib' folder automatically
    description="RPA Wrapper for WinForms version of PCS",
    author="Kevin Lubbers",
    install_requires=[
        "pyautogui",
        "pygetwindow",
        "pyperclip"
    ],
)