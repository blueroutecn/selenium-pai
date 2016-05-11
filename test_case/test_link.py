#-*- coding:utf-8 -*-
import time
import sys
import HTMLTestRunner
import unittest
from BeautifulSoup import BeautifulSoup
import re
import random
import urllib2
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
siturl = "http://paisit.cnsuning.com/shanpai/"
items = []
html = urllib2.urlopen(siturl).read()
soup = BeautifulSoup(html)
itemlist = soup.findAll('input',id= re.compile("^itemId"))
for i in range(0,len(itemlist)):
    item = itemlist[i]['value']
    items.append(item)
print items
#randitem = random.choice(items)
randitem = '9920140912496'
itemid = "itemName_i_" + randitem
print itemid
'''
#截图文件路径
imagename = "D://test_result_//Screenshots//"+ itemid + ".png"
#login data
user = {"username":"593743227@qq.com","passwd":"1qaz2wsx"}

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
    def test_link01(self):        
        '''测试明日预热链接'''
        tomtab = self.driver.find_element_by_id("2")    
        self.assertTrue(tomtab,u'明日预热标签未找到')
        tomtab.click()
        time.sleep(1)
        self.assertEqual(self.current_url(), "http://paisit.cnsuning.com/shanpai/tomorrow.htm")
    def test_link02(self):
        '''测试历史拍卖链接'''
        histab = self.driver.find_element_by_id("3")    
        self.assertTrue(histab,u'历史拍卖标签未找到')
        histab.click()
        time.sleep(1)
        self.assertEqual(self.current_url(), "http://paisit.cnsuning.com/shanpai/bidhistory.htm")
    def test_link03(self):
        '''测试闪拍帮助链接'''
        helptab = self.driver.find_element_by_id("4")
        self.assertTrue(helptab,u'闪拍帮助标签未找到')  
        helptab.click()
        time.sleep(1)
        self.assertEqual(self.current_url(), "http://paisit.cnsuning.com/shanpai/help/help.htm")
    def test_link04(self):
        '''测试各场次tab'''
        tab = self.driver.find_element_by_xpath('/html/body/div[6]/div/div[1]/div[1]/div[1]/div/ul')
        tablist = tab.find_elements_by_tag_name('li')
        for i in range(1,len(tablist)+1):
            self.driver.find_element_by_name('index_today_tab_%s' %i).click()
            time.sleep(1)
            #print i
    def test_link05(self):
        '''测试我的闪拍链接跳转'''
        currentwindow = self.driver.current_window_handle
        member = 'https://passportsit.cnsuning.com/ids/login'
        mydeposit = self.driver.find_element_by_id('myDepositCart')
        self.assertTrue(mydeposit,u'未找到我的闪拍')
        mydeposit.click()
        time.sleep(2)
        allwindow = self.driver.window_handles
        for window in allwindow:
            if window != currentwindow:
                self.driver.switch_to_window(window)
                self.assertIn(member, self.current_url())

             
    def aatest_main_process(self):
        '''测试主流程'''
        mainwindow = self.driver.current_window_handle
        
        self.driver.find_element_by_id(itemid).click()
        self.driver.get_screenshot_as_file(imagename)
        #screenshot = self.driver.get_screenshot_as_png() #binary data embedded in html
        time.sleep(3)
        allwindows = self.driver.window_handles
        for window in allwindows:
            if window!=mainwindow:
                self.driver.switch_to_window(window)
        depbtn = self.driver.find_element_by_id("depositBtn_%s" %randitem)
        WebDriverWait(self.driver, 60).until(lambda the_driver:the_driver.find_element_by_id("depositBtn_%s" %randitem).is_displayed())
        depbtn.click()
        time.sleep(3)
        try:
            self.driver.switch_to_frame("iframeLogin")
            self.driver.find_element_by_id("loginName").clear()
            self.driver.find_element_by_id("loginName").send_keys(user["username"])
            self.driver.find_element_by_id("loginPassword").clear()
            self.driver.find_element_by_id("loginPassword").send_keys(user["passwd"])
            self.driver.find_element_by_id("loginBtn").click()
            self.driver.switch_to_window(mainwindow)
            time.sleep(3)
        except NoSuchFrameException, e:
            print "未找到登录窗口！"
        time.sleep(3)
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[@id="m-pay-tpl"]/div/div[2]/p[1]/input').click()
        self.driver.find_element_by_id('next-submit').click()
        time.sleep(2)
        self.driver.find_element_by_id('m-pay-submit').click()
    #except NoSuchElementException, e:
        #print u"未找到该元素！"
                     
if __name__ == '__main__':
    unittest.main()
    
    '''
    suite = unittest.TestLoader().loadTestsFromTestCase(PaiPcTest)
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime())
    filename = 'D://test_result//test_result_'+ timestr + '.html'
    print filename
    with open(filename,'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=1,title=u'闪拍PC测试报告',description=u'闪拍PC端基于UI的自动化测试')
        runner.run(suite)
    '''


        

