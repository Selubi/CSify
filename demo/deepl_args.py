import deepl
from demo.constants import deepl_apikey

#  Pre-built DeepL arguments for the Csify class.

translator = deepl.Translator(deepl_apikey)

EN_TO_ENJA = {
    "spacy_model": "en_core_web_sm",
    "translate_func": lambda base_sentence:
    translator.translate_text(base_sentence, target_lang="JA").text,
    "space": ' '
}

JA_TO_JAEN = {
    "spacy_model": "ja_core_news_sm",
    "translate_func": lambda base_sentence:
    translator.translate_text(base_sentence, target_lang="EN-US").text.strip('.?!'),
    "space": ''
}

JA_TO_JAZH = {
    "spacy_model": "ja_core_news_sm",
    "translate_func": lambda base_sentence:
    translator.translate_text(base_sentence, target_lang="ZH").text.strip("。"),
    "space": ''
}

JA_TO_JAID = {
    "spacy_model": "ja_core_news_sm",
    "translate_func": lambda base_sentence:
    translator.translate_text(base_sentence, target_lang="ID").text.strip(".?!").lower(),
    "space": ''
}

EN_TO_ENID = {
    "spacy_model": "en_core_web_sm",
    "translate_func": lambda base_sentence:
    translator.translate_text(base_sentence, target_lang="ID").text.strip('.?!'),
    "space": ' '
}

EN_TO_ENZH = {
    "spacy_model": "en_core_web_sm",
    "translate_func": lambda base_sentence:
    translator.translate_text(base_sentence, target_lang="ZH").text,
    "space": ' '
}

ZH_TO_ZHEN = {
    "spacy_model": "zh_core_web_sm",
    "translate_func": lambda base_sentence:
    translator.translate_text(base_sentence, target_lang="EN-US").text.strip('.?!'),
    "space": ''
}

ZH_TO_ZHJA = {
    "spacy_model": "zh_core_web_sm",
    "translate_func": lambda base_sentence:
    translator.translate_text(base_sentence, target_lang="JA").text,
    "space": ''
}
