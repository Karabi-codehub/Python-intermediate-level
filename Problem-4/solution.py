import re

text = "Here is a code: 123a and another: 456B, but not 12a or 7899c"

# Define the pattern: 3 digits followed by one letter
pattern = r"\d{3}[a-zA-Z]"

# Find all matches in the text
matches = re.findall(pattern, text)

print("Matches found:", matches)