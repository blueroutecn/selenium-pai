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
    def __init__(self, host, browser):
        super(BaseClass, self).__init__()
        self.host = host
        self.browser = browser
    '''

    def getbrowser(self):
        browserlist = {
            'http://192.168.1.4:5555/wd/hub': 'chrome',
            'http://192.168.1.4:5556/wd/hub': 'internet explorer',
            #'http://192.168.1.4:5557/wd/hub': 'firefox'
        }

        for host, browser in browserlist.items():
            print host, browser
            driver = webdriver.Remote(
                command_executor=host,
                desired_capabilities=
                {
                    'browserName': browser,
                    'version': '',
                    'platform': 'ANY',
                    'javascriptEnabled': True
                }
            )
            yield driver

    def setUp(self):
        print "Testing started!"

        url = 'http://www.jd.com/'
        self.driver = self.getbrowser().next()
        self.driver.get(url)

    def tearDown(self):
        print "Testing stoped!"
        self.driver.quit()
    '''
    def test_01(self):
        """测试明日预热链接"""
        self.driver.find_element_by_link_text("服装城").click()
        time.sleep(3)
    '''
if __name__ == '__main__':
    unittest.main()
