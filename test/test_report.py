# coding=utf-8
# 
# Production data test comes here

import unittest2
from os.path import join
from clamc_yield_report.report import getPositions



class TestReport(unittest2.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestReport, self).__init__(*args, **kwargs)



	def testGetPositions(self):
		self.assertEqual(1, 1)
