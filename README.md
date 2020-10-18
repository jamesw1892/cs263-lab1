# CS263 Lab 1

My code for lab 1, breaking simple encryption using Python 3. Tasks in `Tasks.pdf`.

# Ex1

Every password is a dictionary word. Cracked 96% with Caesar cipher and comparing to wordlist. Cracked the remaining 4% by using a Caesar shift of 0 (the remaining words weren't encrypted at all)!

# Ex2

2 emails to crack.

## Email 0

Cracked by using known word attack - guessed line 8 was "cheers" substituted those letters in the whole message. This made it easy to spot "successfully", word 5 on line 5 to fill in a few more, etc until all filled in.

## Email 1

The substitution from email 0 gave the first word to be the same as in email 1 - "carpsten" but the others are different. This suggests polyalphabetic substition, where the substitution changes every word.

Can also use known word attack on the 1-letter word which must be either "a" or "i".

# Ex3

Cracked 95% by hashing words in wordlists and comparing with hashes