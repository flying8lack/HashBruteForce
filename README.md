#Hash Brute Force
## written in python 3.5
Python Hash Cracker, was built by myself for [Hackthissite](https://www.hackthissite.org/) challanges, but could be used anywhere else :)


this software is owned and written by **flying8lack** using python, all it does is ask you to input hash type, hash, minimal posssible length of the
original password (put 0 if you don't know) and level of possible characters.

this program will first attempt using the rainbow table [hash_db.txt](hash_db.txt), if it fails it will try brute force attack until it reach maximum of 10 character in length.

you can edit your own rainbow table, but make sure it follow the following format:

```
algorithm_name:hashed_password:original_password
```
#########################################################################################

available levels:
1. (0-9)
2. (0-9 and a-z)
3. (0-9, a-z and A-Z)
4. (a-z)
