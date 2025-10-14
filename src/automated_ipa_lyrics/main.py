import re
import requests
import sys
from phonemizer import phonemize
from phonemizer.separator import Separator

def phonemizer_process(source: str , lang: str ) -> str:
    phn = phonemize(
        source,
        language=lang,
        backend='espeak', # pretty good!! IPA!!
        separator=Separator(phone=None, word=' ', syllable='|'),
        strip=True,
        preserve_punctuation=True,
        language_switch="remove-flags",
        njobs=4)
    return phn


if __name__ == "__main__":
    print("Enter a string")
    source = input() or "des oiseaux heureux couvent dans un couvent"
    print("Enter its language code")
    language = input() or "fr-fr"
    print(phonemizer_process(source, language))
