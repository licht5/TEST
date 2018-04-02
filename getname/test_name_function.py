# coding:utf-8
import unittest
from  getname.name_function import get_line_len
class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name=get_line_len(8)
        self.assertEqual(formatted_name,18)