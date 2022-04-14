from base_test import BaseTest
from summerizer_flask.services.core import utils


class UtilsTest(BaseTest):
    def jsonify_base_test(self, text_, result_tmp):
        json_result_ = utils.jsonify_content(content_list=text_)
        self.assertDictEqual(json_result_, result_tmp)
        self.assertEqual(len(json_result_), len(text_))

    def test_bad_type_of_content_list(self):
        "unittest for checking raising error in case of wrong arg type"
        with self.assertRaises(Exception):
            utils.jsonify_content(self.TEXT)
    def test_jsonify_one_content(self):
        """unit test for len(content_list)== 1"""
        self.jsonify_base_test([self.TEXT], self.json_template_one_key)

    def test_jsonify_multiple_content(self):
        """unit test for len(content_list) > 1"""
        text_ = [self.TEXT, self.TEXT]
        self.jsonify_base_test(text_, self.json_template_multiple_key)

    def test_detect_language(self):
        """Unittest for checking successful return"""
        lang = utils.detect_language(text=self.TEXT)
        self.assertEqual(lang, self.lang)

    def test_load_config_section_success(self):
        """Unittest for checking successful return"""
        conf = utils.load_config_section("MODEL")
        self.assertGreater(len(conf), 0)

    def test_load_config_section_fail(self):
        """Unittest for checking non existance section name"""
        conf = utils.load_config_section("")
        self.assertEqual(conf, None)
