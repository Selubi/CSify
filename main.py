# from spacy.cli.download import download as download_spacy
from csify.csify import Csify
import csify.deepl_args
import csify.google_translate_args
import csify.demo

#  This is a demo on how to use the Csify class
if __name__ == '__main__':
    en_sentence = "you are a good soldier, tup. it's time to go now."
    ja_sentence = "植民地とは征服されるものでした そして今日 国は買収されるものなのです"
    zh_sentence = "尽管我早晨六点到了售票处，但是我还没买到票"  # Even though I arrived at the ticket office at 6 am, I was still not able to buy a ticket.
    ko_sentence = "저는 어제 약국에 가서 약을 많이 샀어요."  # I went to the pharmacy and bought a lot of medicine yesterday.

    code_switcher = Csify(**csify.deepl_args.ZH_TO_ZHJA)
    print(code_switcher.generate(zh_sentence))

    code_switcher = Csify(**csify.google_translate_args.KO_TO_KOJA)
    print(code_switcher.generate(ko_sentence))
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
    csify.demo.generate_jesc_cs()
