import test_OpenBrowser,test_NavigateURL

import logging

# chrome_path ="/Users/Shared/Jenkins/Home/jobs/Python/chromedriver 4"
chrome_path = "chromedriver 4"


def test_openBrowser():
    logging.info("opening browser")
    test_OpenBrowser.openBrowser(chrome_path)
    logging.info("closinging browser")

def test_newURL():
    url1 = "https://www.google.com"
    test_NavigateURL.openBrowser(chrome_path,url1)









