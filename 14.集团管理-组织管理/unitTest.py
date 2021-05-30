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
    def test22(self):
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

    # 集团管理-组织管理-创建下级节点（重复）
    def test23(self):
        '''集团管理-组织管理-创建下级节点（重复）测试'''
        print("========【AT2021-T07-14-1】集团管理-组织管理-创建下级节点（重复）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="line"]/div/div[2]/div[2]/div/div').click()
        tool.wait(1)
        tool.setText(b, 'groupName', "我DioToby敢吃屎")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/form/div[4]/div/div/div/input').click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'我DioToby敢吃屎')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('请勿重复添加', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-创建下级节点（成功）
    def test24(self):
        '''集团管理-组织管理-创建下级节点（成功）测试'''
        print("========【AT2021-T07-14-2】集团管理-组织管理-创建下级节点（成功）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="line"]/div/div[2]/div[2]/div/div').click()
        tool.wait(1)
        tool.setText(b, 'groupName', "我DioToby敢吃屎")
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[2]/div/form/div[4]/div/div/div/input').click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'我Toby敢吃屎')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('创建成功', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-合并集团（失败）
    def test25(self):
        '''集团管理-组织管理-合并集团（失败）测试'''
        print("========【AT2021-T07-14-3】集团管理-组织管理-合并集团（失败）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'合并集团')]").click()
        tool.wait(1)
        tool.setText(b, 'groupName', "吃屎不及时")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'合并集团')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div/div[3]/span/button/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('无法合并加入本身！', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-合并集团（成功）
    def test25(self):
        '''集团管理-组织管理-合并集团（成功）测试'''
        print("========【AT2021-T07-14-4】集团管理-组织管理-合并集团（成功）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'合并集团')]").click()
        tool.wait(1)
        tool.setText(b, 'groupName', "吃屎不及时")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'合并集团')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div/div[3]/span/button/span').click()
        tool.wait(5)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 集团管理-组织管理-编辑信息
    def test25(self):
        '''集团管理-组织管理-编辑信息测试'''
        print("========【AT2021-T07-14-5】集团管理-组织管理-编辑信息=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'编辑信息')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('修改节点信息成功', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-分配单位
    def test26(self):
        '''集团管理-组织管理-分配单位测试'''
        print("========【AT2021-T07-14-6】集团管理-组织管理-分配单位=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'分配单位')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('分配成功', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-调整组织
    def test27(self):
        '''集团管理-组织管理-调整组织测试'''
        print("========【AT2021-T07-14-7】集团管理-组织管理-调整组织=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div[3]/div/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[6]/div/div/span/div/div/img').click()
        b.find_element_by_xpath("//button[contains(text(),'调整组织')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div[3]/div/div/div[2]/div/div[2]/div/div/div/input').click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'吃屎不及时')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div[3]/div/div/div[2]/div/div[3]/span/button[1]/span').click()
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('调整成功', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-移出组织
    def test28(self):
        '''集团管理-组织管理-移出组织测试'''
        print("========【AT2021-T07-14-8】集团管理-组织管理-移出组织=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div[3]/div/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[6]/div/div/span/div/div/img').click()
        b.find_element_by_xpath("//button[contains(text(),'移出组织')]").click()
        tool.wait(1)
        b.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[2]/span').click()
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 集团管理-组织管理-初始化排序
    def test29(self):
        '''集团管理-组织管理-初始化排序测试'''
        print("========【AT2021-T07-14-9】集团管理-组织管理-初始化排序=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织维护')]").click()
        tool.wait(2)
        b.find_element_by_xpath("//span[contains(text(),'初始化排序')]").click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('初始化排序成功', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-删除组织
    def test30(self):
        '''集团管理-组织管理-删除组织测试'''
        print("========【AT2021-T07-14-10】集团管理-组织管理-删除组织=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织维护')]").click()
        tool.wait(2)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr[1]/td[3]/div/div/i').click()
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr[2]/td[1]/div/label/span/span').click()
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[2]/td[5]/div/div/span/div/div/img').click()
        tool.wait(1)
        b.find_element_by_xpath(
            "//div[contains(text(),'删除')]").click()
        tool.wait(1)
        b.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/button[2]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('删除成功', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-组织关系导入（下载模板）
    def test31(self):
        '''集团管理-组织管理-组织关系导入（下载模板）测试'''
        print("========【AT2021-T07-14-11】集团管理-组织管理-组织关系导入（下载模板）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织维护')]").click()
        tool.wait(2)
        b.find_element_by_xpath("//span[contains(text(),'组织关系导入')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'下载模板')]").click()
        tool.wait(5)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 集团管理-组织管理-组织关系导入（批量导入）
    def test32(self):
        '''集团管理-组织管理-组织关系导入（批量导入）测试'''
        print("========【AT2021-T07-14-12】集团管理-组织管理-组织关系导入（批量导入）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织维护')]").click()
        tool.wait(2)
        b.find_element_by_xpath("//span[contains(text(),'组织关系导入')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'批量导入')]").click()
        tool.wait(10)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 集团管理-组织管理-组织查看
    def test33(self):
        '''集团管理-组织管理-组织查看测试'''
        print("========【AT2021-T07-14-13】集团管理-组织管理-组织查看）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="line"]/div/div[2]/div[2]/span/div').click()
        b.find_element_by_xpath('//*[@id="el-popover-9052"]/div[1]/label[2]/span[1]/span').click()
        b.find_element_by_xpath('//*[@id="el-popover-9052"]/div[1]/label[3]/span[1]/span').click()
        tool.wait(2)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 集团管理-组织管理-组织搜索
    def test34(self):
        '''集团管理-组织管理-组织查看测试'''
        print("========【AT2021-T07-14-14】集团管理-组织管理-组织搜索）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//input[@placeholder='请输入搜索内容']").send_keys('吃')
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span/i/img').click()
        tool.wait(1)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 集团管理-组织管理-创建性质（重复）
    def test35(self):
        '''集团管理-组织管理-创建性质（重复）测试'''
        print("========【AT2021-T07-14-15】集团管理-组织管理-创建性质（重复）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="tab-1"]/div/i').click()
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="line"]/div/div[2]/div[2]/div/div/i').click()
        tool.wait(1)
        tool.setText(b, 'propertiesName', "未分配单位")
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[3]/span/button[1]').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('操作失败', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-创建性质（成功）
    def test36(self):
        '''集团管理-组织管理-创建性质（成功）测试'''
        print("========【AT2021-T07-14-16】集团管理-组织管理-创建性质（成功）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="tab-1"]/div/i').click()
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="line"]/div/div[2]/div[2]/div/div/i').click()
        tool.wait(1)
        tool.setText(b, 'propertiesName', "吔屎")
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[3]/span/button[1]').click()
        tool.wait(1)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 集团管理-组织管理-分配单位（修改名称失败）
    def test37(self):
        '''集团管理-组织管理-分配单位（修改名称失败）测试'''
        print("========【AT2021-T07-14-17】集团管理-组织管理-分配单位（修改名称失败）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="tab-1"]/div/i').click()
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="tree"]/div[3]/div[1]/div/div/div').click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'分配单位')]").click()
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('操作失败', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-分配单位（修改名称成功）
    def test38(self):
        '''集团管理-组织管理-分配单位（修改名称成功）测试'''
        print("========【AT2021-T07-14-18】集团管理-组织管理-分配单位（修改名称成功）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="tab-1"]/div/i').click()
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="tree"]/div[3]/div[1]/div/div/div').click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'分配单位')]").click()
        tool.wait(1)
        tool.setText(b, 'propertiesName', "吔屎了Toby")
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('操作失败', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-分配单位
    def test39(self):
        '''集团管理-组织管理-分配单位（修改名称成功）测试'''
        print("========【AT2021-T07-14-19】集团管理-组织管理-分配单位=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="tab-1"]/div/i').click()
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="tree"]/div[3]/div[1]/div/div/div').click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'分配单位')]").click()
        tool.wait(1)
        tool.setText(b, 'propertiesName', "吔屎了Toby")
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="list"]/div[1]/div[1]/label/span/span').click()
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div/div[3]/span/button[1]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('修改成功', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-性质维护-删除
    def test40(self):
        '''集团管理-组织管理-性质维护-删除测试'''
        print("========【AT2021-T07-14-20】集团管理-组织管理-性质维护-删除=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="tab-1"]/div/i').click()
        tool.wait(1)
        b.find_element_by_xpath(
            "//span[contains(text(),'性质维护')]").click()
        tool.wait(2)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr/td[1]/div/label/span/span').click()
        tool.wait(1)
        b.find_element_by_xpath(
            '/html/body/div[2]/div/div[3]/button[2]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        self.assertEqual('删除性质成功', addUnitMsg)
        tool.close(b)

    # 集团管理-组织管理-性质查看
    def test41(self):
        '''集团管理-组织管理-性质查看测试'''
        print("========【AT2021-T07-14-21】集团管理-组织管理-性质查看=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="tab-1"]/div/i').click()
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="line"]/div/div[2]/div[2]/span/div').click()
        b.find_element_by_xpath('//*[@id="el-popover-169"]/div[1]/label[2]/span[1]/span').click()
        tool.wait(2)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)

    # 集团管理-组织管理-性质搜索
    def test42(self):
        '''集团管理-组织管理-性质搜索测试'''
        print("========【AT2021-T07-14-22】集团管理-组织管理-性质搜索）=============")
        b = tool.login("18857748370", "xr952343147")
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'集团管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath("//span[contains(text(),'组织管理')]").click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="tab-1"]/div/i').click()
        tool.wait(1)
        b.find_element_by_xpath("//input[@placeholder='请输入搜索内容']").send_keys('吔')
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span/i/img').click()
        tool.wait(1)
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        pic_path = '.\\unittest\\' + current_time + '.png'  # 设置存储图片路径，测试结果图片可以按照每天进行区分
        print(pic_path)
        b.save_screenshot(pic_path)  # 截图，获取测试结果
        tool.close(b)
