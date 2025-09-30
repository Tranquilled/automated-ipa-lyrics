import epitran
import re
import requests
import sys

sources = {
    "french": ["https://fr.wiktionary.org/w/index.php?search="],
    "german": ["https://de.wiktionary.org/w/index.php?search="],
}

regexes = {
    "https://fr.wiktionary.org/w/index.php?search=": re.compile(
        r"\"Prononciation API\">(.+?)<\/span>"
    )
}


def search(url, regex):
    response = requests.get(url)
    try:
        found = regex.search(response.text)[1]
        return found.replace("\\", "").replace("/", "")
    except:
        return False


def lookup(word, language):
    for url in sources[language]:
        print(url + word)
        regex = regexes[url]
        print(regex)
        scrape = search(url + word, regex)
        if scrape and len(scrape) > 0:
            return scrape
    else:
        return f"{word}"


def main(filename, language):
    with open(filename, "r") as f:
        original = f.read()
    original = (
        original.replace("\n", " ")
        .lower()
    )


def epitran_process(source: str, lang_code: str) -> str:
    epi = epitran.Epitran(lang_code)
    output = epi.transliterate(source)
    print(output)
    return output


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        language = sys.argv[2]

    except:
        print("Enter a string")
        source = input()
        print("Enter its language code")
        language = input()
        epitran_process(source, language)
