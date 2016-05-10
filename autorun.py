#coding:utf-8
import os.path
import unittest
import HTMLTestRunner
import time

basedir = os.path.dirname(os.path.abspath(__file__))
def testcasedir():
	'''测试用例路径'''
	casedir = os.path.join(basedir,'testcase/')
	return casedir

def testresult():
	'''测试报告'''
	timestr = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
	resultdir = os.path.join(basedir,'test_result/')
	testreport = os.path.join(resultdir,'TestReport'+ timestr+'.htm')
	return testreport

def autorun():
	'''批量执行所有测试用例'''
	suite = unittest.defaultTestLoader.discover(
		testcasedir(),
		pattern='test_*.py',
		top_level_dir=None
		)

	with open(testresult()) as fp:
		runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title=u'闪拍UI自动化测试报告',\
			description=u'闪拍PC端UI自动化测试详细情况如下')
		runner.run(suite)
if __name__ = '__main__':
	autorun()