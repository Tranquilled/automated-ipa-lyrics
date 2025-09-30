# Automated IPA transcriber

## Corpus processing (once)
Process the corpus to determine all allowable maps between letter combinations and *phonemes* (not phones -- broad definition of each sound to decrease the size of phonetic vocabulary).

Lexeme-phoneme pair is stored as a line with conditions (part of speech, etc.), if any, following.
Lexeme is the *maximum length* that matches a unique phoneme(?).

## Source processing


## Mapping
Syllables are language-dependent and assembled from either a consonant group and a vowel or recognized groups of vowels (diphthongs).
Sandhis/intervocalics/etc. are language-dependent and are inserted based on metadata in the 2 adjoining words/syllables.
