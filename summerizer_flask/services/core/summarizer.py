from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from .utils import load_config_section

CONF = load_config_section("MODEL")


class Summarizer:
    def __init__(self):
        print("Loading a model")

        self.model = AutoModelForSeq2SeqLM.from_pretrained(CONF["model_name"])
        self.tokenizer = AutoTokenizer.from_pretrained(CONF["tokenizer_name"])

    def AwesomeFunction(self, QueryText: str) -> "something":
        # TODO: It returns text with <s></s>. I should solve it
        inputs = self.tokenizer(QueryText, return_tensors="pt")
        prediction = self.model.generate(**inputs)
        decoded = self.tokenizer.batch_decode(prediction)
        return decoded
