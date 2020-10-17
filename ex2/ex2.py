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
    'L': 'l',
    'P': 'p',
    'Q': 'q',
    'T': 't',
    'U': 'u',
    'V': 'v',
    'W': 'w',
    'Y': 'y',
    'Z': 'z'
}

# use known word "cheers"
sub_cheers = dict() #sub_id.copy()
sub_cheers["G"] = "c"
sub_cheers["U"] = "h"
sub_cheers["M"] = "e"
sub_cheers["D"] = "r"
sub_cheers["S"] = "s"

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
            if char in sub_cheers:
                char = sub_cheers[char]
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
