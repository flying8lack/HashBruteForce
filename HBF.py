import hashlib
import itertools

print("###warning this application is written and owned by flying8lack###")
print("\n")

option_hash = input("hash-type(md5,md4,sha256 etc): ")
hash_in = input("hash: ")
poss_list_option = input("Level: ")
minimum_password_length = input("original value length(put 0 if you don't know): ")

#level check
if poss_list_option == '1':
    poss_list = '0123456789'
    
elif poss_list_option == '2':
    poss_list = '0123456789'+'abcdefghijklmnopqrstuvwxyz'
    
elif poss_list_option == '5':
    poss_list = 'abcdefghijklmnopqrstuvwxyz'.upper()
    
elif poss_list_option == '3':
    #pick this option if you don't know the possible characters in the hash password.
    poss_list = '0123456789'+'abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper()
    
elif poss_list_option == '4':
    poss_list = 'abcdefghijklmnopqrstuvwxyz'
    
elif poss_list_option == '5':
    poss_list = 'abcdefghijklmnopqrstuvwxyz'.upper()
    
else:
    print("no such input.")
    quit()
    
#poss_list = '0123456789'+'abcdefghijklmnopqrstuvwxyz'+'abcdefghijklmnopqrstuvwxyz'.upper()
print("cracking..")

with open("hash_db.txt", "r") as file:
    for password in file:
        
        password = password.split(":")
        if password[0] == option_hash:
            
            if password[1] == hash_in:
                print("password found, it was: %s" % password[2])
                
                op = input()
                quit()
            else:
                pass

        else:
            pass
        
print("dictionary attack did not work, trying brute force...")

for password_length in range(int(minimum_password_length), 10):
    
    for guess in itertools.product(poss_list, repeat=password_length):
        
        hash_attempt = hashlib.new(option_hash,(''.join(guess)).encode()).hexdigest()
        #print("tried "+''.join(guess))
        
        if hash_attempt == hash_in:
            print("found, it is: %s" % ''.join(guess))
            with open("hash_db.txt", "a") as file:
                
                file.write(option_hash+":"+hash_in+":"+(''.join(guess)+"\n"))
            op = raw_input()
            quit()
        else:
            pass
    
