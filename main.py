from spacy.cli.download import download as download_spacy
from csify.csify import Csify
import spacy
import deepl

if __name__ == '__main__':
    try:
        spacy_en = spacy.load("en_core_web_sm")
    except:
        download_spacy("en_core_web_sm")
        spacy_en = spacy.load("en_core_web_sm")
    try:
        spacy_jp = spacy.load("ja_core_news_sm")
    except:
        download_spacy("ja_core_news_sm")
        spacy_en = spacy.load("ja_core_news_sm")
    translator = deepl.Translator('4ae11136-c75e-afc3-2b1b-5024fda6e6d0:fx')
    code_switcher = Csify(spacy_en,spacy_jp,translator)
    print(code_switcher.en_to_cs("if my instinct when i was in hysteria mode is correct, we have a chance!"))
    print(code_switcher.ja_to_cs("最初はうまく いかなかったんだよ"))
