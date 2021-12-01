"""
initiate summarizer class. so the pretrained model would be downloaded and save inside docker image.
"""
from summerizer_flask.services.core import summarizer


def main():
    print("downloading pretrained Model and tokenizer")
    # just for downloading pretrained model and save it inside docker image
    try:
        summarizer.Summarizer()
    except:
        # ignore exception. models could be downloaded when the class initiated.
        pass


if __name__ == "__main__":
    main()
