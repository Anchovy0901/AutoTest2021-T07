import time
import unittest

from selenium.webdriver.common.by import By

import HTMLTestReport
import tool

class unitTest(unittest.TestCase):
    # 新增部门-部门名称未填写
    def test1(self):
        print("========【AT2021-T07-3-1】新增部门-部门名称未填写 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        # 创建部门
        b.find_element_by_xpath('//*[@id="line"]/div/div[1]/div[2]/div/div/i').click()
        tool.wait(1)
        # tool.setText(b, "agencyName", "自测七队的部门")  # 部门名称
        # tool.wait(1)
        tool.setText(b, "agencyCode", "102938")  # 部门编码
        tool.wait(1)
        # tool.setOject(b, "parentId", "自测七队的上级部门")  # 上级部门
        # tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('请填写正确信息', addUnitMsg)
        tool.close(b)

    # 新增部门-成功添加
    def test2(self):
        print("========【AT2021-T07-3-2】新增部门-成功添加=============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        # 创建部门
        b.find_element_by_xpath('//*[@id="line"]/div/div[1]/div[2]/div/div/i').click()
        tool.wait(1)
        tool.setText(b, "agencyName", "自测七队的部门1")  # 部门名称
        tool.wait(1)
        tool.setText(b, "agencyCode", "102938")  # 部门编码
        tool.wait(1)
        # tool.setOject(b, "parentId", "自测七队的上级部门")  # 上级部门
        # tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('新增成功', addUnitMsg)
        tool.close(b)

    # 新增部门-部门编号重复
    def test3(self):
        print("========【AT2021-T07-3-3】新增部门-部门编号重复 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        # 创建部门
        b.find_element_by_xpath('//*[@id="line"]/div/div[1]/div[2]/div/div/i').click()
        tool.wait(1)
        tool.setText(b, "agencyName", "自测七队的部门2")  # 部门名称
        tool.wait(1)
        tool.setText(b, "agencyCode", "102938")  # 部门编码
        tool.wait(1)
        # tool.setOject(b, "parentId", "自测七队的上级部门")  # 上级部门
        # tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(0.5)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('该部门编码已存在，请勿重复添加!', addUnitMsg)
        tool.close(b)

    # 新增部门-部门批量导入
    def test4(self):

        print("========【AT2021-T07-3-4】新增部门-部门批量导入 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="部门维护"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="部门批量导入"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="批量导入"]').click()
        tool.wait(3.5)

        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('导入成功，如有部分错误数据请在导入记录中查看', addUnitMsg)
        tool.close(b)

    # 编辑部门-修改部门名称
    def test5(self):
        print("========【AT2021-T07-3-5】编辑部门-修改部门名称 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="部门维护"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//div[@class="cell el-tooltip"]/div/i').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[4]/td[5]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[1]').click()
        tool.wait(1)
        tool.setText(b, "agencyName", "自测七队的修改部门1")  # 部门名称
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()

        tool.wait(0.5)
        tool.close(b)

    # 编辑部门-修改部门编码
    def test6(self):
        print("========【AT2021-T07-3-6】编辑部门-修改部门编码 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="部门维护"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//div[@class="cell el-tooltip"]/div/i').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[4]/td[5]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[1]').click()
        tool.wait(1)
        tool.setText(b, "agencyCode", "109239928")  # 部门编码
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(1)
        tool.close(b)

    # 删除部门-删除不是末级的部门
    def test7(self):
        '''系统修改后强制只能修改末级的部门'''
        print("========【AT2021-T07-3-7】删除部门-删除不是末级的部门 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        tool.wait(1)
        addUnitMsg = "只能选择末级部门！"
        self.assertEqual('只能选择末级部门！', addUnitMsg)
        tool.close(b)

    # 删除部门-删除末级的部门
    def test8(self):
        '''编辑单位信息-改修联系方式'''
        print("========【AT2021-T07-3-8】删除部门-删除末级的部门 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="部门维护"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//div[@class="cell el-tooltip"]/div/i').click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[4]/td[1]/div/label/span/span').click()
        b.find_element_by_xpath('//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[5]/td[1]/div/label/span/span').click()
        b.find_element(By.XPATH, '//button/span[text()="删除"]').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@class="el-button el-button--default el-button--small el-button--primary "]/span').click()
        tool.wait(1)

        tool.close(b)

    # 新增公告-新增成功
    def test9(self):
        print("========【AT2021-T07-3-9】新增公告-新增成功 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="发布公告"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="新增"]').click()
        tool.wait(1)
        tool.setText(b, "noticeTitle", "测试测试")  # 标题
        tool.wait(1)
        tool.setTextArea(b, "noticeContent", "内容")  # 内容
        tool.wait(1)
        b.find_element_by_xpath("//form[@class='el-form el-form--label-top']/div[2]/div/div/div/input").click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom-start"]/div/div/ul/li/span[text()="信息上报"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(1)

        tool.close(b)

    # 新增公告-重复测试
    def test10(self):
        print("========【AT2021-T07-3-10】 新增公告-重复测试 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="发布公告"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="新增"]').click()
        tool.wait(1)
        tool.setText(b, "noticeTitle", "测试测试")  # 标题
        tool.wait(1)
        tool.setTextArea(b, "noticeContent", "内容")  # 内容
        tool.wait(1)
        b.find_element_by_xpath("//form[@class='el-form el-form--label-top']/div[2]/div/div/div/input").click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom-start"]/div/div/ul/li/span[text()="信息上报"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(1)
        tool.close(b)

    # 编辑公告-发布/下架切换
    def test11(self):
        print("========【AT2021-T07-3-11】编辑公告-发布/下架切换 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="发布公告"]').click()
        tool.wait(1)

        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[1]').click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span/i/img').click()
        tool.wait(4)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[1]').click()
        tool.wait(2)
        tool.close(b)

    # 编辑公告-修改标题
    def test12(self):
        print("========【AT2021-T07-3-12】编辑公告-修改标题 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="发布公告"]').click()
        tool.wait(1)

        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[2]/td[8]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[2]').click()
        tool.wait(1)
        tool.setText(b, "noticeTitle", "修改测试")  # 标题
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('编辑成功', addUnitMsg)
        tool.close(b)

    # 编辑公告-修改公告类型
    def test13(self):
        print("========【AT2021-T07-3-13】编辑公告-修改公告类型 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="发布公告"]').click()
        tool.wait(1)

        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[2]/td[8]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[2]').click()
        tool.wait(1)

        b.find_element_by_xpath("//form[@class='el-form el-form--label-top']/div[2]/div/div/div/input").click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom-start"]/div/div/ul/li/span[text()="信息上报"]').click()
        tool.wait(1)

        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(2)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('编辑成功', addUnitMsg)
        tool.close(b)

    # 删除公告-删除单个
    def test14(self):
        print("========【AT2021-T07-3-14】删除公告-删除单个 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="发布公告"]').click()
        tool.wait(1)

        b.find_element_by_xpath('//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[5]/td[1]/div/label/span/span').click()
        b.find_element(By.XPATH, '//button/span[text()="删除"]').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@class="el-button el-button--default el-button--small el-button--primary "]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('删除成功', addUnitMsg)
        tool.close(b)

    # 删除公告-删除多个
    def test15(self):
        print("========【AT2021-T07-3-15】删除公告-删除多个 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="发布公告"]').click()
        tool.wait(1)

        b.find_element_by_xpath('//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[5]/td[1]/div/label/span/span').click()
        b.find_element_by_xpath('//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[6]/td[1]/div/label/span/span').click()
        b.find_element(By.XPATH, '//button/span[text()="删除"]').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@class="el-button el-button--default el-button--small el-button--primary "]/span').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('删除成功', addUnitMsg)
        tool.close(b)

    # 账户开通-账户开通/停用
    def test16(self):
        print("========【AT2021-T07-3-16】账户开通-账户开通/停用 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        tool.wait(1)

        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[2]/td[9]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[2]').click()
        tool.wait(1)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/span/i/img').click()
        tool.wait(4)
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[2]/td[9]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[2]').click()
        tool.wait(2)
        tool.close(b)

    # 新增人员-人员批量导入
    def test17(self):
        print("========【AT2021-T07-3-17】新增人员-人员批量导入 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="人员导入"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="批量导入"]').click()
        tool.wait(3.5)

        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('导入成功，如有部分错误数据请在导入记录中查看', addUnitMsg)
        tool.close(b)

    # 变更部门-部门切换
    def test18(self):
        print("========【AT2021-T07-3-18】变更部门-部门切换 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[3]/td[9]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[1]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div/div/div').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('部门变更成功', addUnitMsg)
        tool.close(b)

    # 编辑人员信息-修改手机号
    def test19(self):
        print("========【AT2021-T07-3-19】编辑人员信息-修改手机号 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[3]/td[9]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[3]').click()
        tool.wait(1)
        tool.setText(b, "phone", "13566666666")  # 部门名称
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('修改成功', addUnitMsg)
        tool.close(b)

    # 编辑人员信息-角色分配
    def test20(self):
        print("========【AT2021-T07-3-20】编辑人员信息-角色分配 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[3]/td[9]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[4]').click()
        tool.wait(1)
        b.find_element_by_xpath("//*[@role='dialog']/div[2]/div/div/div/input").click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom-start"]/div/div/ul/li[3]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('更新成功', addUnitMsg)
        tool.close(b)

    # 补充手机号-批量导入
    def test21(self):
        print("========【AT2021-T07-3-21】补充手机号-批量导入 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="补充手机号"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="批量导入"]').click()
        tool.wait(3.5)

        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('导入成功，如有部分错误数据请在导入记录中查看', addUnitMsg)
        tool.close(b)

    # 编辑人员信息-移出单位
    def test22(self):
        print("========【AT2021-T07-3-22】编辑人员信息-移出单位 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[4]/div[2]/div/div/div[3]/div/div/div[4]/div[2]/table/tbody/tr[3]/td[9]/div/div/span/div/div/img').click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom"]/div[5]').click()
        tool.wait(1)
        b.find_element(By.XPATH,'//*[@class="el-button el-button--default el-button--small el-button--primary "]/span').click()
        tool.wait(1)
        tool.close(b)

    # 查看申请-查看单位申请
    def test23(self):
        '''解散单位'''
        print("========【AT2021-T07-3-23】查看申请-查看单位申请 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="查看申请"]').click()
        tool.wait(1)
        tool.close(b)

    # 新增人员-手机号重复
    def test24(self):
        '''解散单位'''
        print("========【AT2021-T07-2-24】解散单位 =============")
        b = tool.login("18857748370", "xr952343147")
        tool.joinItem(b, "单位管理", "部门人员")
        b.find_element(By.XPATH, '//button/span[text()="新增人员"]').click()
        tool.setText(b, "name", "测试小童")  # 人员名称
        tool.wait(1)
        tool.setText(b, "phone", "18888888889")  # 手机号
        tool.wait(1)
        b.find_element_by_xpath("//form[@class='el-form el-form--label-top']/div[3]/div/div/div/input").click()
        b.find_element(By.XPATH, '//*[@x-placement="bottom-start"]/div/div/ul/li/span[text()="普通用户"]').click()
        tool.wait(1)
        b.find_element(By.XPATH, '//button/span[text()="确 定"]').click()
        tool.wait(1)
        addUnitMsg = b.find_element_by_xpath("//div[@role='alert']/p").text
        self.assertEqual('该用户已在该单位中或已申请加入该单位!', addUnitMsg)
        tool.close(b)




