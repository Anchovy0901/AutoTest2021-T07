import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import shutil
def wait(times):
    time.sleep(times)


def setText(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/input").send_keys(value)
    return
def setText2(b, item, value):
    b.find_element_by_xpath("//div[@title='"+item+"']//input").send_keys(value)
    print(b)
    pass
    return
def setText3(b, item, value):
    ele = b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/input")
    ele.send_keys(Keys.CONTROL, 'a')
    ele.send_keys(value)
    wait(1)
    return

def setText5(b, item, value):
    ele = b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/textarea")
    ele.send_keys(Keys.CONTROL, 'a')
    ele.send_keys(value)
    wait(1)
    return

def setText4(b, item, value):
    ele = b.find_element_by_xpath("//label[@for='" + item + "']/../div//input")
    ele.send_keys(Keys.CONTROL, 'a')
    ele.send_keys(value)
    wait(1)
    return
def cleanText(b, item):
    ele = b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/input")
    ele.send_keys(Keys.CONTROL, 'a')
    ele.send_keys(Keys.DELETE)
    wait(1)
    return

def setTextArea(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/textarea").send_keys(value)
    return
def setNumber(b, item, value):
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

def setObject3(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/div/input").click()
    wait(1)
    unitElements = b.find_elements_by_xpath('//div[@class="ref-input__item"]')
    for element in unitElements:
        itemText = element.find_element_by_xpath('./span[@class="name"]').text
        if (itemText == value):
            element.click()
            wait(1)
    return

def setObject4(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/input").click()
    wait(1)
    if value == '启用':
        b.find_element_by_xpath('/html/body/div[last()]/div[1]/div[1]/ul/li[1]').click()
    else:
        b.find_element_by_xpath('/html/body/div[last()]/div[1]/div[1]/ul/li[2]').click()
    wait(2)
    return

def setX(b, item, value):
    ele = b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/input").click()
    wait(0.5)
    b.find_element_by_xpath('//li/span[contains(text(),"' + value + '")]').click()
    return

def setDict(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/input").click()
    wait(1)
    b.find_element_by_xpath(
        "//div[@x-placement='top-start']/div[1]/div[1]/ul/li/span[text()='" + value + "']").click()

    return
def setDict2(b, item, value):
    # b.find_element_by_xpath("//div[@title='" + item + "']//input").click()
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/input").click()
    wait(1)
    if value == "1":
        b.find_element_by_xpath("/html/body/div[11]/div[1]/div[1]/ul/li[1]").click()
    else:
        b.find_element_by_xpath("/html/body/div[11]/div[1]/div[1]/ul/li[2]").click()
    return


def setFile(b, item, value):
    b.find_element_by_xpath("//label[@for='" + item + "']/../div/div/div/div/input").send_keys(os.path.abspath(value))

    return


def login(account, password):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    b = webdriver.Chrome()
    b.set_window_size(1920, 1080)
    b.implicitly_wait(10)
    url = 'http://platform.assetcloud.org.cn/#/login'
    b.get(url)
    b.find_element_by_xpath("//input[@placeholder='请输入手机号码']").send_keys(account)
    b.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys(password)
    b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[5]/button/span').click()
    wait(5)
    return b



def joinItem(b,item1,item2,item3):
    b.find_element(By.XPATH, '//span[@alt="'+item1+'"]').click()
    b.find_element(By.XPATH, '//div[text()="'+item2+'"]').click()
    b.find_element(By.XPATH, '//div[@class="right"]/div[@class="content"]/span[text()="·'+item3+'"]').click()
    wait(5)
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
