import time
import unittest

from selenium.webdriver.common.by import By

import HTMLTestReport
import tool

class unitTest(unittest.TestCase):
    # 新增岗位-岗位名称未填写
    def test1(self):
        print("========【AT2021-T07-4-1】新增部门-部门名称未填写 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        # 创建岗位
        b.find_element_by_xpath('//*[@id="line"]/div/div[1]/div[2]/div/i').click()
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('请填写正确信息', addUnitMsg)
        tool.close(b)

    # 新增岗位-新增成功
    def test2(self):
        print("========【AT2021-T07-3-2】新增部门-成功添加=============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        # 创建岗位
        b.find_element_by_xpath('//*[@id="line"]/div/div[1]/div[2]/div/i').click()
        tool.wait(1)
        tool.setText(b, "jobName", "自测七队的岗位1")  # 岗位名称
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        tool.close(b)

    # 新增岗位-岗位名称重复
    def test3(self):
        print("========【AT2021-T07-3-3】新增部门-部门编号重复 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        # 创建岗位
        b.find_element_by_xpath('//*[@id="line"]/div/div[1]/div[2]/div/i').click()
        tool.wait(1)
        tool.setText(b, "jobName", "自测七队的岗位1")  # 岗位名称
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('岗位已存在，请勿重复添加', addUnitMsg)
        tool.close(b)

    # 新增岗位-特殊名称（“未分配人员”）
    def test4(self):

        print("========【AT2021-T07-3-4】新增部门-部门批量导入 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        # 创建岗位
        b.find_element_by_xpath('//*[@id="line"]/div/div[1]/div[2]/div/i').click()
        tool.wait(1)
        tool.setText(b, "jobName", "未分配人员")  # 岗位名称
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('注意单位名称', addUnitMsg)
        tool.close(b)

    # 修改岗位-修改岗位名称
    def test5(self):
        print("========【AT2021-T07-3-5】编辑部门-修改部门名称 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        b.find_element(By.XPATH, '//button/span[text()="岗位维护"]').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[6]/td[5]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[1]').click()
        tool.wait(1)
        tool.setText(b, "jobName", "自测七队的修改岗位1")  # 岗位名称
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('修改成功', addUnitMsg)
        tool.close(b)

    # 人员调整-调整岗位
    def test6(self):
        print("========【AT2021-T07-3-6】编辑部门-修改部门编码 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[7]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[1]').click()
        tool.wait(1)
        b.find_element_by_xpath("//*[@role='dialog']/div[2]/div/div/div/input").click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom-start"]/div/div/ul/li[1]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('修改成功', addUnitMsg)
        tool.close(b)

    # 岗位信息-分配人员
    def test7(self):
        '''系统修改后强制只能修改末级的部门'''
        print("========【AT2021-T07-3-7】删除部门-删除不是末级的部门 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="tree"]/div/div[8]/div[1]/div/div/div').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[7]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[1]').click()
        tool.wait(1)
        b.find_element_by_xpath("//*[@role='dialog']/div[2]/div/div/div/input").click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom-start"]/div/div/ul/li[7]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('更新成功', addUnitMsg)
        tool.close(b)

    # 岗位信息-移出人员
    def test8(self):
        '''编辑单位信息-改修联系方式'''
        print("========【AT2021-T07-3-8】删除部门-删除末级的部门 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@id="tree"]/div/div[8]/div[1]/div/div/div').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[7]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[2]').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@class="el-button el-button--default el-button--small el-button--primary "]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('移除人员成功', addUnitMsg)

        tool.close(b)

    # 岗位信息-岗位内分配人员
    def test9(self):
        print("========【AT2021-T07-3-9】新增公告-新增成功 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@id="tree"]/div/div[8]/div[1]/div/div/div').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div[1]/div/div/div[2]/span').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="list"]/div[2]/div[1]/label/span/span').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('修改成功', addUnitMsg)

        tool.close(b)

    # 岗位信息批量导入
    def test10(self):
        print("========【AT2021-T07-3-10】 新增公告-重复测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="岗位维护"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="岗位导入"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="批量导入"]').click()
        tool.wait(3.5)

        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('导入成功，如有部分错误数据请在导入记录中查看', addUnitMsg)
        tool.close(b)

    # 岗位信息-删除岗位
    def test11(self):
        print("========【AT2021-T07-3-11】编辑公告-发布/下架切换 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "岗位管理")
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="岗位维护"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr[6]/td[1]/div/label/span/span').click()
        tool.wait(0.5)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr[7]/td[1]/div/label/span/span').click()
        tool.wait(0.5)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr[8]/td[1]/div/label/span/span').click()
        tool.wait(0.5)
        b.find_element(By.XPATH, '//button/span[text()="删除"]').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@class="el-button el-button--default el-button--small el-button--primary "]/span').click()
        tool.wait(0.5)

        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('删除岗位成功', addUnitMsg)
        tool.close(b)







