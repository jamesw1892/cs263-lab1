from typing import Union
import os

PASSWORD_FILENAME = "staff_passwords.txt"
CRACKED_FILENAME = "staff_passwords_cracked.txt"
WORDLISTS_DIR = os.path.join(os.path.pardir, "wordlists")

def caesar(password: str) -> Union[str, None]:
    """
    Crack the given password using caesar cipher with varies shifts
    AKA rot1, rot2, ..., rot13, ..., rot25
    """

    # calculate the possible plaintexts of the password,
    # 1 for each of the 25 shifts
    possible_plaintexts = []
    for shift in range(1, 25+1):
        possible_plaintext = ""
        for char in password:
            char_code = ord(char.upper())

            # if the character is a letter, shift it, otherwise leave it
            # this ignores punctuation
            if 65 <= char_code <= 90:
                char_code = ((char_code - 65 + shift) % 26) + 65

            possible_plaintext += chr(char_code)
        possible_plaintexts.append(possible_plaintext)

    # see if any word in any wordlist matches any of the possible plaintexts
    for wordlist_filename in os.listdir(WORDLISTS_DIR):
        with open(os.path.join(WORDLISTS_DIR, wordlist_filename)) as f:
            for line in f:
                line = line.replace("\n", "").upper()
                if line in possible_plaintexts:
                    return line

    # if no match was found
    return None

def crack(password: str) -> Union[str, None]:
    """
    Crack the given password
    """

    # found 96% by caesar
    return caesar(password)

def main():
    """
    Manage cracking passwords while offloading the actual cracking
    to the 'crack' function
    """

    # initialise file for cracked passwords if doesn't already exist
    if not os.path.exists(CRACKED_FILENAME):

        # get number of passwords to crack (and therefore how many lines
        # to create in cracked file)
        num_passwords = 0
        with open(PASSWORD_FILENAME) as f:
            for line in f:
                num_passwords += 1

        # write that many lines
        with open(CRACKED_FILENAME, "w") as f:
            f.write("\n" * num_passwords)

    # load currently cracked passwords into memory
    # uncracked passwords also have an empty equal to the empty string
    answers = []
    with open(CRACKED_FILENAME) as f:
        for line in f:
            answers.append(line.replace("\n", ""))

    found_new = False
    line_num = 0
    with open(PASSWORD_FILENAME) as f:
        for line in f:
            if answers[line_num] == "":

                # try to crack uncracked passwords
                password = line.replace("\n", "")
                answer = crack(password)

                # if successful, save it
                if answer is not None:
                    found_new = True
                    print("{} decrypted is {}".format(password, answer))
                    answers[line_num] = answer
            line_num += 1

    # write newly found passwords to file (if found any)
    if found_new:
        with open(CRACKED_FILENAME, "w") as f:
            f.write("\n".join(answers) + "\n")

def output_progress():
    """
    Output the number and percentage of passwords currently
    """

    num_cracked = 0
    total_num = 0
    with open(CRACKED_FILENAME) as f:
        for line in f:
            total_num += 1

            # have cracked it if that line is not empty
            if line.replace("\n", "") != "":
                num_cracked += 1

    print("Cracked {}/{} = {}%".format(num_cracked, total_num, round(num_cracked / total_num * 100)))

if __name__ == "__main__":
    main()
    output_progress()
