import string
def longest_world(sentence):
    # Remove punctuation from the sentence
    #str.maketrans(from_chars, to_chars, remove_chars)
    #Replace characters in from_chars with the ones in to_chars.
    #Remove characters in remove_chars
    #In our case:str.maketrans('', '', string.punctuation) We are saying: from_chars = '' → Nothing to change.
                                                                         #to_chars = '' → No new characters to add.
                                                                         #remove_chars = string.punctuation → Just remove all punctuation!
    cleaned_sentence= sentence.translate(str.maketrans('','',string.punctuation))
    
    # Split sentence into words
    words = cleaned_sentence.split()
    if words:
        word=max(words,key=len) # key=len tells Python: Compare the items by their lengths, not by the actual strings.
        return word
    else:
        return " "

input_sentence=input("Enter a Sentence:")
print("Longest word:",longest_world(input_sentence))

