MORSE_CODE_DICT = {
    "A": "▄ ▄▄▄",
    "B": "▄▄▄ ▄ ▄ ▄",
    "C": "▄▄▄ ▄ ▄▄▄ ▄",
    "D": "▄▄▄ ▄ ▄",
    "E": "▄",
    "F": "▄ ▄ ▄▄▄ ▄",
    "G": "▄▄▄ ▄",
    "H": "▄ ▄ ▄ ▄",
    "I": "▄ ▄",
    "J": "▄ ▄▄▄ ▄▄▄ ▄▄▄",
    "K": "▄▄▄ ▄ ▄▄▄",
    "L": "▄ ▄▄▄ ▄ ▄",
    "M": "▄▄▄ ▄▄▄",
    "N": "▄▄▄ ▄",
    "O": "▄▄▄ ▄▄▄ ▄▄▄",
    "P": "▄ ▄▄▄ ▄▄▄ ▄",
    "Q": "▄▄▄ ▄▄▄ ▄ ▄▄▄",
    "R": "▄ ▄▄▄ ▄",
    "S": "▄ ▄ ▄",
    "T": "▄▄▄",
    "U": "▄ ▄ ▄▄▄",
    "V": "▄ ▄ ▄ ▄▄▄",
    "W": "▄ ▄▄▄ ▄▄▄",
    "X": "▄▄▄ ▄ ▄ ▄▄▄",
    "Y": "▄▄▄ ▄ ▄▄▄ ▄▄▄",
    "Z": "▄▄▄ ▄▄▄ ▄ ▄",
    "0": "▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄",
    "1": "▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄",
    "2": "▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄",
    "3": "▄ ▄ ▄ ▄▄▄ ▄▄▄",
    "4": "▄ ▄ ▄ ▄ ▄▄▄",
    "5": "▄ ▄ ▄ ▄ ▄",
    "6": "▄▄▄ ▄ ▄ ▄ ▄",
    "7": "▄▄▄ ▄▄▄ ▄ ▄ ▄",
    "8": "▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄",
    "9": "▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄",

}


def translation(s):

    morse = ""
    s = s.upper()
    for char in s:
        if char in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[char] + "   "
        elif char == " ":
            morse += "       "
        else:
            morse += char + "   "

    morse = morse[:-3]
    return morse


sentence = str(input("Type a sentence to translate to Morse Code: "))

morse_sentence = translation(sentence)
print(morse_sentence)
