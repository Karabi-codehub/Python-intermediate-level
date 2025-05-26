from collections import Counter #Import Counter for easy word counting.

import string #Imports string module so we can easily access punctuation characters (like ., ,, !, etc.).

#Take blog content input from user
text = input("Enter blog text: ")


#Define stopwords
#Asks the user to enter words they want to ignore (called stopwords). These are often common words like "the", "and", etc.
stop_word_input = input("Enter stopwords:")


#stop_input.strip():Checks if the input is not empty or just spaces.
#stop_input.split(','):Splits the input string into a list of words based on commas ,.
#word.strip().lower():For each word:.strip() removes leading/trailing spaces & lower() makes it lowercase.
#set(...):Stores all the processed words in a set (no duplicates, unordered).
if stop_word_input.strip():
    stopwords = set(word.strip().lower() for word in stop_word_input.split(','))

#if the user did not enter any stopwords, it uses a default set of common stopwords.
else:
    stopwords = {'the', 'is', 'and', 'over', 'a', 'an', 'in', 'on', 'to', 'of', 'with', 'for', 'by', 'at', 'from'}

#Remove punctuation
# string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

#Convert to lowercase
cleaned_text = cleaned_text.lower()

#Split into words
words = cleaned_text.split()

#Remove stopwords
filtered_words = [word for word in words if word not in stopwords] 

#Count word frequencies
word_counts=Counter(filtered_words) #Counter(filtered_words): Counts how often each word appears.

#Find the most frequent word(s)
if word_counts:
    most_common_word, freq = word_counts.most_common(1)[0] #.most_common(1) means:Give me the 1 most common item (i.e., just the top one).
                                                           #[0] means indexing, where 0 is first value in the imdex. that means we want the most_common_word in index first then put frequency in 2nd index

    print("\n✅ Most frequent word:", most_common_word)
    print("📊 Frequency:", freq)         

else:
    print("\n⚠️ No valid words found after removing stopwords.")                                     