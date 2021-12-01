from typing import Union
from services.core import summarizer
from services.core import utils

LANG = utils.load_config_section("LANG_INFO")["LANG"]


def summarize_text(text: str) -> Union[dict, str]:
    assert len(text) > 0, "text is empty"
    try:
        # handling error message for unsupported/mixed Language
        txt_lang = utils.detect_language(text)
        assert (
            txt_lang == LANG
        ), "Your Text Language is: {}. BUT Supported Language is : {}".format(
            txt_lang, LANG
        )
    except Exception as e:
        return str(e)
    summerizer_obj = summarizer.Summarizer()
    summerized_list = summerizer_obj.AwesomeFunction(text)
    json_result = utils.jsonify_content(content_list=summerized_list)
    return json_result
