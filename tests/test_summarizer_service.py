from base_test import BaseTest
from summerizer_flask.services.core import summarizer


class TestSummarizerService(BaseTest):
    #TODO: it should run based on schedule, because it long running procees
    def AwesomeFunction_test(self):
        summerizer_obj = summarizer.Summarizer()
        summerized_list = summerizer_obj.AwesomeFunction("")
        self.assertIsInstance(summerized_list, list)
        self.assertGreater(len(summerized_list), 0)
