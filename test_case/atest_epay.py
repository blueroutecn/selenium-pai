#coding:utf-8

import time
import re
import os
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
try:
    sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    from common import SuperPath,SuperConfig 
except ImportError, e:
    print "import moudle path fail,errinfo:%s" %e

url = SuperConfig.readconf('siturl','itemurl')
user = SuperConfig.readconf('sitlogin','user')
passwd = SuperConfig.readconf('sitlogin','passwd')
itemid = re.findall(r'\d+', url)[0]

class EpayFlow(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_epayflow(self):
        '''测试易付宝支付保证金主流程'''
        mainwindow = self.driver.current_window_handle
        WebDriverWait(self.driver, 60).until(lambda the_driver:the_driver.find_element_by_id\
        ("depositBtn_%s" %itemid).is_enabled)
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
        WebDriverWait(self.driver, 60).until(lambda the_driver:the_driver.find_element_by_id\
        ("depositBtn_%s" %itemid).is_enabled())
        self.driver.find_element_by_id("depositBtn_%s" %itemid).click()
        self.driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div/div[2]/a').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="m-pay-tpl"]/div/div[2]/p[1]/input').click()
        self.driver.find_element_by_id('next-submit').click()
        time.sleep(2)
        self.driver.find_element_by_id('m-pay-submit').click()
        time.sleep(3)
        allwindows = self.driver.window_handles
        #print allwindows
        for window in allwindows:
            if window != mainwindow:
                self.driver.switch_to_window(window)
                time.sleep(5)
                self.driver.find_element_by_id('fund-eppBalanceAmount').click()
                time.sleep(2)
                self.driver.find_element_by_id('sec').send_keys('123qwe')
                self.driver.find_element_by_xpath('//*[@id="validateForm"]/div[1]/a').click()
            else:
                pass
                #print mainwindow
        self.driver.switch_to_window(mainwindow)
        self.driver.refresh()
        time.sleep(2)
        WebDriverWait(self.driver,60).until(lambda the_driver: the_driver.find_element_by_name\
        ('detail_action_bid_chujia').is_displayed())
        self.driver.find_element_by_name('detail_action_bid_chujia').click()
        self.driver.find_element_by_name('detail_action_bid_chujia').click()

        js = 'alert("bid success!");'
        self.driver.execute_script(js)
        self.driver.switch_to_alert().dismiss()
        self.driver.switch_to_window(mainwindow)
        #WebDriverWait(driver, 15).until(lambda driver:driver.find_element_by_class_name('winBidTip-pay').is_enabled())
        #driver.find_element_by_class_name('winBidTip-pay').click()

if __name__ == '__main__':
    unittest.main()

