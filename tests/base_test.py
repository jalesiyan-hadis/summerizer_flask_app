"""
It is not a runable test function.
It is just a Base Class as a Parent for runable Test class to reduce duplicate varibles
"""
from unittest.case import TestCase

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class BaseTest(TestCase):
    def setUp(self) -> None:

        self.TEXT = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
        A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
        Only 18 days after that marriage, she got hitched yet again."""
        self.unsuportted_text = "Es ist auf Deutsch"
        self.lang = "en"
        self.json_template_one_key = {"summary": self.TEXT}
        self.json_template_multiple_key = {
            "summary_1": self.TEXT,
            "summary_2": self.TEXT,
        }
