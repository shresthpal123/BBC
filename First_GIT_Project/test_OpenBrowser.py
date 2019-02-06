from selenium import webdriver


def openBrowser(chrome_path):
    global driver
    driver=webdriver.Chrome(chrome_path)