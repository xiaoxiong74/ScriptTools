from selenium import webdriver
import time
browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

##demo1
# browser.get('http://www.baidu.com/')
# print(browser.page_source)
# browser.close()

##demo2
#################查找元素####################
#单个元素查找
# browser.get("http://www.taobao.com")
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)
# browser.close()

# 这里列举一下常用的查找元素方法：
#
# find_element_by_name
# find_element_by_id
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

# 下面这种方式是比较通用的一种方式：这里需要记住By模块所以需要导入
# from selenium.webdriver.common.by import By
# browser.get("http://www.taobao.com")
# input_first = browser.find_element(By.ID,"q")
# print(input_first)
# browser.close()


#多个元素查找
#其实多个元素和单个元素的区别，举个例子：find_elements,单个元素是find_element,其他使用上没什么区别，通过其中的一个例子演示
# browser.get("http://www.taobao.com")
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# browser.close()

# 当然上面的方式也是可以通过导入from selenium.webdriver.common.by import By 这种方式实现
#
# lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
#
# 同样的在单个元素中查找的方法在多个元素查找中同样存在：
# find_elements_by_name
# find_elements_by_id
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector


#################元素交互操作####################

#对于获取的元素调用交互方法
# browser.get("http://www.taobao.com")
# input_str = browser.find_element_by_id('q')
# input_str.send_keys("ipad")
# time.sleep(1)
# input_str.clear()
# input_str.send_keys("MakBook pro")
# button = browser.find_element_by_class_name('btn-search')
# button.click()
# browser.close()



# 交互动作
#
# 将动作附加到动作链中串行执行
# from selenium.webdriver import ActionChains
#
#
# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 执行JavaScript
# 这是一个非常有用的方法，这里就可以直接调用js方法来实现一些操作，
# 下面的例子是通过登录知乎然后通过js翻到页面底部，并弹框提示
# browser.get("http://www.zhihu.com/explore")
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')


# 获取元素属性
# get_attribute('class')

# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))
# browser.close()


url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
browser.close()