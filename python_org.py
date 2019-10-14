from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(
    ChromeDriverManager().install())
driver.get("http://www.python.org/downloads")
assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# elem = driver.find_elements_by_xpath("//a[text()='Downloads']")[0]

# driver.implicitly_wait(10)
# ActionChains(driver).move_to_element(elem).click(elem).perform()

# elem = driver.find_elements_by_xpath("//a[text()='All releases']")[0]
# elem.click()
driver.implicitly_wait(5)

# elem = driver.find_elements_by_css_selector(
#     "a[href='/downloads/release/python-374/']")[0]
# print(elem)
# print(elem.text)
# ActionChains(driver).move_to_element(elem).click(elem).perform()
elems = driver.find_elements_by_xpath(
    "//a[contains(., 'Download Python')]")
for elem in elems:
    print("-------")
    print(elem.text)
    print(elem.tag_name)
    # print(elem.tag)
elems[0].click()
# elem.click()
# body = driver.find_element_by_tag_name("body")
# body.send_keys(Keys.CONTROL + 't')
# driver.findElement(By.cssSelector("body")).sendKeys(Keys.CONTROL + "t")
# time.sleep(2)
# driver.close()
