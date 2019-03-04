from selenium import webdriver
import unittest
import HTMLTestRunner
import time,os,datetime
from bs4 import BeautifulSoup
from BeautifulReport import BeautifulReport


if __name__ == '__main__':
	test_suite = unittest.TestSuite()
	dir = r"F:\webTest\testcase"
	discover = unittest.defaultTestLoader.discover(dir, pattern='*test.py', top_level_dir=None)
	for testcase in discover:
		for test in testcase:
			test_suite.addTests(test)
	now = time.strftime("%Y-%m-%M-%H-%M-%S", time.localtime(time.time()))
	reportName = now+"result.html"
	fn = "report\\"+now+"result.html"
	fp = open(fn, 'wb')
	runner = BeautifulReport(test_suite)
	runner.report(filename=reportName, description='测试报告', log_path='report\\')
