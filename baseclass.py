#coding:utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

class BaseClass(unittest.TestCase):
    """所有测试用例的基类，继承多浏览器执行"""
    '''
    def __init__(self, arg):
        super(BaseClass, self).__init__()
        self.arg = arg
    '''
    def setUp(self):
        browserlist = ['chrome','firefox']
        for browser in browserlist:
            self.driver = webdriver.Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=
                {
                    'browserName':browser,
                    'version':'',
                    'platform':'ANY',
                    'javascriptEnabled':True
                }
            )
            url = 'http://paisit.cnsuning.com/shanpai/index.htm'
            self.driver.get(url)
            #yield self.driver
    def tearDown(self):
        self.driver.quit()
    def test_01(self):
        '''测试明日预热链接'''
        tomtab = self.driver.find_element_by_id("2")    
        self.assertTrue(tomtab,u'明日预热标签未找到')
        tomtab.click()
        time.sleep(1)
        self.assertEqual(self.driver.current_url, "http://paisit.cnsuning.com/shanpai/tomorrow.htm")
if __name__ == '__main__':
    unittest.main()
        