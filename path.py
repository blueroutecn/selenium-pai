#coding:utf-8
import os
import time
import inspect

timestr = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())

class SuperPath(object):
    """测试结果文件路径类"""
    def __init__(self):
        super(SuperPath, self).__init__()
        #self.arg = arg       
    @staticmethod
    def basepath():
        path = os.path.abspath(os.path.dirname(__file__))
        return path
    @staticmethod
    def imagepath(dir='screen_shot'):
        resultpath = os.path.join(SuperPath.basepath(),'test_result')
        if os.path.exists(resultpath):
            os.chdir(resultpath)
        else:
            os.mkdir(resultpath)
            os.chdir(resultpath)
        if os.path.exists(dir):
            screenshot_dir = os.path.abspath(dir)
        else:
            os.mkdir(dir)
            screenshot_dir = os.path.abspath(dir)
        os.chdir(screenshot_dir)
        if os.path.exists(timestr):
            screenshot_subdir = os.path.abspath(timestr)
        else:
            os.mkdir(timestr)
            screenshot_subdir = os.path.abspath(timestr)
        return screenshot_subdir
    @staticmethod
    def imagename(name):
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
        imagename = os.path.join(SuperPath.imagepath(),name +'_' + timestamp + '.jpeg')
        return imagename
    @staticmethod
    def get_current_function_name():
        '''获取当前调用方的函数名称'''
        return inspect.stack()[1][3]

    def testfunction(self):
        '''测试获取当前的函数名称'''
        #funcinfo = inspect.getmembers(self.testfunction)
        #funcname = dict(funcinfo)['func_name']
        funcname = SuperPath.get_current_function_name()
        return funcname     #返回当前函数名称testfunction

if __name__ == '__main__':
    #print SuperPath.imagepath()
    #print SuperPath.imagename('test')
    h = SuperPath()
    print h.testfunction()


    

