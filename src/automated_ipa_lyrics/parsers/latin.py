"""
No sandhis!
"""

MAX_FRAME = 3

SINGLES = {
    "ā": "aː",  # can I handle gemination as its own class of postprocessing?
    "b": "b",
    "d": "",
    # I swear to god these are ɛ but Wikipedia says they're e
    "e": "ɛ",
    "æ": "ɛ",
    "œ": "ɛ",
    "f": "f",
    "h": "",  # null in ecclesiastical
    "j": "j",
    "k": "k",
    "l": "l",
    "m": "m",
    "o": "ɔ",
    "ō": "oː",
    "p": "p",
    "q": "kʷ",  # dependent on preprocessing
    "r": "r",
    "s": "s",
    "u": "u",
    "v": "v",
    "y": "i",
    "z": "d͡z",
}

# I count diphthongs as equivalent to 2 consecutive vowels, sue me
DOUBLES = {}

SUCCEEDING_DEPENDENTS = {
    "c": {
        "h": "k",
        "a": "ka",
        "o": "ko",
        "u": "ku",
        "e": "t͡ʃɛ",
        "æ": "t͡ʃɛ",
        "œ": "t͡ʃɛ",
        "i": "t͡ʃi",
        "y": "t͡ʃi",
    },
    "g": {
        "a": "ga",
        "o": "go",
        "u": "gu",
        "n": "ɲ",
        "e": "d͡ʒɛ",
        "æ": "d͡ʒɛ",
        "œ": "d͡ʒɛ",
        "i": "d͡ʒi",
        "y": "d͡ʒi",
    },
    "i": {},
    "n": {},
    "t": "t", 
    "ti": "t͡s",
    "xc": "ksk", 
    "xcæ": "kʃɛ", 
    "xcœ": "kʃɛ", 
    "xci": "kʃi", 
    "xcy": "kʃi"
}


INTERVOCALICS = {
    "i": "jː",
    "h": "k",
    "s": "z",
    "x": "gz",  # technically only before stress; TODO: change this after stress implemented
}

class Phoneme:
    def __init__(self, lexeme: str):
        self.lexeme = lexeme

    def lookup(self):
        l = self.lexeme
        if l in SINGLES:
            self.p = SINGLES[l]
        if l[0] in SUCCEEDING_DEPENDENTS:
            self.p = SUCCEEDING_DEPENDENTS[l[0]][l[1:]]


def preprocess(raw: str) -> str:
    return (
        raw.replace("ae", "æ").replace("oe", "œ").replace("rh", "r").replace("ph", "f")
    )


def process_source(raw: str) -> list[str]:
    lexemes = []
    while len(raw):
        pass
