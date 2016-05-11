#coding:utf-8

import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
browserlist = ['chrome','firefox','ie']
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=
    {
        'browserName':'chrome',
        'version':'',
        'platform':'ANY',
        'javascriptEnabled':True
    }
)
driver.get('http://paisit.cnsuning.com/shanpai/detail/item/9920140912530.htm')
driver.implicitly_wait(5)
driver.maximize_window()
mainwindow = driver.current_window_handle
WebDriverWait(driver, 60).until(lambda the_driver:the_driver.find_element_by_id("depositBtn_9920140912530").is_enabled)
driver.find_element_by_id('depositBtn_9920140912530').click()
try:
    driver.switch_to_frame("iframeLogin")
    driver.find_element_by_id("loginName").clear()
    driver.find_element_by_id("loginName").send_keys("593743227@qq.com")
    driver.find_element_by_id("loginPassword").clear()
    driver.find_element_by_id("loginPassword").send_keys("1qaz2wsx")
    driver.find_element_by_id("loginBtn").click()
    driver.switch_to_window(mainwindow)
    time.sleep(3)
except NoSuchFrameException, e:
    print "未找到登录窗口！"
#driver.find_element_by_name('shanpai_detail_Freemargin').click()
driver.refresh()
time.sleep(3)
WebDriverWait(driver, 60).until(lambda the_driver:the_driver.find_element_by_id("depositBtn_9920140912530").is_enabled())
driver.find_element_by_id('depositBtn_9920140912530').click()
driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div/div[2]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="m-pay-tpl"]/div/div[2]/p[1]/input').click()
driver.find_element_by_id('next-submit').click()
time.sleep(2)
driver.find_element_by_id('m-pay-submit').click()
time.sleep(3)
allwindows = driver.window_handles
print allwindows
for window in allwindows:
    if window != mainwindow:
        driver.switch_to_window(window)
        time.sleep(5)
        driver.find_element_by_id('fund-eppBalanceAmount').click()
        time.sleep(2)
        driver.find_element_by_id('sec').send_keys('123qwe')
        driver.find_element_by_xpath('//*[@id="validateForm"]/div[1]/a').click()
    else:
        pass
        print mainwindow
driver.switch_to_window(mainwindow)
driver.refresh()
time.sleep(2)
WebDriverWait(driver,60).until(lambda the_driver: the_driver.find_element_by_name('detail_action_bid_chujia').is_displayed())
driver.find_element_by_name('detail_action_bid_chujia').click()
driver.find_element_by_name('detail_action_bid_chujia').click()

js = 'alert("bid success!");'
driver.execute_script(js)
driver.switch_to_alert().dismiss()
driver.switch_to_window(mainwindow)
#WebDriverWait(driver, 15).until(lambda driver:driver.find_element_by_class_name('winBidTip-pay').is_enabled())
#driver.find_element_by_class_name('winBidTip-pay').click()

