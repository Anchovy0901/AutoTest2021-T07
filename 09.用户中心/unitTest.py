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

    # 切换边栏-切换至左方
    def test11(self):
        '''切换边栏-切换至左方测试'''
        print("========【AT2021-T07-11-1】切换边栏-切换至左方测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[3].click()
        tool.wait(2)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 切换边栏-切换至上方
    def test12(self):
        '''切换边栏-切换至上方测试'''
        print("========【AT2021-T07-11-2】切换边栏-切换至上方测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[3].click()
        tool.wait(2)
        b.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[3].click()
        tool.wait(2)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 用户中心-修改信息
    def test13(self):
        '''用户中心-修改信息测试'''
        print("========【AT2021-T07-9-1】用户中心-修改信息 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(2)
        b.find_element_by_xpath(
            "//button[@class='el-button el-button--text']//span[text()='修改信息']").click()
        tool.wait(1)
        tool.setText(b, 'name', "Toby")
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('修改用户信息成功', addUnitMsg)
        tool.close(b)

    # 用户中心-修改密码-修改失败（原密码错误）
    def test14(self):
        '''用户中心-修改密码-修改失败（原密码错误）测试'''
        print("========【AT2021-T07-9-2】用户中心-修改密码-修改失败（原密码错误） =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(2)
        b.find_element_by_xpath(
            "//button[@class='el-button el-button--text']//span[text()='修改密码']").click()
        tool.wait(1)
        tool.setText(b, 'pass', "xr1234")
        tool.setText(b, 'newPass', "xr952343147")
        tool.setText(b, 'checkPass', "xr952343147")
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[3]/span/button[2]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('原密码不正确!', addUnitMsg)
        tool.close(b)

    # 用户中心-修改密码-修改失败（两次密码不一致）
    def test15(self):
        '''用户中心-修改密码-修改失败（两次密码不一致）测试'''
        print("========【AT2021-T07-9-3】用户中心-修改密码-修改失败（两次密码不一致） =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(2)
        b.find_element_by_xpath(
            "//button[@class='el-button el-button--text']//span[text()='修改密码']").click()
        tool.wait(1)
        tool.setText(b, 'pass', "xr952343147")
        tool.setText(b, 'newPass', "xr1234")
        tool.setText(b, 'checkPass', "xr12345")
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[3]/span/button[2]/span').click()
        tool.wait(1)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 用户中心-修改密码-修改成功
    def test16(self):
        '''用户中心-修改密码-修改成功测试'''
        print("========【AT2021-T07-9-4】用户中心-修改密码-修改成功 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(2)
        b.find_element_by_xpath(
            "//button[@class='el-button el-button--text']//span[text()='修改密码']").click()
        tool.wait(1)
        tool.setText(b, 'pass', "xr952343147")
        tool.setText(b, 'newPass', "xr952343147")
        tool.setText(b, 'checkPass', "xr952343147")
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div[3]/span/button[2]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('修改密码成功', addUnitMsg)
        tool.close(b)

    # 用户中心-设为主单位
    def test17(self):
        '''用户中心-设为主单位测试'''
        print("========【AT2021-T07-9-5】用户中心-设为主单位 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(2)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr/td[1]/div/label/span/span').click()
        tool.wait(1)
        b.find_element_by_xpath(
            "//button[@class='el-button el-button--text']//span[text()='设为主单位']").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('设置主单位成功', addUnitMsg)
        tool.close(b)

    # 用户中心-查看申请
    def test18(self):
        '''用户中心-查看申请测试'''
        print("========【AT2021-T07-9-6】用户中心-查看申请 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(2)
        b.find_element_by_xpath(
            "//button[@class='el-button el-button--text']//span[text()='查看申请']").click()
        tool.wait(2)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 用户中心-加入单位
    def test19(self):
        '''用户中心-加入单位测试'''
        print("========【AT2021-T07-9-7】用户中心-加入单位 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(2)
        b.find_element_by_xpath(
            "//button[@class='el-button el-button--text']//span[text()='加入单位']").click()
        tool.wait(1)
        tool.setText(b, 'tenantName', "12")
        tool.wait(1)
        b.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span').click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('申请成功，等待审核', addUnitMsg)
        tool.close(b)

    # 用户中心-加入单位（重复申请）
    def test20(self):
        '''用户中心-加入单位（重复申请）测试'''
        print("========【AT2021-T07-9-8】用户中心-加入单位（重复申请） =============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(2)
        b.find_element_by_xpath(
            "//button[@class='el-button el-button--text']//span[text()='加入单位']").click()
        tool.wait(1)
        tool.setText(b, 'tenantName', "豪哥")
        tool.wait(1)
        b.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span').click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请勿重复申请', addUnitMsg)
        tool.close(b)

    # 用户中心-取消申请
    def test21(self):
        '''用户中心-取消申请测试'''
        print("========【AT2021-T07-9-9】用户中心-取消申请=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(2)
        b.find_element_by_xpath(
            "//button[@class='el-button el-button--text']//span[text()='查看申请']").click()
        tool.wait(2)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()
        tool.wait(2)
        b.find_element_by_xpath(
            "//button[@class='el-button el-button--text']//span[text()='取消申请']").click()
        tool.wait(2)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 用户中心-搜索
    def test21(self):
        '''用户中心-搜索测试'''
        print("========【AT2021-T07-9-10】用户中心-搜索=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(2)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(2)
        tenantElement = b.find_element_by_xpath("//input[@placeholder='请输入搜索内容']")
        tenantElement.send_keys('豪哥')
        tool.wait(2)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span/i/img').click()
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)