import re
import requests
import sys

sources = {
    "french": ["https://fr.wiktionary.org/w/index.php?search="],
    "german": ["https://de.wiktionary.org/w/index.php?search="],
}

regexes = {
    "https://fr.wiktionary.org/w/index.php?search=": re.compile(r"\"Prononciation API\">(.+?)<\/span>")
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
            return(scrape)
    else:
        return f"{word}"
        

if __name__ == "__main__":
    try:
        word = sys.argv[1]
        language = sys.argv[2]
        print(lookup(word, language))
    except:
        print("Enter a word and its language")