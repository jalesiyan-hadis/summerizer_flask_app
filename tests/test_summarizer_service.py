from base_test import BaseTest
from summerizer_flask.services.core import summarizer


class TestSummarizerService(BaseTest):
    def test_AwesomeFunction(self):
        summerizer_obj = summarizer.Summarizer()
        summerized_list = summerizer_obj.AwesomeFunction(self.TEXT)
        self.assertIsInstance(summerized_list, list)
        self.assertGreater(len(summerized_list), 0)
