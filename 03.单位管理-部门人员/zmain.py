import time
import unittest

import HTMLTestReport
import unitTest
if __name__ == "__main__":
    '''生成测试报告'''
    #单位管理-部门人员
    testunit = unittest.TestSuite()

    testunit.addTest(unitTest.unitTest("test1"))
    testunit.addTest(unitTest.unitTest("test2"))
    testunit.addTest(unitTest.unitTest("test3"))
    testunit.addTest(unitTest.unitTest("test4"))
    testunit.addTest(unitTest.unitTest("test5"))
    testunit.addTest(unitTest.unitTest("test6"))
    testunit.addTest(unitTest.unitTest("test7"))
    testunit.addTest(unitTest.unitTest("test8"))
    testunit.addTest(unitTest.unitTest("test9"))
    testunit.addTest(unitTest.unitTest("test10"))
    testunit.addTest(unitTest.unitTest("test11"))
    testunit.addTest(unitTest.unitTest("test12"))
    testunit.addTest(unitTest.unitTest("test13"))
    testunit.addTest(unitTest.unitTest("test14"))
    testunit.addTest(unitTest.unitTest("test15"))
    testunit.addTest(unitTest.unitTest("test16"))
    testunit.addTest(unitTest.unitTest("test17"))
    testunit.addTest(unitTest.unitTest("test18"))
    testunit.addTest(unitTest.unitTest("test19"))
    testunit.addTest(unitTest.unitTest("test20"))
    testunit.addTest(unitTest.unitTest("test21"))
    testunit.addTest(unitTest.unitTest("test22"))
    testunit.addTest(unitTest.unitTest("test23"))
    testunit.addTest(unitTest.unitTest("test24"))

    report_path = ".\\maintest\\单位管理-部门人员测试"  + '.html'  # 生成测试报告的路径
    fp = open(report_path, "wb")
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description='自动化测试演示报告', tester='童峻涛')
    runner.run(testunit)
    fp.close()
    print("完成："+report_path)
