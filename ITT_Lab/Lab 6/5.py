import re
text = input("Enter the text: ")
pattern = input("Enter the pattern to find: ")
replacement = input("Enter the replacement string: ")
new_text = re.sub(pattern, replacement, text)
print("Original text:", text)
print("New text after replacement:", new_text)
