#-*- coding:utf-8 -*-
import time
import sys
import HTMLTestRunner
import unittest
import re
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#动态修改环境变量，导入自定义模块
try:
    sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    from common import SuperPath,SuperConfig,randitem
except ImportError, e:
    print "import moudle path fail,errinfo:%s" %e

siturl = SuperConfig.readconf('siturl','homeurl')

class PaiPcTest(unittest.TestCase):
    """测试闪拍pc"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Ie()
        #self.driver = webdriver.Firefox()
        self.driver.get(siturl)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def current_url(self):
        current_url = self.driver.current_url
        return current_url
    def current_window(self):
        current_window = self.driver.current_window_handle
        return current_window
    def switch_window(self,refwindow):
        '''切换到新窗口'''
        allwindow = self.driver.window_handles
        for window in allwindow:
            if window != refwindow:
                self.driver.switch_to_window(window)
    def test_link01(self):        
        '''测试明日预热链接'''
        tomtab = self.driver.find_element_by_id("2")    
        self.assertTrue(tomtab,u'明日预热标签未找到')
        tomtab.click()
        time.sleep(1)
        self.assertEqual(self.current_url(), "http://paisit.cnsuning.com/shanpai/tomorrow.htm")
        self.driver.get_screenshot_as_file(SuperPath.imagename(SuperPath.get_current_function_name()))
    def test_link02(self):
        '''测试历史拍卖链接'''
        histab = self.driver.find_element_by_id("3")    
        self.assertTrue(histab,u'历史拍卖标签未找到')
        histab.click()
        time.sleep(1)
        self.assertEqual(self.current_url(), "http://paisit.cnsuning.com/shanpai/bidhistory.htm")
        self.driver.get_screenshot_as_file(SuperPath.imagename(SuperPath.get_current_function_name()))
    def test_link03(self):
        '''测试闪拍帮助链接'''
        helptab = self.driver.find_element_by_id("4")
        self.assertTrue(helptab,u'闪拍帮助标签未找到')  
        helptab.click()
        time.sleep(1)
        self.assertEqual(self.current_url(), "http://paisit.cnsuning.com/shanpai/help/help.htm")
        self.driver.get_screenshot_as_file(SuperPath.imagename(SuperPath.get_current_function_name()))
    def test_link04(self):
        '''测试各场次tab'''
        tab = self.driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/div/ul')
        tablist = tab.find_elements_by_tag_name('li')
        for i in range(1,len(tablist)+1):
            self.driver.find_element_by_name('index_today_tab_%s' %i).click()
            time.sleep(1)
            self.driver.get_screenshot_as_file(SuperPath.imagename(SuperPath.get_current_function_name()))
    def test_link05(self):
        '''测试我的闪拍链接跳转'''
        current_window = self.current_window()
        member = 'https://passportsit.cnsuning.com/ids/login'
        mydeposit = self.driver.find_element_by_id('myDepositCart')
        self.assertTrue(mydeposit,u'未找到我的闪拍')
        mydeposit.click()
        time.sleep(2)
        self.switch_window(current_window)
        self.assertIn(member, self.current_url())
        self.driver.get_screenshot_as_file(SuperPath.imagename(SuperPath.get_current_function_name()))
    def test_link06(self):
        '''测试主页链接'''
        time.sleep(1)
        self.assertEqual(self.driver.current_url, siturl)
        self.driver.get_screenshot_as_file(SuperPath.imagename(SuperPath.get_current_function_name()))
    def test_link07(self):
        '''测试随机拍品链接'''
        current_window = self.current_window()
        self.driver.find_element_by_id(randitem()).click()
        time.sleep(2)
        self.switch_window(current_window)
        time.sleep(1)
        self.driver.get_screenshot_as_file(SuperPath.imagename(SuperPath.get_current_function_name()))
if __name__ == '__main__':
    unittest.main()
    


        

