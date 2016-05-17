#coding:utf-8

import time
import re
import os
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
try:
    sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    from common import SuperPath,SuperConfig 
except ImportError, e:
    print "import moudle path fail,errinfo:%s" %e

url = SuperConfig.readconf('siturl','itemurl')
user = SuperConfig.readconf('sitlogin','user')
passwd = SuperConfig.readconf('sitlogin','passwd')
itemid = re.findall(r'\d+', url)[0]

class SmaFlow(unittest.TestCase):
    """docstring for SmaFlow"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
       
    def tearDown(self):
        self.driver.quit()

    def test_smaflow(self):
        '''测试s码缴保证金主流程'''
        mainwindow = self.driver.current_window_handle
        WebDriverWait(self.driver, 60).until(lambda the_driver:the_driver.find_element_by_id\
        ("depositBtn_%s" %itemid).is_enabled())
        #driver.find_element_by_name('shanpai_detail_Freemargin').click()
        self.driver.find_element_by_id("depositBtn_%s" %itemid).click()
        try:
            self.driver.switch_to_frame("iframeLogin")
            self.driver.find_element_by_id("loginName").clear()
            self.driver.find_element_by_id("loginName").send_keys(user)
            self.driver.find_element_by_id("loginPassword").clear()
            self.driver.find_element_by_id("loginPassword").send_keys(passwd)
            self.driver.find_element_by_id("loginBtn").click()
            self.driver.switch_to_window(mainwindow)
            time.sleep(3)
        except NoSuchFrameException, e:
            print "未找到登录窗口！"
        #driver.find_element_by_name('shanpai_detail_Freemargin').click()
        self.driver.refresh()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element_by_link_text('免保证金').is_displayed())
        self.driver.find_element_by_link_text('免保证金').click()
        self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div/div[2]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="m-pay-tpl"]/div/div[2]/p[1]/input').click()
        self.driver.find_element_by_id('next-submit').click()
        time.sleep(2)
        '''
        self.driver.find_element_by_id('m-use-code').send_keys('YNDACSUEKN5S2XFH')
        self.driver.find_element_by_id('m-use-submit').click()
        time.sleep(1)
        WebDriverWait(self.driver,60).until(lambda the_driver: the_driver.find_element_by_name('detail_action_bid_chujia').is_displayed())
        self.driver.find_element_by_name('detail_action_bid_chujia').click()
        self.driver.find_element_by_name('detail_action_bid_chujia').click()
        '''
if __name__ == '__main__':
    unittest.main()

