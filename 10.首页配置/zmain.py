import time
import unittest

import HTMLTestReport
import unitTest
if __name__ == "__main__":
    '''生成测试报告'''

    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
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
    # testunit.addTest(landTest.landTest("test11"))
    # testunit.addTest(landTest.landTest("test12"))
    # testunit.addTest(landTest.landTest("test13"))
    # testunit.addTest(landTest.landTest("test14"))
    # testunit.addTest(landTest.landTest("test15"))
    # testunit.addTest(landTest.landTest("test16"))
    # testunit.addTest(landTest.landTest("test17"))
    # testunit.addTest(landTest.landTest("test18"))
    # testunit.addTest(landTest.landTest("test19"))
    # testunit.addTest(landTest.landTest("test20"))
    # testunit.addTest(landTest.landTest("test21"))
    # testunit.addTest(landTest.landTest("test22"))
    # testunit.addTest(landTest.landTest("test23"))
    # testunit.addTest(landTest.landTest("test24"))
    report_path = ".\\test\\" + current_time + '.html'  # 生成测试报告的路径
    fp = open(report_path, "wb")
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description='自动化测试演示报告', tester='童峻涛')
    runner.run(testunit)
    fp.close()
    print("完成："+report_path)
