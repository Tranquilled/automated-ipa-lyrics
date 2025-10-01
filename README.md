# Automated IPA lyrics

Many singers are accustomed or required to sing in languages that they are not familiar with as languages.
Furthermore, singing songs in the target language is an effective, fun, and time-honored way to learn a language.
Traditionally, especially for singers, one step of learning songs is to transcribe the pronunciation of the words (often alongside learning their meanings) in the International Phonetic Alphabet.
Alongside a relevant orthography/dialect guide, even broad-transcription IPA is a great tool for language-learning just to get the feel of the language on the tongue.

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
