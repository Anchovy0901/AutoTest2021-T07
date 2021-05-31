import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import tool


class unitTest(unittest.TestCase):
    def test1(self):
        print("========【AT2021-T07-15-01】集团管理-应用中心-读取应用列表 =============")
        b = tool.login("13588631227", "Toby0901")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, './/span[contains(text(),"集团管理")]').click()
        print("成功进入首页-集团管理……")
        b.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[2]/ul[1]/li[2]/ul/li[3]/div').click()
        print("成功进入首页-集团管理-应用中心……读取列表")
        xxx = b.find_elements(By.XPATH,
                              '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div/div[3]/table/tbody/tr')
        for ele in xxx:
            itemText = ele.find_element_by_xpath('./td[2]/div/div').text + ": " + ele.find_element_by_xpath(
                './td[4]/div').text + " - " + ele.find_element_by_xpath('./td[6]/div').text
            print(itemText)

        # print("进入首页-我的应用-单位管理……")
        # tool.wait(1)
        # addUnitMsg = b.find_element_by_xpath('//div[@class="el-table__body-wrapper"]').text
        # print("进入首页-我的应用-单位管理-拉取信息-单位信息……")
        # self.assertEqual('单位信息', addUnitMsg)

    def test2(self):
        print("========【AT2021-T07-15-02】集团管理-应用中心-订阅 =============")
        b = tool.login("13588631227", "Toby0901")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, './/span[contains(text(),"集团管理")]').click()
        print("成功进入首页-集团管理……")
        b.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[2]/ul[1]/li[2]/ul/li[3]/div').click()
        print("成功进入首页-集团管理-应用中心……")
        b.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/div/button/span').click()
        print("成功进入首页-集团管理-应用中心-应用市场……")
        elements = b.find_elements(By.XPATH, '//div[@class="layout"]//div[@class="layout-box"]')
        for element in elements:
            itemText = element.find_element_by_xpath('./div//div[@class="layout-box__name"]').text
            print(itemText)  # 应用名称
            if (itemText == '万仪智联'):
                element.find_element_by_xpath('./div//button[1]').click()
                tool.wait(1)
                b.find_element_by_xpath('//div[@class="el-dialog__header"]/div/div[4]/button').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('应用订阅成功', addUnitMsg)

    def test3(self):
        print("========【AT2021-T07-15-03】集团管理-应用中心-退订 =============")
        b = tool.login("13588631227", "Toby0901")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, './/span[contains(text(),"集团管理")]').click()
        print("成功进入首页-集团管理……")
        b.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[2]/ul[1]/li[2]/ul/li[3]/div').click()
        print("成功进入首页-集团管理-应用中心……读取列表")
        xxx = b.find_elements(By.XPATH,
                              '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div/div[3]/table/tbody/tr')
        for ele in xxx:
            itemText = ele.find_element_by_xpath('./td[4]/div').text
            print(itemText)
            if (itemText == "万仪智联"):
                element = ele.find_element_by_xpath('./td[last()]//img')
                ActionChains(b).move_to_element(element).perform()
                tool.wait(1)
                b.find_element_by_xpath('//body/div[last()]/div[2]').click()
                b.find_element_by_xpath('//button/span[contains(text(),"确定")]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('退订成功', addUnitMsg)

    def test4(self):
        print("========【AT2021-T07-15-04】集团管理-应用中心-查看 =============")
        b = tool.login("13588631227", "Toby0901")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, './/span[contains(text(),"集团管理")]').click()
        print("成功进入首页-集团管理……")
        b.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[2]/ul[1]/li[2]/ul/li[3]/div').click()
        print("成功进入首页-集团管理-应用中心……读取列表")
        xxx = b.find_elements(By.XPATH,
                              '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div/div[3]/table/tbody/tr')
        for ele in xxx:
            itemText = ele.find_element_by_xpath('./td[4]/div').text
            print(itemText)
            if (itemText == "米画师"):
                element = ele.find_element_by_xpath('./td[last()]//img')
                ActionChains(b).move_to_element(element).perform()
                tool.wait(1)
                b.find_element_by_xpath('//body/div[last()]/div[1]').click()

        tool.wait(1)
        xxx = b.find_elements(By.XPATH,
                              '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/span')
        itemText = " "
        for ele in xxx:
            itemText += ele.text
        print(itemText)

    def test5(self):
        print("========【AT2021-T07-15-05】集团管理-应用中心-应用分发 =============")
        b = tool.login("13588631227", "Toby0901")
        print("成功登录……")
        # b.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/div[2]').click()
        b.find_element(By.XPATH, './/span[contains(text(),"集团管理")]').click()
        print("成功进入首页-集团管理……")
        b.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div[2]/ul[1]/li[2]/ul/li[3]/div').click()
        print("成功进入首页-集团管理-应用中心……读取列表")
        xxx = b.find_elements(By.XPATH, '/html/body/div/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div/div[3]/table/tbody/tr')
        for ele in xxx:
            itemText = ele.find_element_by_xpath('./td[4]/div').text
            print( itemText )
            if (itemText == "米画师"):
                element = ele.find_element_by_xpath('./td[last()]//img')
                ActionChains(b).move_to_element(element).perform()
                tool.wait(1)
                b.find_element_by_xpath('//body/div[last()]/div[3]').click()
                b.find_element_by_xpath('//*[@id="scroll"]/div[1]/div/div/div/div[1]/div/label/span/span').click()
                b.find_element_by_xpath('//button/span[contains(text(),"确 定")]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('分发成功', addUnitMsg)
