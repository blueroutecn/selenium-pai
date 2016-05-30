#coding:utf-8

import unittest
import sys
import os.path
import time
from selenium import webdriver


try:
    sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    from baseclass import BaseClass
except ImportError, e:
    print "import moudle path fail, errinfo:%s" %e


class JdTest(BaseClass):
    """测试京东链接"""

    def atest_link(self):
        """测试用例中循环调用多浏览器"""
        browserlist = {
                'http://192.168.1.4:5555/wd/hub': 'chrome',
                'http://192.168.1.4:5556/wd/hub': 'internet explorer',
                #'http://192.168.1.4:5557/wd/hub': 'firefox'
            }

        for host, browser in browserlist.items():
            print "Testing on: %s" % browser
            print host, browser
            self.driver = webdriver.Remote(
                command_executor=host,
                desired_capabilities=
                {
                    'browserName': browser,
                    'version': '',
                    'platform': 'ANY',
                    'javascriptEnabled': True
                }
            )
            self.driver.get("http://www.jd.com/")
            self.driver.find_element_by_link_text("服装城").click()
            time.sleep(3)
            self.driver.quit()

    def test_link02(self):
        """测试多线程方式启动"""
        self.driver.find_element_by_link_text("服装城").click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()


