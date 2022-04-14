from typing import Dict, Union,List
from langdetect import detect_langs
import configparser
import os

CONFIG_ADDRESS = os.path.join(os.path.dirname(__file__), "config.ini")


def jsonify_content(content_list: List[str])->dict:
    """Function for convert the list to the json format
    

    Args:
        content_list (List[str]): _description_

    Returns:
        dict: _description_
    Examples
    --------
    >>> list_ = ["sample text1", "sample text2"]
    >>> m = utils.jsonify_content(list_)
    >>> m
    {"summery_1":"sample text1",
     "summery_2":"sample text2"}
    """
    assert isinstance(content_list,list), "content_list should be a list"
    tmp_dict = {}
    if len(content_list) > 1:
        for num, content in enumerate(content_list, start=1):
            tmp_key = "_".join(["summary", str(num)])
            tmp_dict[tmp_key] = content
    elif len(content_list) == 1:
        tmp_dict["summary"] = content_list[0]
    return tmp_dict


def detect_language(text: str) -> str:
    """
    Function for recognizing language
    if accuracy>0.9 consider text with specific language otherwise it consider that as mixed language

    Args:
        text (str): _description_

    Returns:
        str: _description_
    Examples
    --------
    >>> text = "sample text1"
    >>> m = utils.detect_language(text)
    >>> m
    "en"
    """
    detected_language = detect_langs(text)[0]
    ACCURRACY = float(load_config_section(section="LANG_INFO")["ACCURRACY"])
    assert float(detected_language.prob) > ACCURRACY, "text is mixed Language"
    return detected_language.lang


def load_config_section(section) -> Union[Dict, None]:
    """
    return specific Section from config.ini
    -------
    Parameters:
        section: name of the section key
        dtype : str

    Returns
    -------
    dict : dictionary
    None: if section does not exist
    -------
    Exception: if config.ini does not exist
    """
    config = configparser.ConfigParser()
    assert len(config.read(CONFIG_ADDRESS)) > 0, 'Config file does not exist'
    if section in config.sections():
        return config[section]
    else:
        return None
