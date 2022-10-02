import deepl

from constants import deepl_apikey

translator = deepl.Translator(deepl_apikey)

EN_TO_ENJA = {
    "spacy_model": "en_core_web_sm",
    "translate_func": lambda base_sentence: (
        translator.translate_text(base_sentence, target_lang="JA")).text,
    "space": ' '
}

JA_TO_JAEN = {
    "spacy_model": "ja_core_news_sm",
    "translate_func": lambda base_sentence: (
        translator.translate_text(base_sentence, target_lang="EN-US").text.strip('.?!')),
    "space": ''
}
