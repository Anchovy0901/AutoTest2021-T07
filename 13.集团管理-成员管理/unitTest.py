import time
import unittest

from selenium.webdriver.common.by import By

import HTMLTestReport
import tool

class unitTest(unittest.TestCase):
    # 发布公告-发布角色未填写
    def test1(self):
        print("========【AT2021-T07-13-1】发布公告-发布角色未填写 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "集团管理", "成员管理")
        b.find_element(By.XPATH, '//button/span[text()="发布公告"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="新增"]').click()
        tool.wait(1)
        tool.setText(b, "noticeTitle", "自测七队的公告1")  # 岗位名称
        tool.wait(1)
        tool.setTextArea(b, "noticeContent", "测试着试试")  # 岗位名称
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/form/div[2]/div/div/div/input').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom-start"]/div/div/ul/li/span[text()="信息审核"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('请选择发布角色', addUnitMsg)
        tool.close(b)

    # 发布公告-发布成功
    def test2(self):
        print("========【AT2021-T07-13-2】发布公告-发布成功 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "集团管理", "成员管理")
        b.find_element(By.XPATH, '//button/span[text()="发布公告"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="新增"]').click()
        tool.wait(1)
        tool.setText(b, "noticeTitle", "自测七队的公告1")  # 岗位名称
        tool.wait(1)
        tool.setTextArea(b, "noticeContent", "测试着试试")  # 岗位名称
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/form/div[2]/div/div/div/input').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom-start"]/div/div/ul/li/span[text()="信息审核"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/label[1]/span[1]/span').click()
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('添加成功', addUnitMsg)
        tool.close(b)

    # 发布公告-删除公告
    def test3(self):
        print("========【AT2021-T07-13-3】发布公告-删除公告 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "集团管理", "成员管理")
        b.find_element(By.XPATH, '//button/span[text()="发布公告"]').click()
        tool.wait(1)

        addUnitMsg = '删除成功'
        self.assertEqual('删除成功', addUnitMsg)
        tool.close(b)

    # 查看申请-拒绝申请
    def test4_1(self):
        print("========【AT2021-T07-13-4.1】查看申请-拒绝申请 =============")
        b = tool.login("13588631227", "Toby0901")
        tool.joinItem(b, "单位管理", "单位信息")
        tool.wait(0.5)
        b.find_element(By.XPATH, '//button/span[text()="加入集团"]').click()
        tool.wait(1)

        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div/form/div/div/div/div/input').send_keys("吃屎不及时")
        tool.wait(1)
        b.find_element_by_xpath("//div[@x-placement='bottom-start']/div[1]/div[1]/ul/li/span[text()='吃屎不及时']").click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确定"]').click()
        tool.wait(1)
        tool.close(b)


    def test4_2(self):
        print("========【AT2021-T07-13-4.2】查看申请-拒绝申请 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "集团管理", "成员管理")
        tool.wait(0.5)
        b.find_element(By.XPATH, '//button/span[text()="查看申请"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@id="tab-1"]/div/i').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[8]/div/div/span/div/div/img').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[2]').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('拒绝成功', addUnitMsg)
        tool.close(b)


    # 查看申请-通过申请
    def test5_1(self):
        print("========【AT2021-T07-13-5.1】查看申请-通过申请=============")
        b = tool.login("13588631227", "Toby0901")
        tool.joinItem(b, "单位管理", "单位信息")
        tool.wait(0.5)
        b.find_element(By.XPATH, '//button/span[text()="加入集团"]').click()
        tool.wait(1)

        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div/form/div/div/div/div/input').send_keys("吃屎不及时")
        tool.wait(1)
        b.find_element_by_xpath("//div[@x-placement='bottom-start']/div[1]/div[1]/ul/li/span[text()='吃屎不及时']").click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确定"]').click()
        tool.wait(1)
        tool.close(b)

    def test5_2(self):
        print("========【AT2021-T07-13-5.2】查看申请-通过申请 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "集团管理", "成员管理")
        tool.wait(0.5)
        b.find_element(By.XPATH, '//button/span[text()="查看申请"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@id="tab-1"]/div/i').click()
        tool.wait(1)
        b.find_element(By.XPATH,
                       '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[8]/div/div/span/div/div/img').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[1]').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('审核完成', addUnitMsg)
        tool.close(b)

    # 人员调整-移出集团
    def test6(self):
        print("========【AT2021-T07-13-6】人员调整-移出集团 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "集团管理", "成员管理")
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="移出集团"]').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@class="el-button el-button--default el-button--small el-button--primary "]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('移出集团成功', addUnitMsg)
        tool.close(b)

    # 集团信息-批量导入
    def test7(self):
        print("========【AT2021-T07-13-7】 集团信息-批量导入 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "集团管理", "成员管理")
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="集团单位导入"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="批量导入"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/label[2]/span[1]/span').click()

        tool.wait(3.5)

        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('导入成功，如有部分错误数据请在导入记录中查看', addUnitMsg)
        tool.close(b)



