from csify.csify import Csify
import csify.deepl_args
import csify.google_translate_args
import csify.demo

#  This is a demo on how to use the Csify class
if __name__ == '__main__':
    #  Initiate an EN-JA code-switcher.
    code_switcher = Csify(**csify.deepl_args.EN_TO_ENJA)
    print(code_switcher.generate("your last report was more than two weeks ago."))
    print(code_switcher.generate("our lives are not our own, from womb to tomb, we're bound to others."))
    #  Initiate an KO-JA code-switcher.
    code_switcher = Csify(**csify.google_translate_args.KO_TO_KOJA)
    print(code_switcher.generate("저는 어제 약국에 가서 약을 많이 샀어요."))
    """
    This demo function below is defined at ./csify/demo.py
    It downloads and extracts the JESC split corpus, a parallel Japanese-English monolingual corpus.
    Of the extraction results located at ./data/split, we will take the test data (./data/split/test) that contains
    2000 lines and generate code-switched data from it.
    The result will be in 2 files:
    English sentences and code-switched sentences generated from it will be stored in ./data/CSified/EN-Code-Switched
    Japanese sentences and code-switched sentences generated from it will be stored in ./data/CSified/JA-Code-Switched
    This demo also features a progress bar that tracks how many sentences it has generated and its speed in 
    it/s (sentences per second).
    """
    csify.demo.generate_jesc_cs()
