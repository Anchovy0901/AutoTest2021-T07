import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import tool


class unitTest(unittest.TestCase):
    def test1(self):
        print("========【AT2021-T07-5-01】应用市场-获取应用 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button/span').click()

        elements = b.find_elements(By.XPATH, '//div[@class="layout"]//div[@class="layout-box"]')
        for element in elements:
            itemText = element.find_element_by_xpath('./div//div[@class="layout-box__name"]').text
            print(itemText)  # 应用名称
            if (itemText == '校企应用'):
                element.find_element_by_xpath('./div//button[1]').click()
                tool.wait(1)
                b.find_element_by_xpath('//div[@class="el-dialog__header"]/div/div[4]/button').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('应用订阅成功', addUnitMsg)

    def test2(self):
        '''单位管理-应用中心'''
        print("========【AT2021-T07-5-16】应用退订-成功测试 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        elements = b.find_elements(By.XPATH, '//tr[@class="el-table__row"]')
        for element in elements:
            itemText = element.find_element_by_xpath('./td[4]/div').text
            print(itemText)             #应用名称
            if(itemText == '校企应用'):
                ele = element.find_element_by_xpath('./td[last()]//img')
                ActionChains(b).move_to_element(ele).perform()
                tool.wait(1)
                b.find_element_by_xpath('//body/div[last()]/div[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('退订成功', addUnitMsg)

    def test3(self):
        '''图标库-新建图标-成功测试'''
        print("========【AT2021-T07-5-02】图标库-新建图标-成功测试 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button/span').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[2]').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/button[1]').click()
        tool.wait(15)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div[3]/span/button[1]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('新增成功', addUnitMsg)

    def test4(self):
        '''图标库-新增图标-图标大小不符合规范（500kb~2Mb）'''
        print("========【AT2021-T07-5-03】图标库-新增图标-图标大小不符合规范（500kb~2Mb） =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button/span').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[2]').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/button[1]').click()
        tool.wait(15)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div[3]/span/button[1]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertNotEqual('新增成功', addUnitMsg)

    def test5(self):
        '''图标库-新增图标-图标大小不符合规范（>2Mb）'''
        print("========【AT2021-T07-5-04】图标库-新增图标-图标大小不符合规范（>2Mb） =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button/span').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[2]').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/button[1]').click()
        tool.wait(15)
        # b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div[3]/span/button[1]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertNotEqual('新增成功', addUnitMsg)

    def test6(self):
        '''图标库-删除图标 '''
        print("========【AT2021-T07-5-05】图标库-删除图标  =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button/span').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[2]').click() #图标库
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/button[2]/span').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/input').click()
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/button[1]/span').click()
        b.find_element_by_xpath(
            '//button/span[contains(text(),"确定")]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('删除成功', addUnitMsg)

    def test7(self):
        '''注册应用-成功测试 '''
        print("========【AT2021-T07-5-07】注册应用-成功测试=============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click()  # 应用市场
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()  # 开发者中心
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[3]').click()  # 注册
        tool.setText4(b, "appName", "协和科技")  # 应用名称
        tool.setText4(b, "contactName", "杨某人")  # 负责人姓名
        tool.setText4(b, "contact", "1234567890")  # 负责人联系方式
        tool.setText5(b, "description", "协和科技-诚信为本")  # 应用介绍
        tool.setX(b, "appType", "大数据应用")  # 应用类型
        tool.setX(b, "targetUser", "个人")  # 目标用户
        tool.setX(b, "appField", "数字社会")  # 应用领域
        tool.setX(b, "appCategory", "IaaS应用")  # 目标用户
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('注册申请提交成功', addUnitMsg)

    def test8(self):
        '''注册应用-缺省测试-应用名称未填写 '''
        print("========【AT2021-T07-5-08】注册应用-缺省测试-应用名称未填写=============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click()  # 应用市场
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()  # 开发者中心
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[3]').click()  # 注册
        # tool.setText4(b, "appName", "协和科技-2")  #应用名称
        tool.setText4(b, "contactName", "杨某人")  # 负责人姓名
        tool.setText4(b, "contact", "1234567890")  # 负责人联系方式
        tool.setText5(b, "description", "协和科技-诚信为本")  # 应用介绍
        tool.setX(b, "appType", "大数据应用")  # 应用类型
        tool.setX(b, "targetUser", "个人")  # 目标用户
        tool.setX(b, "appField", "数字社会")  # 应用领域
        tool.setX(b, "appCategory", "IaaS应用")  # 目标用户
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@class='el-form-item__error']").text
        self.assertEqual('请输入应用名称', addUnitMsg)

    def test9(self):
        print("========【AT2021-T07-5-09】注册应用-缺省测试-应用类型未填写=============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click()  # 应用市场
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()  # 开发者中心
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[3]').click()  # 注册
        tool.setText4(b, "appName", "协和科技-2")  # 应用名称
        tool.setText4(b, "contactName", "杨某人")  # 负责人姓名
        tool.setText4(b, "contact", "1234567890")  # 负责人联系方式
        tool.setText5(b, "description", "协和科技-诚信为本")  # 应用介绍
        # tool.setX(b, "appType", "大数据应用")  #应用类型
        tool.setX(b, "targetUser", "个人")  # 目标用户
        tool.setX(b, "appField", "数字社会")  # 应用领域
        tool.setX(b, "appCategory", "IaaS应用")  # 目标用户
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@class='el-form-item__error']").text
        self.assertEqual('请选择应用类型', addUnitMsg)

    def test10(self):
        print("========【AT2021-T07-5-10】注册应用-缺省测试-目标用户未填写=============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click()  # 应用市场
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()  # 开发者中心
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[3]').click()  # 注册
        tool.setText4(b, "appName", "协和科技-2")  # 应用名称
        tool.setText4(b, "contactName", "杨某人")  # 负责人姓名
        tool.setText4(b, "contact", "1234567890")  # 负责人联系方式
        tool.setText5(b, "description", "协和科技-诚信为本")  # 应用介绍
        tool.setX(b, "appType", "大数据应用")  # 应用类型
        # tool.setX(b, "targetUser", "个人")  #目标用户
        tool.setX(b, "appField", "数字社会")  # 应用领域
        tool.setX(b, "appCategory", "IaaS应用")  # 目标用户
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@class='el-form-item__error']").text
        self.assertEqual('请选择目标用户', addUnitMsg)

    def test11(self):
        print("========【AT2021-T07-5-11】注册应用-缺省测试-应用领域未填写=============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click()  # 应用市场
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()  # 开发者中心
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[3]').click()  # 注册
        tool.setText4(b, "appName", "协和科技-2")  # 应用名称
        tool.setText4(b, "contactName", "杨某人")  # 负责人姓名
        tool.setText4(b, "contact", "1234567890")  # 负责人联系方式
        tool.setText5(b, "description", "协和科技-诚信为本")  # 应用介绍
        tool.setX(b, "appType", "大数据应用")  # 应用类型
        tool.setX(b, "targetUser", "个人")  # 目标用户
        # tool.setX(b, "appField", "数字社会")  #应用领域
        tool.setX(b, "appCategory", "IaaS应用")  # 目标分类
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@class='el-form-item__error']").text
        self.assertEqual('请选择应用领域', addUnitMsg)

    def test12(self):
        print("========【AT2021-T07-5-12】注册应用-缺省测试-应用分类未填写=============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click()  # 应用市场
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()  # 开发者中心
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[3]').click()  # 注册
        tool.setText4(b, "appName", "协和科技-2")  # 应用名称
        tool.setText4(b, "contactName", "杨某人")  # 负责人姓名
        tool.setText4(b, "contact", "1234567890")  # 负责人联系方式
        tool.setText5(b, "description", "协和科技-诚信为本")  # 应用介绍
        tool.setX(b, "appType", "大数据应用")  # 应用类型
        tool.setX(b, "targetUser", "个人")  # 目标用户
        tool.setX(b, "appField", "数字社会")  # 应用领域
        # tool.setX(b, "appCategory", "IaaS应用")  #目标分类
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@class='el-form-item__error']").text
        self.assertEqual('请选择应用分类', addUnitMsg)

    def test13(self):
        print("========【AT2021-T07-5-13】注册应用-缺省测试-应用介绍未填写=============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click()  # 应用市场
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()  # 开发者中心
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[3]').click()  # 注册
        tool.setText4(b, "appName", "协和科技-2")  # 应用名称
        tool.setText4(b, "contactName", "杨某人")  # 负责人姓名
        tool.setText4(b, "contact", "1234567890")  # 负责人联系方式
        # tool.setText5(b, "description", "协和科技-诚信为本")  #应用介绍
        tool.setX(b, "appType", "大数据应用")  # 应用类型
        tool.setX(b, "targetUser", "个人")  # 目标用户
        tool.setX(b, "appField", "数字社会")  # 应用领域
        tool.setX(b, "appCategory", "IaaS应用")  # 目标分类
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@class='el-form-item__error']").text
        self.assertEqual('请输入应用介绍', addUnitMsg)

    def test14(self):
        print("========【AT2021-T07-5-14】注册应用-缺省测试-负责人姓名未填写=============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click()  # 应用市场
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()  # 开发者中心
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[3]').click()  # 注册
        tool.setText4(b, "appName", "协和科技-2")  # 应用名称
        # tool.setText4(b, "contactName", "杨某人")  #负责人姓名
        tool.setText4(b, "contact", "1234567890")  # 负责人联系方式
        tool.setText5(b, "description", "协和科技-诚信为本")  # 应用介绍
        tool.setX(b, "appType", "大数据应用")  # 应用类型
        tool.setX(b, "targetUser", "个人")  # 目标用户
        tool.setX(b, "appField", "数字社会")  # 应用领域
        tool.setX(b, "appCategory", "IaaS应用")  # 目标分类
        tool.wait(1)
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@class='el-form-item__error']").text
        self.assertEqual('请输入负责人姓名', addUnitMsg)

    def test16(self):
        print("========【AT2021-T07-5-16】注册应用-重复测试-应用名称重复测试=============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        b.find_element(By.XPATH, '//span[@title="单位管理"]').click()
        b.find_element(By.XPATH, '//span[@title="应用中心"]').click()
        tool.wait(1)

        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/button').click() #应用市场
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/button[2]').click()  #开发者中心
        b.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[3]').click()  #注册
        tool.setText4(b, "appName", "协和科技")  #应用名称
        tool.setText4(b, "contactName", "杨某人")  #负责人姓名
        tool.setText4(b, "contact", "123")  #负责人联系方式
        tool.setText5(b, "description", "协和科技-诚信为本")  #应用介绍
        tool.setX(b, "appType", "大数据应用")  #应用类型
        tool.setX(b, "targetUser", "个人")  #目标用户
        tool.setX(b, "appField", "数字社会")  #应用领域
        tool.setX(b, "appCategory", "IaaS应用")  #目标分类
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button[2]').click()

        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertNotEqual('注册申请提交成功', addUnitMsg)