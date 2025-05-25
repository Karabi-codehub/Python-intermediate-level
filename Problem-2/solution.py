import ast  # Needed to safely convert string input into Python list

#creating a function called group_anagrams that takes a list of words.
def group_anagrams(words):
    
    # Create an empty dictionary to store grouped anagrams
    anagram_dict={}
    
    #go through each word one by one in the list
    for word in words:
        
        #Sort the letters of the word.
        sorted_word=''.join(sorted(word)) #sorted(word):This splits the word into letters and sorts them alphabetically,sorted("bat") → ['a', 'b', 't']
                                          #''.join(...):This takes the list ['a', 'b', 't'] and joins it back into one string
                                          # "bat" becomes "abt" & "tab" also becomes "abt".So, they are anagrams!
       
        if sorted_word in anagram_dict: # If we've already seen this sorted version before.anagram_dict = { "abt": ["bat"]}
            anagram_dict[sorted_word].append(word) #add the word to that group.anagram_dict = ["abt": ["bat", "tab"]]
        
        else:
            anagram_dict[sorted_word]=[word] #If it's a new sorted word, start a new group with the word
            
            
    return list(anagram_dict.values())

#out input is tag format , tags: ["bat", "tab", "cat", "act"]. want to let the user enter something like:
user_input=input("Enter tags in format(tags:[\"word1\",\"word2\",\"word3\",......]):") #takes user input as a string.

#Test a piece of code that might cause an error — and handle that error without crashing your program
#est a piece of code that might cause an error — and handle that error without crashing your program.number = int("abc")  # ❌ This will crash with a ValueError
#With try, you can handle it: try:number = int("abc") 
                              #except:print("❌ That was not a number!")

try:
    tag_start=user_input.index('[') # where the tag part begins
    tag_part=user_input[tag_start:] #cuts the input from the [ onward — so we now have only the tag part
                                    #before,tags: ["bat", "tab", "cat", "act"].after,["bat", "tab", "cat", "act"]
    tags=ast.literal_eval(tag_part) #Safely convert the string to a list
                                    #ast= Abstract Syntax Trees.We use ast to safely read strings that look like Python data (lists, dicts, etc)
                                    #literal_eval=literal evaluate.A function inside ast.It takes a string'["tea", "bat"]'  turns it into ["tea", "bat"](Real Python list)

except Exception as error: #If the input is wrong (like missing brackets or quotes), this will catch the error and show a message
    print("❌ Invalid input format.")
    exit()
    
#Grouping Anagrams
grouped=group_anagrams(tags)

print("Tags:",tags)
print("Grouped Anagrams:",grouped)

