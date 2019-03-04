from selenium import webdriver
import time

# config配置

# 浏览器种类维护
browser_config ={'firefox':webdriver.Firefox}

#定位信息维护
locat_config = {
	'login_page':{
		'email':['xpath','//form[1]//input[@type="email"]'],
        'password':['xpath','//form[1]//input[@type="password"]'],
		'loginButton':['xpath','//form[1]//button[@type="button"]']
	},
	'home_page':{
          'account':['xpath', '//*[@id="app"]/div/header/div[2]/span']
	}
}