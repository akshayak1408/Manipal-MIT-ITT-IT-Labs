import re
text = input("Enter a text: ")
clean_text = re.sub(r'[^\w\s]', '', text)
print("Text with punctuations removed:", clean_text)
