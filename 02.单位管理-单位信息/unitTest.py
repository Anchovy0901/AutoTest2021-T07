import time
import unittest

from selenium.webdriver.common.by import By

import HTMLTestReport
import tool

class unitTest(unittest.TestCase):
    # 新增单位-单位名称未填写
    def test1(self):
        '''新增单位-单位名称未填写'''
        print("========【case_0001】新增单位-单位名称未填写 =============")
        b = tool.login("18857748370", "xr952343147")
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div/div[1]').click()
        tool.wait(1)
        #创建单位
        b.find_element_by_xpath('//*[@class="select-item__btn"]/i').click()
        tool.wait(1)
        # tool.setText(b, "tenantName", "Dio任的一拳超人")  # 单位名称
        tool.wait(1)
        tool.setText(b, "socialCreCode", "102938475610293847")  # 社会统一信用代码
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[2]").text
        self.assertEqual('请输入单位名称', addUnitMsg)
        tool.close(b)

    # 新增单位-社会统一信用代码未填写
    def test2(self):
        '''新增单位-社会统一信用代码未填写'''
        print("========【case_0002】新增单位-社会统一信用代码未填写=============")
        b = tool.login("18857748370", "xr952343147")
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div/div[1]').click()
        tool.wait(1)
        # 创建单位
        b.find_element_by_xpath('//*[@class="select-item__btn"]/i').click()
        tool.wait(1)
        tool.setText(b, "tenantName", "Dio任的一拳超人")  # 单位名称
        tool.wait(1)
        # tool.setText(b, "socialCreCode", "102938475610293847")  # 社会统一信用代码
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/form/div[2]/div/div[2]").text
        self.assertEqual('请输入社会统一信用代码', addUnitMsg)
        tool.close(b)

    # 新增单位-社会统一信用代码不符合规范（数字位数不对）
    def test3(self):
        '''新增单位-社会统一信用代码不符合规范（数字位数不对）'''
        print("========【case_0003】新增单位-社会统一信用代码不符合规范（数字位数不对） =============")
        b = tool.login("18857748370", "xr952343147")
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div/div[1]').click()
        tool.wait(1)
        # 创建单位
        b.find_element_by_xpath('//*[@class="select-item__btn"]/i').click()
        tool.wait(1)
        tool.setText(b, "tenantName", "Dio任的一拳超人")  # 单位名称
        tool.wait(1)
        tool.setText(b, "socialCreCode", "2132312")  # 社会统一信用代码
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/form/div[2]/div/div[2]").text
        self.assertEqual('请输入符合规范的社会统一信用代码', addUnitMsg)
        tool.close(b)

    # 新增单位-社会统一信用代码不符合规范（混入字母）
    def test4(self):
        '''新增单位-社会统一信用代码不符合规范（混入字母）'''
        print("========【case_0004】新增单位-社会统一信用代码不符合规范（混入字母） =============")
        b = tool.login("18857748370", "xr952343147")
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div/div[1]').click()
        tool.wait(1)
        # 创建单位
        b.find_element_by_xpath('//*[@class="select-item__btn"]/i').click()
        tool.wait(1)
        tool.setText(b, "tenantName", "Dio任的一拳超人")  # 单位名称
        tool.wait(1)
        tool.setText(b, "socialCreCode", "1029384aa610293847")  # 社会统一信用代码
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/form/div[2]/div/div[2]").text
        self.assertEqual('请输入符合规范的社会统一信用代码', addUnitMsg)
        tool.close(b)

    # 新增单位-单位名称重复
    def test5(self):
        '''新增单位-单位名称重复'''
        print("========【case_0005】新增单位-单位名称重复 =============")
        b = tool.login("18857748370", "xr952343147")
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div/div[1]').click()
        tool.wait(1)
        # 创建单位
        b.find_element_by_xpath('//*[@class="select-item__btn"]/i').click()
        tool.wait(1)
        tool.setText(b, "tenantName", "豪哥什么时候请客吃饭")  # 单位名称
        tool.wait(1)
        tool.setText(b, "socialCreCode", "102938475610293847")  # 社会统一信用代码
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('单位已存在，可申请加入该单位！', addUnitMsg)
        tool.close(b)

    # 新增单位-社会统一信用代码重复
    def test6(self):
        '''新增单位-社会统一信用代码重复'''
        print("========【case_0006】新增单位-社会统一信用代码重复 =============")
        b = tool.login("18857748370", "xr952343147")
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div/div[1]').click()
        tool.wait(1)
        # 创建单位
        b.find_element_by_xpath('//*[@class="select-item__btn"]/i').click()
        tool.wait(1)
        tool.setText(b, "tenantName", "今天厕所的饭有点苦涩")  # 单位名称
        tool.wait(1)
        tool.setText(b, "socialCreCode", "123456789098765433")  # 社会统一信用代码
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('单位已存在，可申请加入该单位！', addUnitMsg)
        tool.close(b)

    # 新增单位-新建成功
    def test7(self):
        '''新增土地啥都不写测试'''
        print("========【case_0007】新增单位-新建成功 =============")
        b = tool.login("18857748370", "xr952343147")
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div/div/div[1]').click()
        tool.wait(1)
        # 创建单位
        b.find_element_by_xpath('//*[@class="select-item__btn"]/i').click()
        tool.wait(1)
        tool.setText(b, "tenantName", "dio任速度洗内")  # 单位名称
        tool.wait(1)
        tool.setText(b, "socialCreCode", "102988885610293847")  # 社会统一信用代码
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        tool.close(b)

    # 编辑单位信息-改修联系方式
    def test8(self):
        '''编辑单位信息-改修联系方式'''
        print("========【case_0008】编辑单位信息-改修联系方式=============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        #点击编辑单位信息
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/button/span[text()="编辑单位信息"]').click()
        tool.wait(1)
        #相当于setText（）
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[2]/div[1]/div[1]/input').clear()
        tool.wait(1)
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[2]/div[1]/div[1]/input').send_keys("13866666666")
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)

        tool.close(b)

    # 编辑单位信息-区划名称
    def test9(self):
        '''编辑单位信息-区划名称'''
        print("========【case_0009】编辑单位信息-区划名称 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        # 点击编辑单位信息
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/button/span[text()="编辑单位信息"]').click()
        tool.wait(1)
        # 获取下拉框
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div/form/div[6]/div/div/div/input').click()
        tool.wait(1)
        #相当于setObject（）
        b.find_element_by_xpath("//div[@x-placement='bottom-start']/div[1]/div[1]/div[1]/ul/li/label/span").click()
        # tool.setObject(b,"administrationDivisionName","北京")
        # tool.wait(1)
        # tool.setObject(b, "administrationDivisionName", "北京市")
        # tool.wait(1)
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)

        tool.close(b)

    # 编辑单位信息-单位地址
    def test10(self):
        '''编辑单位信息-单位地址'''
        print("========【case_0010】 编辑单位信息-单位地址 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        # 点击编辑单位信息
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/button/span[text()="编辑单位信息"]').click()
        #相当于setObject（）
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div[2]/div/form/div[8]/div/div/div/input').click()
        tool.wait(1)
        b.find_element_by_xpath("//div[@x-placement='bottom-start']/div[1]/div[1]/div[1]/ul/li/span[text()='北京']").click()
        tool.wait(1)
        b.find_element_by_xpath("//div[@x-placement='bottom-start']/div[1]/div[2]/div[1]/ul/li/span[text()='北京市']").click()
        tool.wait(1)
        b.find_element_by_xpath("//div[@x-placement='bottom-start']/div[1]/div[3]/div[1]/ul/li/span[text()='东城区']").click()
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        tool.close(b)

    # 创建集团-集团名称未填
    def test11(self):
        '''创建集团-集团名称未填'''
        print("========【case_0011】创建集团-集团名称未填 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        # 点击创建集团
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button/span[text()="创建集团"]').click()

        #相当于setText()
        # b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[1]/div/div/input').send_keys("我dio任要吃饭")
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[2]/div/div/input').send_keys("吃饭集团")
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[3]/div/div/input').send_keys("吃饭必拉稀")
        tool.wait(1)

        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('请输入正确信息', addUnitMsg)
        tool.close(b)

    # 创建集团-集团描述未填
    def test12(self):
        '''创建集团-集团描述未填'''
        print("========【case_0012】创建集团-集团描述未填 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        # 点击创建集团
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button/span[text()="创建集团"]').click()

        #相当于setText()
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[1]/div/div/input').send_keys("我dio任要吃饭")
        # b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[2]/div/div/input').send_keys("吃饭集团")
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[3]/div/div/input').send_keys("吃饭必拉稀")
        tool.wait(1)

        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('请输入正确信息', addUnitMsg)
        tool.close(b)

    # 创建集团-集团编码未填
    def test13(self):
        '''创建集团-集团编码未填'''
        print("========【case_0013】创建集团-集团编码未填 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")

        # 点击创建集团
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button/span[text()="创建集团"]').click()

        #相当于setText()
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[1]/div/div/input').send_keys("我dio任要吃饭")
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[2]/div/div/input').send_keys("吃饭集团")
        # b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[3]/div/div/input').send_keys("吃饭必拉稀")
        tool.wait(1)

        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('请输入正确信息', addUnitMsg)
        tool.close(b)

    # 创建集团-创建成功
    def test14(self):
        '''创建集团-创建成功'''
        print("========【case_0014】创建集团-创建成功 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        tool.wait(1)
        # 点击创建集团
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button/span[text()="创建集团"]').click()
        tool.wait(1)
        #相当于setText()
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[1]/div/div/input').send_keys("我dio任要吃饭")
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[2]/div/div/input').send_keys("吃饭集团")
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[3]/div/div/input').send_keys("吃饭必拉稀")
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        tool.close(b)

    # 创建集团-集团名称重复
    def test15(self):
        '''创建集团-集团名称重复'''
        print("========【case_0015】创建集团-集团名称重复=============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        tool.wait(1)
        # 点击创建集团
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button/span[text()="创建集团"]').click()
        tool.wait(1)
        #相当于setText()
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[1]/div/div/input').send_keys("我dio任要吃饭")
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[2]/div/div/input').send_keys("吃饭gogogo")
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[3]/div/div/input').send_keys("吃饭未必拉稀")

        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('该集团名存在', addUnitMsg)
        tool.close(b)

    # 创建集团-集团编码重复
    def test16(self):
        '''创建集团-集团编码重复'''
        print("========【case_0016】创建集团-集团编码重复 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        # 点击创建集团
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button/span[text()="创建集团"]').click()

        #相当于setText()
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[1]/div/div/input').send_keys("我dio任不要吃饭")
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[2]/div/div/input').send_keys("不吃饭集团")
        b.find_element_by_xpath('//*[@role="dialog"]/div[2]/div[1]/form/div[3]/div/div/input').send_keys("吃饭必拉稀")

        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('该集团编码存在', addUnitMsg)
        tool.close(b)

    # 加入集团-提交申请
    def test17(self):
        '''加入集团-提交申请'''
        print("========【case_0017】加入集团-提交申请 =============")
        b = tool.login("17306422238", "YANGyuanJIE#3")
        tool.joinItem(b, "单位管理", "单位信息")
        # 点击加入集团
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button/span[text()="加入集团"]').click()

        #相当于setText()
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div/form/div/div/div/div/input').send_keys("我dio任要吃饭")
        tool.wait(1)
        b.find_element_by_xpath("//div[@x-placement='bottom-start']/div[1]/div[1]/ul/li/span[text()='我dio任要吃饭']").click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('申请成功，请等待审核', addUnitMsg)
        tool.close(b)

    # 加入集团-查看申请
    def test18(self):
        '''加入集团-查看申请'''
        print("========【case_0018】加入集团-查看申请 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        # 点击加入集团
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/button/span[text()="查看申请"]').click()
        tool.wait(2)
        tool.close(b)

    # 查看单位信息-查看更多
    def test19(self):
        '''查看单位信息-查看更多'''
        print("========【case_0019】查看单位信息-查看更多 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        # 点击查看更多
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/button/span[text()="编辑单位信息"]').click()
        tool.wait(2)
        tool.close(b)

    # 解散集团
    def test20(self):
        '''解散集团'''
        print("========【case_0020】解散集团 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "单位信息")
        # 点击查看更多
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[8]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH,'//*[@x-placement="bottom"]/div[1]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@class="el-button el-button--default el-button--small el-button--primary "]/span').click()

        tool.wait(2)
        tool.close(b)

    # 解散单位
    def test21(self):
        '''解散单位'''
        print("========【case_0021】解散单位 =============")
        b = tool.login("18857748370", "xr952343147")
        # 点击查看更多
        b.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div/div/i').click()
        tool.wait(1)
        elements = b.find_elements_by_class_name("el-dropdown-menu__item")
        elements[0].click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[10]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[2]').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@class="el-button el-button--default el-button--small el-button--primary "]/span').click()

        tool.wait(2)
        tool.close(b)





