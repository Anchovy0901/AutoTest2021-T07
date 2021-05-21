import time
import unittest

from selenium.webdriver.common.by import By

import HTMLTestReport
import tool

class unitTest(unittest.TestCase):
    # 登录-账号不存在
    def test1(self):
        '''登录-账号不存在测试'''
        print("========【AT2021-T07-12-1】登录-账号不存在测试 =============")
        b = tool.login("1885774837", "xr952343147")
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('账号不存在!', addUnitMsg)
        tool.close(b)

    # 登录-密码错误
    def test2(self):
        '''登录-密码错误测试'''
        print("========【AT2021-T07-12-2】登录-密码错误测试 =============")
        b = tool.login("18857748370", "xr")
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('账号或密码不正确!', addUnitMsg)
        tool.close(b)

    # 登录-注销
    def test3(self):
        '''登录-注销测试'''
        print("========【AT2021-T07-12-3】登录-注销测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(2)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(1)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[4].click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('注销成功', addUnitMsg)
        tool.close(b)

    # 首页配置-设置平台模板
    def test4(self):
        '''首页配置-设置平台模板测试'''
        print("========【AT2021-T07-10-1】首页配置-设置平台模板测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[2].click()
        tool.wait(2)
        b.find_element(By.XPATH, '//*[@role="tabpanel"]/div[1]/div[1]/div[1]/div[1]').click()
        tool.wait(2)
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[2]/button/span').click()
        tool.wait(2)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 首页配置-搜索存在模板
    def test5(self):
        '''首页配置-搜索存在模板试'''
        print("========【AT2021-T07-10-2】首页配置-搜索存在模板测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[2].click()
        tool.wait(2)
        tool.setSearch(b,"空模板")
        tool.wait(2)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 首页配置-搜索不存在模板
    def test6(self):
        '''首页配置-搜索不存在模板测试'''
        print("========【AT2021-T07-10-3】首页配置-搜索不存在模板测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[2].click()
        tool.wait(2)
        tool.setSearch(b,"啥")
        tool.wait(2)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 首页配置-自定义模板
    def test7(self):
        '''首页配置-自定义模板测试'''
        print("========【AT2021-T07-10-4】首页配置-自定义模板测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[2].click()
        tool.wait(2)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[4]/button/span').click()
        tool.wait(1)
        b.find_element_by_xpath("//div[contains(text(),'待办事项')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//div[contains(text(),'资产卡片')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//div[contains(text(),'预警按钮')]").click()
        tool.wait(2)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/button[2]/span').click()
        tool.wait(2)
        b.find_element_by_xpath("//span[contains(text(),'新增')]").click()
        tool.wait(1)
        tool.setText(b,'name',"自定义模板1")
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('添加成功', addUnitMsg)
        tool.close(b)

    # 首页配置-设置自定义模板
    def test8(self):
        '''首页配置-设置自定义模板测试'''
        print("========【AT2021-T07-10-5】首页配置-设置自定义模板测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[2].click()
        tool.wait(2)
        b.find_element(By.XPATH, "//div[contains(text(),'自定义模板1')]").click()
        tool.wait(2)
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[2]/button/span').click()
        tool.wait(2)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 首页配置-自定义模板
    def test9(self):
        '''首页配置-自定义模板测试'''
        print("========【AT2021-T07-10-6】首页配置-重复自定义模板测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[2].click()
        tool.wait(2)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[4]/button/span').click()
        tool.wait(1)
        b.find_element_by_xpath("//div[contains(text(),'待办事项')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//div[contains(text(),'资产卡片')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//div[contains(text(),'预警按钮')]").click()
        tool.wait(2)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/button[2]/span').click()
        tool.wait(2)
        b.find_element_by_xpath("//span[contains(text(),'新增')]").click()
        tool.wait(1)
        tool.setText(b,'name',"自定义模板1")
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('模板已存在', addUnitMsg)
        tool.close(b)

    # 首页配置-删除自定义模板
    def test10(self):
        '''首页配置-删除自定义模板测试'''
        print("========【AT2021-T07-10-7】首页配置-删除自定义模板测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[2].click()
        tool.wait(2)
        b.find_element(By.XPATH, '//div[@class="tree defaultClick"]/div[1]/div[2]').click()
        tool.wait(2)
        b.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('删除成功', addUnitMsg)
        tool.close(b)



