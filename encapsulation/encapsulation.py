# 封装部分维护
from config.config_01 import locat_config
from selenium.webdriver.support.wait import WebDriverWait
import time
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class UIHandle():
	# 构造方法，用来接收selenium的driver对象
	@classmethod
	def __init__(cls, driver):
		cls.driver = driver

	# 输入地址@classmethod
	@classmethod
	def get(cls, url):
		cls.driver.get(url)

	# 关闭浏览器驱动
	@classmethod
	def quit(cls):
		cls.driver.quit()

	# 浏览器等待
	@classmethod
	def wait(cls):
		time.sleep(5)

	# element对象（还可加入try，截图等...）
	@classmethod
	def element(cls, page, element):
		# 加入日志
		# 加入隐形等待
		# 此处可以传入config_01中的dict定位参数,调用presence_of_element_located()判断元素是否存在
		el = WebDriverWait(cls.driver, 10).until(EC.presence_of_element_located(locat_config[page][element]))
		# 加入日志
		return el

	# send_keys方法
	@classmethod
	def Input(cls, page, element, msg):
		el = cls.element(page, element)
		el.send_keys(msg)

	# click方法
	@classmethod
	def Click(cls, page, element):
		el = cls.element(page, element)
		el.click()

	# 断言（获取元素值：与期望值相比）
	@classmethod
	def check(cls, page, element):
		el = cls.element(page, element)
		# 通过try抛出异常进行断言判断
		try:
			assert u'Hi,丹丹' == el.text
			print('Assertion test pass.')
		except Exception as e:
			print('Assertion test fail.', format(e))