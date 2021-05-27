import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import tool


class unitTest(unittest.TestCase):
    def test1(self):
        print("========【AT2021-T07-7-01】首页-消息-待办-查看工单 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr[1]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]').text
        self.assertEqual('跳转成功', addUnitMsg)

