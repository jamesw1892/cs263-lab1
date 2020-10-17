from typing import List

EMAIL_FILENAMES = [
    "email0.txt",
    "email1.txt"
]

sub_id = {
    'A': 'a',
    'B': 'b',
    'C': 'c',
    'D': 'd',
    'E': 'e',
    'F': 'f',
    'G': 'g',
    'H': 'h',
    'I': 'i',
    'J': 'j',
    'K': 'k',
    'L': 'l',
    'M': 'm',
    'N': 'n',
    'O': 'o',
    'P': 'p',
    'Q': 'q',
    'R': 'r',
    'S': 's',
    'T': 't',
    'U': 'u',
    'V': 'v',
    'W': 'w',
    'X': 'x',
    'Y': 'y',
    'Z': 'z'
}

# cheers, line 8
# successfully line 5 word 5
# then filled in rest
sub_known_words = {
    'A': 'g',
    'B': 'y',
    'C': 'o',
    'D': 'r',
    'E': 'd',
    'F': 'q',
    'G': 'c',
    'H': 'v',
    'I': 'I', # not in ciphertext
    'J': 'J', # not in ciphertext
    'K': 't',
    'L': 'l', # itself
    'M': 'e',
    'N': 'n', # itself
    'O': 'p',
    'P': 'u',
    'Q': 'b',
    'R': 'r',
    'S': 's', # itself
    'T': 'a',
    'U': 'h',
    'V': 'w',
    'W': 'm',
    'X': 'X', # not in ciphertext
    'Y': 'f',
    'Z': 'i'
}


def caesar(emails: List[str]):

    contents = emails[0]

    outs = [contents]
    for shift in range(1, 25+1):
        out = ""
        for char in contents:
            num = ord(char)
            if 65 <= num <= 90:
                num = ((num - 65 + shift) % 26) + 65
            out += chr(num)
        outs.append(out)

    for out in outs:
        print(out)
        input()
        print("\n\n\n\n")

def test_substitution(emails: List[str]) -> List[str]:

    adapted_emails = []
    for email in emails:
        adapted_email = ""
        for char in email:

            # if char not in substition,
            # it is not a letter so leave as is
            if char in sub_known_words:
                char = sub_known_words[char]
            adapted_email += char

        adapted_emails.append(adapted_email)

    return adapted_emails

def main():

    # read emails into memory
    emails = []
    for email_filename in EMAIL_FILENAMES:
        with open(email_filename) as f:
            emails.append(f.read())

    # yields no results apart from first word could be mr
    # caesar(emails)

    # yields only the word cheers making sense
    adapted_emails = test_substitution(emails)

    for index, adapted_email in enumerate(adapted_emails):
        filename = "email{}_adapted.txt".format(index)
        with open(filename, "w") as f:
            f.write(adapted_email)

if __name__ == "__main__":
    main()
