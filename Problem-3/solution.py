import re # Import regex module

text = "My code is 123"

# Pattern: any three digits
pattern=r"\d{3}"  #\d: a digit (0–9)
                  #{3}: exactly 3 of them
               
# Search for the pattern
match=re.search(pattern,text) #re.search(...): Looks for the pattern in the text.

if match:
     print("Found a 3-digit number!")
else:
    print("No 3-digit number found.")
