"""
Word Occurrences
Estimate: 35 minutes
Actual:    12 minutes
"""

WORD_TO_OCCURRENCES = {}

text = input("text: ")

for word in text.split():
    if word in WORD_TO_OCCURRENCES:
        WORD_TO_OCCURRENCES[word] += 1
    else:
        WORD_TO_OCCURRENCES[word] = 1

for words, occurrences in WORD_TO_OCCURRENCES.items():
    print(f"{words}: {occurrences}")