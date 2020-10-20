import os
from hashlib import md5

PASSWORD_FILENAME = "tabula_staff_passwords.txt"
CRACKED_FILENAME = "tabula_staff_passwords_cracked.txt"
WORDLISTS_DIR = os.path.join(os.path.pardir, "wordlists")

def hash(s: str) -> str:
    return md5(s.encode()).hexdigest()

def main():

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

    for wordlist_filename in os.listdir(WORDLISTS_DIR):
        with open(os.path.join(WORDLISTS_DIR, wordlist_filename)) as f:
            for line in f:
                line = line.replace("\n", "")

                # hash each word from each wordlist
                line_hash = hash(line)

                line_num = 0
                with open(PASSWORD_FILENAME) as g:
                    for password_hash in g:

                        # only try to crack uncracked passwords
                        if answers[line_num] == "":
                            password_hash = password_hash.replace("\n", "")

                            # if the hash matches, we know the word is the password
                            if line_hash == password_hash:
                                print("{} decrypted is {}".format(line_hash, line))
                                answers[line_num] = line
                                with open(CRACKED_FILENAME, "w") as f:
                                    f.write("\n".join(answers) + "\n")
                        line_num += 1

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
