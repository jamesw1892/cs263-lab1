EMAIL_FILENAMES = [
    "email0.txt",
    "email1.txt"
]

def caesar():

    with open(EMAIL_FILENAMES[0]) as f:
        contents = f.read()

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

def permut():

    pass

def main():

    # yielded no results apart from first word could be mr
    # caesar()

    permut()

if __name__ == "__main__":
    main()
