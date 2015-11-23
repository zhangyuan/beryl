from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from nose.tools import *
import helper
import settings

@given("Open products page")
def open_products_page(context):
  context.driver.get(settings.products_url)


@when('search by keyword "{keyword}"')
def search_products_by_keyword(context, keyword):
  WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "searchForm")))
  element = context.driver.find_elements_by_css_selector(".searchForm input")[0]
  element.send_keys(keyword)

@then('only products match the keyword "{keyword}" should be shown')
def show_products_with_keyword(context, keyword):
  elements = context.driver.find_elements_by_css_selector(".dataList .dataNode")
  ok_(len(elements) > 0, "no element with %r found" % keyword)

  for e in elements:
    ok_(helper.is_element_contains_keyword(e, keyword), "product without the keyword %r" % keyword)
