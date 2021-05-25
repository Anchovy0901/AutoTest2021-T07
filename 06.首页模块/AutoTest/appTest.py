import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import tool


class unitTest(unittest.TestCase):
    def test1(self):
        print("========【AT2021-T07-6-01】首页-待办-查看工单 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        # b.find_element(By.XPATH, '//svg[@id="icon-shouye1"]').click()
        # b.find_element(By.XPATH, '//svg[@id="icon-xiaoxi1"]').click()

        b.find_element(By.XPATH, '//*[@id="workSpace"]/div/div[1]/div/div[2]/div/div/div/div/div[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]').text
        self.assertEqual('跳转成功', addUnitMsg)

    def test2(self):
        print("========【AT2021-T07-6-02】首页-个人信息展示 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        # b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        # b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//*[@id="workSpace"]/div/div[7]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]').text
        print("登录者：" + addUnitMsg)
        self.assertEqual('豆浆汤面宇宙青年旅舍', addUnitMsg)

    def test3(self):
        print("========【AT2021-T07-6-03】首页-邀请成员 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        tool.wait(1)

        # b.find_element_by_xpath('span[contains(text()="邀请")]').click()
        b.find_element_by_xpath('//*[@id="invitation"]/div/div[1]/div[2]/p[3]/span').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        print(addUnitMsg)
        self.assertEqual('邀请链接已复制!可以去钉钉，QQ，微信粘贴', addUnitMsg)

    def test4(self):
        print("========【AT2021-T07-6-04】首页-应用中心跳转=============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        # b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        # b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        b.find_element_by_xpath(
            '//*[@id="invitation"]/div/div[3]/div[2]/p[2]/span').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//*[@id="tab-0"]/div/i').text
        self.assertEqual('应用中心', addUnitMsg)

    def test5(self):
        print("========【AT2021-T07-6-05】首页-资产卡片-查看更多 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="indexcard"]/div/div[1]/p').click()
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertNotEqual('请求出错', addUnitMsg)

