import deepl
from constants import deepl_apikey
from google.cloud import translate_v2 as translate

# TODO: CLEAN UP GOOGLE TRANSLATE in both constants.py and here

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
    translator.translate_text(base_sentence, target_lang="ZH").text,
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

#  below here uses google translate
translate_client = translate.Client.from_service_account_json(
    "C:\\Users\\grego\\Downloads\\active-area-364315-0afbee343ee8.json")

JA_TO_JAKO = {
    "spacy_model": "ja_core_news_sm",
    "translate_func": lambda base_sentence:
    translate_client.translate(base_sentence, target_language="KO")["translatedText"],
    "space": ''
}

KO_TO_KOJA = {
    "spacy_model": "ko_core_news_sm",
    "translate_func": lambda base_sentence:
    translate_client.translate(base_sentence, target_language="JA")["translatedText"],
    "space": ''
}

ZH_TO_ZHKO = {
    "spacy_model": "zh_core_web_sm",
    "translate_func": lambda base_sentence:
    translate_client.translate(base_sentence, target_language="KO")["translatedText"],
    "space": ''
}

KO_TO_KOZH = {
    "spacy_model": "ko_core_news_sm",
    "translate_func": lambda base_sentence:
    translate_client.translate(base_sentence, target_language="ZH")["translatedText"],
    "space": ''
}

EN_TO_ENKO = {
    "spacy_model": "en_core_web_sm",
    "translate_func": lambda base_sentence:
    translate_client.translate(base_sentence, target_language="KO")["translatedText"],
    "space": ' '
}

KO_TO_KOEN = {
    "spacy_model": "ko_core_news_sm",
    "translate_func": lambda base_sentence:
    translate_client.translate(base_sentence, target_language="EN")["translatedText"],
    "space": ''
}
