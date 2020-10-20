from typing import List

EMAIL_FILENAMES = [
    "email0.txt",
    "email1.txt"
]

sub_email0 = {
    'A': 'g',
    'B': 'y',
    'C': 'o',
    'D': 'r',
    'E': 'd',
    'F': 'q',
    'G': 'c',
    'H': 'v',
    'I': 'x',
    'J': 'k',
    'K': 't',
    'L': 'l',
    'M': 'e',
    'N': 'n',
    'O': 'p',
    'P': 'u',
    'Q': 'b',
    'R': 'j',
    'S': 's',
    'T': 'a',
    'U': 'h',
    'V': 'w',
    'W': 'm',
    'X': 'z',
    'Y': 'f',
    'Z': 'i'
}

def test_substitution_email0(email: str) -> str:
    """
    Returns possibly deciphered version of email 0
    """

    adapted_email = ""
    for char in email:

        # if char not in substition,
        # it is not a letter so leave as is
        if char in sub_email0:
            char = sub_email0[char]
        adapted_email += char

    return adapted_email

def shift_substitution(sub_current: dict, num_places: int) -> dict:
    """
    Edit entries in the substitution dictionary by shifting
    the output characters by num_places through the alphabet
    (wrapping around)
    """

    for cipherchar in sub_current:
        plainchar = sub_current[cipherchar]
        num = ord(plainchar)
        if 97 <= num <= 122:
            num = ((num - 97 + num_places) % 26) + 97
        plainchar = chr(num)
        sub_current[cipherchar] = plainchar

    return sub_current

def crack_email1(email: str) -> str:
    """
    Returns possibly deciphered version of email 1
    """

    adapted_email = ""
    for num_places in range(1, 25+1):
        sub_current = sub_email0.copy()
        for char in email:

            # when a new word starts, shift the substitution in
            # the dictionary by the given number of places
            if char == " ":
                sub_current = shift_substitution(sub_current, num_places)

            # substitute letters
            elif char in sub_current:
                char = sub_current[char]

            adapted_email += char
        adapted_email += "\n"

    return adapted_email

def main():

    # read emails into memory
    emails = []
    for email_filename in EMAIL_FILENAMES:
        with open(email_filename) as f:
            emails.append(f.read())

    # email 0
    adapted_email0 = test_substitution_email0(emails[0])
    with open("email0_adapted.txt", "w") as f:
        f.write(adapted_email0)

    # email 1
    adapted_email1 = crack_email1(emails[1])
    with open("email1_adapted.txt", "w") as f:
        f.write(adapted_email1)

if __name__ == "__main__":
    main()
