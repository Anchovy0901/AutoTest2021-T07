import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import tool


class unitTest(unittest.TestCase):
    def test1(self):
        print("========【AT2021-T07-8-01】首页-我的应用-单位管理-单位信息 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[1]').click()  # 我的应用-单位管理
        print("进入首页-我的应用-单位管理……")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//div[@class="container__body"]/div[1]/div[2]').text
        print("进入首页-我的应用-单位管理-拉取信息-单位信息……")
        self.assertEqual('单位信息', addUnitMsg)

    def test2(self):
        print("========【AT2021-T07-8-02】首页-我的应用-单位管理-部门人员 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[1]').click()  # 我的应用-单位管理
        print("进入首页-我的应用-单位管理……")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//div[@class="container__body"]/div[2]/div[2]').text
        print("进入首页-我的应用-单位管理-拉取信息-部门人员……")
        self.assertEqual('部门人员', addUnitMsg)

    def test3(self):
        print("========【AT2021-T07-8-03】首页-我的应用-单位管理-岗位管理 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[1]').click()  # 我的应用-单位管理
        print("进入首页-我的应用-单位管理……")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//div[@class="container__body"]/div[3]/div[2]').text
        print("进入首页-我的应用-单位管理-拉取信息-岗位管理……")
        self.assertEqual('岗位管理', addUnitMsg)

    def test4(self):
        print("========【AT2021-T07-8-04】首页-我的应用-单位管理-应用中心 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[1]').click()  # 我的应用-单位管理
        print("进入首页-我的应用-单位管理……")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//div[@class="container__body"]/div[4]/div[2]').text
        print("进入首页-我的应用-单位管理-拉取信息-应用中心……")
        self.assertEqual('应用中心', addUnitMsg)

    def test5(self):
        print("========【AT2021-T07-8-05】首页-我的应用-资产内控-资产业务 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[2]').click()  # 我的应用-资产内控
        print("进入首页-我的应用-资产内控……")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//div[@class="container__body"]/div[1]/div[2]').text
        print("进入首页-我的应用-资产内控-拉取信息-资产业务……")
        self.assertEqual('资产业务', addUnitMsg)

    def test6(self):
        print("========【AT2021-T07-8-06】首页-我的应用-资产内控-查询分析 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[2]').click()  # 我的应用-资产内控
        print("进入首页-我的应用-资产内控……")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//div[@class="container__body"]/div[2]/div[2]').text
        print("进入首页-我的应用-资产内控-拉取信息-查询分析……")
        self.assertEqual('查询分析', addUnitMsg)

    def test7(self):
        print("========【AT2021-T07-8-07】首页-我的应用-共享预约平台-业务中心 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[3]').click()  # 我的应用-资产内控
        print("进入首页-我的应用-共享预约平台……")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//div[@class="container__body"]/div[1]/div[2]').text
        print("进入首页-我的应用-共享预约平台-拉取信息-业务中心……")
        self.assertEqual('业务中心', addUnitMsg)

    def test8(self):
        print("========【AT2021-T07-8-08】首页-我的应用-共享预约平台-数据查询 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[3]').click()  # 我的应用-共享预约平台
        print("进入首页-我的应用-共享预约平台……")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//div[@class="container__body"]/div[2]/div[2]').text
        print("进入首页-我的应用-共享预约平台-拉取信息-数据查询……")
        self.assertEqual('数据查询', addUnitMsg)

    def test9(self):
        print("========【AT2021-T07-8-09】首页-我的应用-大仪共享管理-业务中心 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[4]').click()  # 我的应用-大仪共享管理
        print("进入首页-我的应用-大仪共享管理……")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//div[@class="container__body"]/div[1]/div[2]').text
        print("进入首页-我的应用-大仪共享管理-拉取信息-业务中心……")
        self.assertEqual('业务中心', addUnitMsg)

    def test10(self):
        print("========【AT2021-T07-8-10】首页-我的应用-大仪共享管理-数据查询 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[4]').click()  # 我的应用-大仪共享管理
        print("进入首页-我的应用-大仪共享管理……")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('//div[@class="container__body"]/div[2]/div[2]').text
        print("进入首页-我的应用-大仪共享管理-拉取信息-数据查询……")
        self.assertEqual('数据查询', addUnitMsg)

    def test11(self):
        print("========【AT2021-T07-8-11】首页-我的应用-自建应用 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, '//div[@class="buttons"]/div[3]').click()
        print("进入首页-我的应用……")
        b.find_element(By.XPATH, '//div[@class="app-list"]/div[5]').click()  # 我的应用-自建应用
        print("404 Not Found")
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath('/html/body/center[2]').text
        self.assertEqual('404 Not Found', addUnitMsg)