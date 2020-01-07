from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def get_page(url,option={}):
    SERVICE_ARGS = ['--load-images=false', '--disk-cache=true', '--ignore-ssl-errors=true']
    broswer=webdriver.PhantomJS(service_args=SERVICE_ARGS)
    broswer.set_page_load_timeout(30)
    wait = WebDriverWait(broswer, 30)
    try:
        broswer.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div:nth-child(1) > table')))
        return broswer.page_source
    except TimeoutException:
        print("超时")
        broswer.execute_script('window.stop()')
    finally:
        broswer.close()