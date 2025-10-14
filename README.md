<<<<<<< HEAD
# Automated IPA transcriber

## Corpus processing (once)
Process the corpus to determine all allowable maps between letter combinations and *phonemes* (not phones -- broad definition of each sound to decrease the size of phonetic vocabulary).

Lexeme-phoneme pair is stored as a line with conditions (part of speech, etc.), if any, following.
Lexeme is the *maximum length* that matches a unique phoneme(?).

## Source processing


## Mapping
Syllables are language-dependent and assembled from either a consonant group and a vowel or recognized groups of vowels (diphthongs).
Sandhis/intervocalics/etc. are language-dependent and are inserted based on metadata in the 2 adjoining words/syllables.

## Challenges and assumptions

- For ease of interoperability, this project doesn't use narrow transcription.
That means the difference between \ʁ\ in French and German is ignored.
Similarly, whether \ʁ\ is allophonic to \x\ is ignored: it might be in some accents, but that can be dealt with using...

- ...specified IPA charts.
A common challenge in singing is sticking with one accent, which is to say sticking with one phonetic mapping.
If a different accent is desired, that means switching to a different mapping.
The same goes for names and foreign words: the point of the project is to impose a single, specified mapping on the input text.

## Discovering IPA charts
Restricting the problem space to that of art song makes it easy to find a broad transcription charts: a language is a dialect with an army, a navy, and the [default Wikipedia Help:IPA chart](https://en.wikipedia.org/wiki/Help:IPA/Czech).
Alas, this is illusory ease.
All languages have idiosyncratic features that defy simple search-and-replace: they have loanwords and all manner of [context](https://en.wikipedia.org/wiki/Assimilation_(phonology))-[dependent](https://en.wikipedia.org/wiki/Sandhi) [pronunciation](https://en.wikipedia.org/wiki/Elision) [change](https://en.wikipedia.org/wiki/Intervocalic_consonant).
So while the [basic IPA chart](https://en.wikipedia.org/wiki/Help:IPA/Czech) is of great help to anyone trying to actually learn a language, it's insufficient for automated transcription.

Thankfully, the Wikimedia project has also collected reams of IPA transcriptions of words.
These can be used to get a more accurate search-and-replace, that recognizes "women" as a single block corresponding to \wɪmɪn\ rather than 6 characters pronounced \womɛn\ ("woe-men").
>>>>>>> readme
