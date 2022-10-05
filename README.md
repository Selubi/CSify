CSify
======

Generate code-switched text from monolingual text.

This is an implementation of our paper "Generating Code-Switched Text from Monolingual
Text with Dependency Tree" currently evaluated for publication at ICNLP 2023.

Setup
======

- Install library dependencies

```commandline
pip install -r requirements.txt
```

Setup either [DeepL API](https://www.deepl.com/pro-api?cta=header-pro-api)
or [Google Cloud Translation AI](https://cloud.google.com/translate) or both as machine translators.
Alternatively you can bring your own machine translator. Refer to  [The Csify Class](#the-csify-class)
and [Adding More Language Pairs](#adding-more-language-pairs) for more details.

- For DeepL, get [DeepL API Key](https://www.deepl.com/en/docs-api) and insert the key
  in [./constants.py](./constants.py)

```python
deepl_apikey = "<insert deepl API key here>"
```

- For Google Cloud Translation AI, follow this [setup guide](https://cloud.google.com/translate/docs/setup) until
  "Create a service account key". You should get a json file. Save the json file and insert path to it
  in [./constants.py](./constants.py)

```python
path_to_google_cloud_JSON_key = "<insert path to google cloud JSON key here>"
```

DeepL is relatively easier to setup, but has less supported language compared to Google Cloud Translation AI.

If you only setup DeepL, to run the demo at [main.py](main.py), comment out the line below.

```python
import csify.google_translate_args
```

Vice versa if you only setup Google Cloud Translation AI.

The Csify Class
======
The Csify class is defined at [./csify/csify.py](./csify/csify.py).
It generates code switched text from a monolingual base sentence by translating parts of it
to the language you want to insert via the translate function.

```python
from csify.csify import Csify
import csify.deepl_args

code_switcher = Csify(**csify.deepl_args.EN_TO_ENJA)
print(code_switcher.generate("your last report was more than two weeks ago."))
print(code_switcher.generate("our lives are not our own, from womb to tomb, we're bound to others."))
```

outputs

```text
your last report was 二週間以上前 .
私たちの人生は、自分だけのものではないのです、胎内から墓場まで , we 're bound to others . 
```

We define the notation [X][Y] as code switched sentence with X language as the base language and Y language as the
inserted language.
We use ISO 639-1 Code for our naming convention. For example, JA-KO means a Japanese-Korean code switched text generated
from a monolingual Japanese text.

Upon initialization, the Csify class takes three arguement:

- spacy_model : The spacy trained pipeline of the base sentence's language (eg. "en_core_web_sm" for English).
  here are the [list of available pipelines](https://spacy.io/models). Note that the pipeline MUST support parser.
- translate_func : An str -> str function. It takes a text of base sentence's language as input and spits out the input'
  s
  inserted language translation. Wrap the machine translator with this function.
- space : default=' '. Word seperator of the base language. Some language such as Chinese and Japanese doesn't use
  space.
  In that case space should be an empty string.

If you are using DeepL or Google Cloud Translation API,
there are already some pre-built function arguements for Csify class at [./csify/deepl_args.py](./csify/deepl_args.py)
and
[./csify/google_translate_args.py](./csify/deepl_args.py) respectively. For example, to generate EN-ZH with DeepL,
the Csify function arguements looks something like this

```python
EN_TO_ENZH = {
    "spacy_model": "en_core_web_sm",
    "translate_func": lambda base_sentence:
    translator.translate_text(base_sentence, target_lang="ZH").text,
    "space": ' '
}
```

Adding More Language Pairs
======
Adding more language pairs equates to adding function arguement combination for the Csify class. Do note that
base sentences can only be from languages that have spacy trained parser pipeline. You can even bring your own machine
translator. The following code is an example template of using your custom machine translator to create DE-SV code
switched
sentences.

```python
from csify.csify import Csify
from bring_my_own_translator import german_to_swedish_translator

my_translator = german_to_swedish_translator()
my_code_switcher_args = {
    "spacy_model": "de_core_news_sm",
    "translate_func": lambda base_sentence:
    my_translator.my_translate_function(base_sentence),
    "space": ' '
}
code_switcher = Csify(**my_code_switcher_args)
print(code_switcher.generate("Mein Name ist Sam, obwohl er kurz für Samantha ist."))
```

Demo : Generating EN-JA and JA-EN from [JESC Corpus](https://nlp.stanford.edu/projects/jesc/index.html)
======
Refer to the below snippet of [./main.py](./main.py) last lines.

```text
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
    csify.demo.generate_jesc_cs()
```