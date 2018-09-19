# Hash Brute Force
## written in python 3.5
Powerful python hash cracker, was built by myself for [Hack this site](https://www.hackthissite.org/) challanges. However, it could be used anywhere else. :)


this software is owned and written by **flying8lack** using python, all it does is ask you to input hash type, hash, minimal possible length of the
original password (put 0 if you don't know) and level of possible characters.

This program will first attempt cracking the hash using the rainbow table [hash_db.txt](hash_db.txt). If it fails it will try to brute force, until it reach maximum of 10 character in length.

you can edit your own rainbow table, but make sure it follow the following format:

```
algorithm_name:hashed_password:original_password
```
#########################################################################################

Available levels:
1. (0-9)
2. (0-9 and a-z)
3. (0-9, a-z and A-Z) *pick this if you don't know*
4. (a-z)
5. (A-Z)
