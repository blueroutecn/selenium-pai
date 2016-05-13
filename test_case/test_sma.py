#coding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

'''
#打开首页随机选取拍品
items = []
html = urllib2.urlopen(siturl).read()
soup = BeautifulSoup(html)
itemlist = soup.findAll('input',id= re.compile("^itemId"))
for i in xrange(0,len(itemlist)):
    item = itemlist[i]['value']
    items.append(item)
print items
#randitem = random.choice(items)
randitem = '9920140912496'
itemid = "itemName_i_" + randitem
print itemid
'''

browserlist = ['chrome','firefox','ie']
for browser in browserlist:
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=
        {
            'browserName':browser,
            'version':'',
            'platform':'ANY',
            'javascriptEnabled':True
        }
    )
    driver.get('http://paisit.cnsuning.com/shanpai/detail/item/9920140912530.htm')
    driver.implicitly_wait(30)
    driver.maximize_window()
    mainwindow = driver.current_window_handle
    WebDriverWait(driver, 60).until(lambda the_driver:the_driver.find_element_by_id("depositBtn_9920140912530").is_displayed())
    #driver.find_element_by_name('shanpai_detail_Freemargin').click()
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
    WebDriverWait(driver, 10).until(lambda driver:driver.find_element_by_link_text('免保证金').is_displayed())
    driver.find_element_by_link_text('免保证金').click()
    driver.find_element_by_xpath('/html/body/div[21]/div/div/div/div/div[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="m-pay-tpl"]/div/div[2]/p[1]/input').click()
    driver.find_element_by_id('next-submit').click()
    time.sleep(2)
    '''
    driver.find_element_by_id('m-use-code').send_keys('YNDACSUEKN5S2XFH')
    driver.find_element_by_id('m-use-submit').click()
    time.sleep(1)
    WebDriverWait(driver,60).until(lambda the_driver: the_driver.find_element_by_name('detail_action_bid_chujia').is_displayed())
    driver.find_element_by_name('detail_action_bid_chujia').click()
    driver.find_element_by_name('detail_action_bid_chujia').click()
    '''

