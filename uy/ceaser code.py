###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
# read the character's code (use ord())
...
# add one to the character's code
...
# replace new character code with its
# corresponding character (use chr())
...
# add encrypted character to encrypted text
...
ptext = 'The early bird catches the worm'
for char in ptext:
       print(chr(ord(char)+2))
    
   