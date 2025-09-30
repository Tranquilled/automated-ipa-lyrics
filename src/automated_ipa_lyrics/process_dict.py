from os import sys
from pathlib import Path
import jsonlines
import ipdb
import wikipron


def download_wiki_dict(lang_code: str) -> None:
    """
    TODO: add POS functionality to Wikipron
    """
    config = wikipron.Config(key="fra")  # French, with default options.
    output_file = Path(f"../../raw_dicts/{lang_code}.tsv")
    output_file.parent.mkdir(exist_ok=True, parents=True)
    with open(output_file, "w") as f:
        for word, pron in wikipron.scrape(config):
            ipdb.set_trace()
            f.write(f"{word}\t{pron}")


def process_kaikki_dict(filename: Path) -> None:
    """
    Processes a manually-downloaded scrape of Wiktionary (1 language
    at a time) from Kaikki.
    """
    output_file = f"{filename.stem}_trimmed.jsonl"
    phonemic_inventory = set()
    with jsonlines.open(output_file, "w") as f:
        for line in jsonlines.open(filename, "r"):
            word = line["word"]  # Case-sensitive: consider "Job"
            # ipdb.set_trace()
            ipa_values = line.get("sounds")
            if not ipa_values:
                continue
            try:
                ipa = [d for d in ipa_values if "ipa" in d][0]["ipa"].replace("\\", "")
            except Exception:
                if set(word.lower()) < phonemic_inventory:
                    ipa = word
            trimmed = {
                "source": word,
                "ipa_values": ipa,
                "pos": line["pos"]  # part of speech
            }
            phonemic_inventory |= set(ipa)
            f.write(trimmed)


def word_to_syllables(word_ipa: str):
    syllables = []
    current = ""
    # for char in word_ipa:
    #     if char in 


if __name__ == "__main__":
    # filename = sys.argv[1]
    # filename = Path(filename)
    # process_kaikki_dict(filename)
    download_wiki_dict("fra")