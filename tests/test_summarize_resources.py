"""
system test for resources.py
"""
import json
from base_test import BaseTest

from summerizer_flask import create_app


class TestMain(BaseTest):
    def setUp(self) -> None:
        self.app = create_app({"TESTING": True})
        return super().setUp()

    def test_summerize_200_response(self):
        """
        It checks status code 200
        """
        with self.app.test_client() as client:
            resp = client.get("/summ/", data={"text": self.TEXT})
            self.assertEqual(resp.content_type, "application/json")
            self.assertEqual(resp.status_code, 200)

    def test_summerize_422_response(self):
        """
        It checks status code 422
        """
        with self.app.test_client() as client:
            resp = client.get("/summ/", data={"text": self.unsuportted_text})
            self.assertEqual(resp.content_type, "application/json")
            self.assertEqual(resp.status_code, 422)

    def test_summerize_500_response(self):
        """
        It checks status code 500
        """
        with self.app.test_client() as client:
            resp = client.get("/summ/", data={"text": ""})
            self.assertEqual(resp.content_type, "application/json")
            self.assertEqual(resp.status_code, 500)
            # to be sure every exception has error message
            error_msg: dict = json.loads(resp.data)
            error_msg = str(list(error_msg.values())[0])
            self.assertGreater(len(error_msg), 0)

    def test_config(self):
        """
        check for config
        """
        self.assertFalse(create_app().testing)
        self.assertTrue(self.app.testing)
