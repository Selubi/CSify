from spacy.cli.download import download as download_spacy
from csify.csify import Csify
from constants import deepl_apikey
import spacy
import deepl
import csify.demo

#  This is a demo on how to use the Csify class
if __name__ == '__main__':
    #  Try loading spacy tokenizer (dependency parser) if loading fails, download it and try loading it again
    #  English Spacy
    try:
        spacy_en = spacy.load("en_core_web_sm")
    except:
        download_spacy("en_core_web_sm")
        spacy_en = spacy.load("en_core_web_sm")
    #  Japanese Spacy
    try:
        spacy_jp = spacy.load("ja_core_news_sm")
    except:
        download_spacy("ja_core_news_sm")
        spacy_jp = spacy.load("ja_core_news_sm")

    #  Initialize deepl translator
    translator = deepl.Translator(deepl_apikey)

    #  Pass the english parser, japanese parser, and translator to Csify class
    code_switcher = Csify(spacy_en, spacy_jp, translator)

    # Generate code switched sentence by inserting monolingual sentence to the methods of Csify class
    print(code_switcher.en_to_cs("if my instinct when i was in hysteria mode is correct, we have a chance!"))
    print(code_switcher.ja_to_cs("植民地とは征服されるものでした そして今日 国は買収されるものなのです"))

    """
    This demo function is located at ./csify/demo.py
    It downloads and extracts the JESC split corpus, a parallel Japanese-English monolingual corpus.
    Of the extraction results located at ./data/split, we will take the test data (./data/split/test) that contains
    2000 lines and generate code-switched data from it.
    The result will be in 2 files:
    English sentence and code-switched sentence generated from it will be stored in ./data/CSified/EN-Code-Switched
    Japanese sentence and code-switched sentence generated from it will be stored in ./data/CSified/EN-Code-Switched
    This demo also features a progress bar that tracks how many sentences it has generating and its speed in 
    it/s (sentences per second).
    """
    csify.demo.generate_jesc_cs(code_switcher)
