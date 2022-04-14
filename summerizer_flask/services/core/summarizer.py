from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from .utils import load_config_section

CONF = load_config_section("MODEL")


def AwesomeFunction(QueryText: str) -> list:

        print("Loading a model")

        model = AutoModelForSeq2SeqLM.from_pretrained(CONF["model_name"])
        tokenizer = AutoTokenizer.from_pretrained(CONF["tokenizer_name"])

        # TODO: It returns text with <s></s>. I should solve it
        inputs = tokenizer(QueryText, return_tensors="pt")
        prediction = model.generate(**inputs)
        decoded = tokenizer.batch_decode(prediction)
        return decoded
