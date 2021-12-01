from base_test import BaseTest
from summerizer_flask.services.models import summarizer_model


# integration test
class TestSummarizeModel(BaseTest):
    def test_summarize_text_successful(self):
        # Test for succesful result
        result = summarizer_model.summarize_text(text=self.TEXT)
        self.assertIsInstance(result, dict)

    def test_unsupported_language(self):
        """unittest for unsupported language"""
        result = summarizer_model.summarize_text(text="Das ist auf deutsch")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
