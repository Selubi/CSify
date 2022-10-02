# from spacy.cli.download import download as download_spacy
from csify.csify import Csify
import csify.csify_args
import csify.demo

#  This is a demo on how to use the Csify class
if __name__ == '__main__':
    #  Create an English to Japanese code-switcher instance. Arguements are defined in ./csify_args.py
    en_to_enja_code_switcher = Csify(**csify.csify_args.EN_TO_ENJA)
    #  Generate code-switched sentence from monolingual sentence
    print(en_to_enja_code_switcher.generate("you are a good soldier, tup. it's time to go now."))

    # Create an Japanese to English code-switcher instance. Arguements are defined in ./csify_args.py
    ja_to_jaen_code_switcher = Csify(**csify.csify_args.JA_TO_JAEN)
    #  Generate code-switched sentence from monolingual sentence
    print(ja_to_jaen_code_switcher.generate("植民地とは征服されるものでした そして今日 国は買収されるものなのです"))

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
    # csify.demo.generate_jesc_cs()
