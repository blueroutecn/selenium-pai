#coding:utf-8
import os.path
import os
import unittest
import HTMLTestRunner
import time

'''闪拍PC端UI自动化测试'''
__author__ = "yinzx"
__version__ = "1.0"

basedir = os.path.dirname(os.path.abspath(__file__))


def testcasedir():
    """测试用例"""
    casedir = os.path.join(basedir,'test_case')
    return casedir


def testresult():
    """测试报告"""
    timestr = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
    resultdir = os.path.join(basedir, 'test_result')		#join会自动按系统添加路径分隔符
    testreport = os.path.join(resultdir, 'TestReport'+ timestr+'.html')
    return testreport


def autorun():
    """批量执行所有测试用例"""
    suite = unittest.defaultTestLoader.discover(
        testcasedir(),
        pattern='test_*.py',
        top_level_dir=None
        )

    with open(testresult(),'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title=u'闪拍UI自动化测试报告',\
            description=u'闪拍PC端UI自动化测试详细情况如下')
        runner.run(suite)
if __name__ == '__main__':
    autorun()