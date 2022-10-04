from constants import path_to_google_cloud_JSON_key
from google.cloud import translate_v2 as translate

translate_client = translate.Client.from_service_account_json(path_to_google_cloud_JSON_key)

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
