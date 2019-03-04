from encapsulation.encapsulation import UIHandle
from constant import costant_1
from config.config_01 import browser_config
from time import sleep

def login(email_msg, password_msg):
	url = costant_1.LOGIN_URL
	# 打开浏览器
	driver = browser_config['firefox']()
	# 传入driver对象
	uihandle = UIHandle(driver)
	# 输入url地址
	uihandle.get(url)
	# 调用二次封装后的方法，此处可见操作了哪个页面，哪个元素，msg是要插入的值，插入值得操作在另外一个用例文件中传入
	uihandle.Input('login_page','email', email_msg)
	uihandle.Input('login_page', 'password', password_msg)
	uihandle.Click('login_page', 'loginButton')
	uihandle.wait()
	uihandle.check('home_page', 'account')
	uihandle.quit()
