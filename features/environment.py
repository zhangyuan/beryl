import os
import sys
from selenium import webdriver

sys.path.insert(0, os.path.dirname(__file__) + '/lib')

def before_feature(context, feature):
    context.driver.delete_all_cookies()

def after_feature(context, feature):
    pass
    
def before_all(context):
    context.driver = webdriver.Firefox()

def after_all(context):
    context.driver.quit()
