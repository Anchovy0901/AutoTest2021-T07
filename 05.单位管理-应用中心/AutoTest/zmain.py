import time
import unittest
import HTMLTestReport
import appTest

if __name__ == "__main__":
    '''生成测试报告'''

    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()

    # testunit.addTest(appTest.unitTest("test1"))
    # testunit.addTest(appTest.unitTest("test2"))
    # testunit.addTest(appTest.unitTest("test3"))
    # testunit.addTest(appTest.unitTest("test4"))
    # testunit.addTest(appTest.unitTest("test5"))
    # testunit.addTest(appTest.unitTest("test6"))
    # testunit.addTest(appTest.unitTest("test7"))
    # testunit.addTest(appTest.unitTest("test8"))
    # testunit.addTest(appTest.unitTest("test9"))
    # testunit.addTest(appTest.unitTest("test10"))
    # testunit.addTest(appTest.unitTest("test11"))
    # testunit.addTest(appTest.unitTest("test12"))
    # testunit.addTest(appTest.unitTest("test13"))
    # testunit.addTest(appTest.unitTest("test14"))
    # testunit.addTest(appTest.unitTest("test15"))
    testunit.addTest(appTest.unitTest("test16"))

    report_path = ".\\maintest2\\SoftTestReport_" + current_time  + '.html'   #生成测试报告的路径

    fp = open(report_path, "wb")
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description='自动化测试演示报告', tester='杨元杰')
    runner.run(testunit)
    fp.close()
    print("完成："+report_path)
