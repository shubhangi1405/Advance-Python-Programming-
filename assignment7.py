import re

text = input("Enter text: ")

pattern = r'\w+@\w+\.\w+'

emails = re.findall(pattern, text)

print("Email addresses found:", emails)
