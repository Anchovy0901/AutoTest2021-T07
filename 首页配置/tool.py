import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import shutil
def wait(times):
    time.sleep(times)

def login(account, password):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    b = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    b.set_window_size(1920, 1080)
    b.implicitly_wait(10)
    url = 'http://platform.assetcloud.org.cn/#/login'
    b.get(url)
    b.find_element_by_xpath("//input[@placeholder='请输入手机号码']").send_keys(account)
    b.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys(password)
    b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[5]/button/span').click()
    wait(1)
    return b

def joinItem(b,item1,item2):
    b.find_element(By.XPATH, '//span[@title="'+item1+'"]').click()
    wait(1)
    b.find_element(By.XPATH, '//span[@title="'+item2+'"]').click()
    wait(2)
    return

def setText(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/input").clear()
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/input").send_keys(value)
    return
def setSearch(b, value):
    b.find_element_by_xpath("//div[@class='search-input']//input").clear()
    b.find_element_by_xpath("//div[@class='search-input']//input").send_keys(value)
    return
def setText2(b, item, value):
    b.find_element_by_xpath("//div[@title='"+item+"']//input").send_keys(value)
    print(b)
    pass
    return
def setTextArea(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/textarea").send_keys(value)
    return
def setNumber(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/input").clear()
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/input").send_keys(value)
    return


def setCheck(b, item, value):
    if value == 1 or value == 2:
        b.find_element_by_xpath(
            "//label[@for='" + item + "']/../div/div/label[" + str(value) + "]/span[" + str(value) + "]").click()
    return


def setObject(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/div/input").send_keys(value)  # 行政区域
    wait(1)
    b.find_element_by_xpath(
        "//div[@x-placement='bottom-start']/div[1]/div[1]/ul/li/div/span[text()='" + value + "']").click()

    return
def setObject2(b, item, value):
    b.find_element_by_xpath("//div[@title='" + item + "']//input").send_keys(value)
    wait(3)
    b.find_element_by_xpath("//div[@class='ref-input__item']//span[text()='"+value+"']").click()
    return

def setDict(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/input").click()
    wait(1)
    b.find_element_by_xpath(
        "//div[@x-placement='bottom-start']/div[1]/div[1]/ul/li/span[text()='" + value + "']").click()

    return
def setDict2(b, item, value):
    b.find_element_by_xpath("//div[@title='" + item + "']//input").click()
    wait(5)
    b.find_element_by_xpath("//div[@class='el-select-dropdown el-popper']//span[text()='" + value + "']").click()

    return


def setFile(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/div/input").send_keys(os.path.abspath(value))

    return



def getRootPath():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\fcAutomatedTest"
def create(path):
    isExists=os.path.exists(getRootPath()+path)
    if not isExists:
        os.makedirs(getRootPath()+path)
        return getRootPath()+path
    else:
        return ""
def copyfile(path,folder):
    shutil.copy(path,folder)
def close(b):
    b.quit()
    return
