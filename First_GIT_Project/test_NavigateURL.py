from selenium import webdriver
import logging

def openBrowser(chrome_path,url1):
    global driver
    driver=webdriver.Chrome(chrome_path)
    # driver.get("https://www.softwaretestingmaterial.com/how-to-capture-full-page-screenshot-using-selenium-webdriver/")
    driver.get(url1)
    pgTitle = driver.title
    logging.info("closinging browser")
    driver.quit()