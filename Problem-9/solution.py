from collections import Counter #Import Counter for easy word counting.

import string

text = "The sun shines over the lake. The lake is calm and beautiful. Sun is life."

#Define stopwords
stopwords = {'the', 'is', 'and'}

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
most_common_word, freq=word_counts.most_common(1)[0] #most_common_word, freq =This is tuple unpacking. It takes the two parts of the tuple:most_common_word & frequency
                                                     #.most_common(1) means:Give me the 1 most common item (i.e., just the top one).
                                                     #[0] means indexing, where 0 is first value in the imdex. that means we want the most_common_word in index first then put frequency in 2nd index

print("Most frequent word:", most_common_word)
print("Frequency:", freq)                                                  