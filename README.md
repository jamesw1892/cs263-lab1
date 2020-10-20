# CS263 Lab 1

My code for lab 1, breaking simple encryption using Python 3. Tasks in `Tasks.pdf`.

# Ex1

Every password is a dictionary word. Cracked 96% with Caesar cipher and comparing to wordlist. Cracked the remaining 4% by using a Caesar shift of 0 (the remaining words weren't enciphered at all)!

# Ex2

2 emails to crack.

## Email 0

Created dictionary mapping upper case ciphertext letters to lowercase plaintext letters. It started mapping everything to itself (capital to capital) and as I figured out the substitution, I changed it and made it lowercase. This means I can decipher it with the substitution (into `email0_adapted.txt`) and try to spot meaningful words using the lower case letters I think are correct amongst the upper case letters I have yet to figure out.

To actually figure out the substitution, I used a known word attack. First I guessed line 8 was "cheers" as it has a repeated letter in the right place and people usually sign off with "thanks", "best", "cheers" or similar. I added those substitutions to the dictionary, deciphered it again which made it easy to spot "successfully", word 5 on line 5. This made it easy to fill in a few more words and so on until all filled in. Some letters weren't in the ciphertext so couldn't fill in every character in the dictionary but email 0 was completely deciphered and we complete this in email 1.

## Email 1

Using the substitution from email 0 to decipher email 1, the first word was the same name as in the last line of email 0, however the rest was jiberish. As it worked for the whole word but nothing else, it seemed like a polyalphabetic cipher where the substitution changes when words change.

I guessed it could just shift each letter in email 0s substitution every word but didn't know by how many places. For each possible increment (1 to 25), I shifted the substitution by that many characters per word and outputted each decrypted version in a new line in `email1_adapted.txt`. The last line (shift of 25 AKA 1 backwards) seemed to make sense and I could use the techniques used in email 0 to fill in the final few letters that weren't in email 0. It also helped to check against the single letter word which must be either "a" or "i".