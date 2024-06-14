from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def open_browser():
    driverService = webdriver.ChromeService(executable_path=r"..\webdriver\chromedriver.exe", port=2190)
    driver = webdriver.Chrome(service=driverService)
    driver.get("http://www.baidu.com")

    driver.find_element(By.ID, "kw").send_keys("selenium")
    driver.find_element(By.ID, "su").click()
    sleep(3)
    driver.quit()


if __name__ == '__main__':
    open_browser()
