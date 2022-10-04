from csify.csify import Csify
import csify.deepl_args
import csify.google_translate_args
import csify.demo

#  This is a demo on how to use the Csify class
if __name__ == '__main__':
    en_sentence = "you are a good soldier, tup. it's time to go now."
    en_sentence2 = "so you quit school and quit looking for work and decided to become a chef"
    ja_sentence = "しかし社会的弱者と危機に瀕しているグループに力点を置いています"
    ja_sentence2 = "あなたにはそうかもしれないが 私そう思わない"
    zh_sentence = "尽管我早晨六点到了售票处，但是我还没买到票"  # Even though I arrived at the ticket office at 6 am, I was still not able to buy a ticket.
    zh_sentence2 = "商家的诚信和口碑有着密不可分的联系。"  # The integrity of a business is closely linked to its reputation
    ko_sentence = "저는 어제 약국에 가서 약을 많이 샀어요."  # I went to the pharmacy and bought a lot of medicine yesterday.

    code_switcher = Csify(**csify.deepl_args.EN_TO_ENZH)
    print(code_switcher.generate(en_sentence))

    code_switcher = Csify(**csify.google_translate_args.JA_TO_JAHI)
    print(code_switcher.generate(ja_sentence2))
    """
    This demo function below is defined at ./csify/demo.py
    It downloads and extracts the JESC split corpus, a parallel Japanese-English monolingual corpus.
    Of the extraction results located at ./data/split, we will take the test data (./data/split/test) that contains
    2000 lines and generate code-switched data from it.
    The result will be in 2 files:
    English sentence and code-switched sentence generated from it will be stored in ./data/CSified/EN-Code-Switched
    Japanese sentence and code-switched sentence generated from it will be stored in ./data/CSified/JA-Code-Switched
    This demo also features a progress bar that tracks how many sentences it has generating and its speed in 
    it/s (sentences per second).
    """
    # csify.demo.generate_jesc_cs()
