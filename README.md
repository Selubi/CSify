CSify
======
Generate code-switched texts from monolingual texts.

If you got here by DOI citation on papers, this might be a snapshot of the repository during the time of writing.
The latest release can be found below.

[![GitHub version](https://badge.fury.io/gh/Selubi%2FCSify.svg)](https://badge.fury.io/gh/Selubi%2FCSify)
[![PyPI version](https://badge.fury.io/py/csify.svg)](https://badge.fury.io/py/csify)
[![DOI](https://zenodo.org/badge/543922457.svg)](https://zenodo.org/badge/latestdoi/543922457)

This repository is an implementation of our paper "Generating Code-Switched Text from Monolingual Text with Dependency
Tree," accepted for publication at [ALTA 2022](https://aclanthology.org/2022.alta-1.12/).

The demo for this code is available [here](https://csify.selubi.tech/).

In this documentation, we define the notation [X]-[Y] as code switched sentence with X language as the base language and
Y language as the inserted language.
We use ISO 639-1 Code for our naming convention. For example, JA-KO means a Japanese-Korean code switched text generated
from a monolingual Japanese text.


Setup
======
This package is available at [PyPI](https://pypi.org/project/csify/). You can install with pip.

```commandline
pip install csify
```

This package only comes with [spaCy](https://spacy.io/) and contains no machine translator.

The CSify Class
======
The CSify class generates code-switched text from a monolingual base sentence by translating parts of it
to the language you want to insert via the translate function. **You need to bring your own machine translator**.
Here is an example code on generating EN-JA code-switched sentence
using [DeepL API](https://www.deepl.com/pro-api?cta=header-pro-api).

```python
from csify import CSify
import deepl

# Initialize DeepL machine translator
translator = deepl.Translator("<deepl_apikey>")

EN_TO_ENJA = {
  "spacy_model": "en_core_web_sm",
  "translate_func": lambda base_sentence:
  translator.translate_text(base_sentence, target_lang="JA").text.strip("。"),
  "space": ' '
}

code_switcher = CSify(**EN_TO_ENJA)
print(code_switcher.generate("your last report was more than two weeks ago."))
print(code_switcher.generate("our lives are not our own, from womb to tomb, we're bound to others."))
```

outputs

```text
your last report was 二週間以上前 .
私たちの人生は、自分だけのものではないのです、胎内から墓場まで , we 're bound to others . 
```

Upon initialization, the CSify class takes three arguments:

- spacy_model: The spaCy trained pipeline of the base sentence's language (e.g. "en_core_web_sm" for English).
  Here is the [list of available pipelines](https://spacy.io/models). Note that the pipeline MUST support dependency
  parsing. There is no need to download the spaCy pipeline beforehand. The Csify class will do it for you.
- translate_func : An str -> str function. It takes a text of the base sentence's language as input and outputs the
  input's inserted language translation. Wrap the machine translator's translate function to a new function. It is
  recommended to truncate all kinds of punctuation of the inserted language in this function as most of the translation
  will be done on subsentences, not complete sentences.
- space : default=' '. Word separator of the base language. Some languages, such as Chinese and Japanese, don't use
  space. In that case, space should be an empty string.

If you are using DeepL or Google Cloud Translation API,
there are already some pre-built function arguments for CSify class at [demo/deepl_args.py](demo/deepl_args.py)
and
[demo/google_translate_args.py](demo/google_translate_args.py) respectively. For example, to generate EN-ZH with DeepL,
the CSify function arguments look something like this

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
Adding more language pairs equates to adding a function argument combination for the Csify class. Do note that
base sentences can only be from languages that have Spacy trained parser pipeline. You can even bring your own machine
translator. The following code is an example template of using your custom machine translator to create DE-SV
code-switched
sentences.

```python
from csify import CSify
from my_awesome_translator import german_to_swedish_translator

my_translator = german_to_swedish_translator()
my_code_switcher_args = {
  "spacy_model": "de_core_news_sm",
  "translate_func": lambda base_sentence:
  my_translator.my_translate_function(base_sentence),
  "space": ' '
}
code_switcher = CSify(**my_code_switcher_args)
print(code_switcher.generate("Mein Name ist Sam, obwohl er kurz für Samantha ist."))
```

Setup - Demo
======

| :warning: WARNING |
|:---------------------------------------------------------------------------------------------------------|
| **Warning: The JESC demo translates around 100,000 characters. Pay attention to your API character limit!** |

- Clone this repository

```commandline
git clone https://github.com/Selubi/CSify.git
```

- Install library dependencies

```commandline
pip install -r requirements.txt
```

Setup either [DeepL API](https://www.deepl.com/pro-api?cta=header-pro-api)
or [Google Cloud Translation AI](https://cloud.google.com/translate) or both as machine translators.
Alternatively, you can bring your own machine translator. Refer to  [The CSify Class](#the-csify-class)
and [Adding More Language Pairs](#adding-more-language-pairs) for more details.

- For DeepL, get [DeepL API Key](https://www.deepl.com/en/docs-api) and insert the key
  in [demo/constants.py](demo/constants.py)

```python
deepl_apikey = "<insert deepl API key here>"
```

- For Google Cloud Translation AI, follow this [setup guide](https://cloud.google.com/translate/docs/setup) until
  "Create a service account key." You should get a JSON file. Save the JSON file and insert the path to it
  in [demo/constants.py](demo/constants.py).

```python
path_to_google_cloud_JSON_key = "<insert path to google cloud JSON key here>"
```

| :warning: WARNING                                                                                                 |
|:------------------------------------------------------------------------------------------------------------------|
| **It is recommended to assume [constants.py](demo/constants.py) as unchanged in git to prevent API key leakage.** |
| ```git update-index --assume-unchanged demo/constants.py ```                                                      |

DeepL is relatively easier to set up but has less supported language than Google Cloud Translation AI.


Demo: Generating EN-JA and JA-EN from [JESC Corpus](https://nlp.stanford.edu/projects/jesc/index.html)
======
Refer to the below snippet of [demo/main.py](demo/main.py).

```python
    """
    This demo function below is defined at ./demo.py
    It downloads and extracts the JESC split corpus, a parallel Japanese-English monolingual corpus.
    Of the extraction results located at ./data/split, we will take the test data (./data/split/test) that contains
    2000 lines and generate code-switched data from it.
    The result will be in 2 files:
    English sentences and code-switched sentences generated from it will be stored in ./data/CSified/EN-Code-Switched
    Japanese sentences and code-switched sentences generated from it will be stored in ./data/CSified/JA-Code-Switched
    This demo also features a progress bar that tracks how many sentences it has generated and its speed in 
    it/s (sentences per second).
    """
demo.generate_jesc_cs()
```

| :warning: WARNING                                                                                       |
|:--------------------------------------------------------------------------------------------------------|
| **Warning: this demo translates around 100,000 characters. Pay attention to your API character limit!** |
