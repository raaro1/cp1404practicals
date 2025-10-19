"""
Word Occurrences
Estimate: 35 minutes
Actual:    30 minutes
"""

WORD_TO_OCCURRENCES = {}

text = input("text: ").lower()

for word in text.split():
    if word in WORD_TO_OCCURRENCES:
        WORD_TO_OCCURRENCES[word] += 1
    else:
        WORD_TO_OCCURRENCES[word] = 1

width = max(len(word) for word in WORD_TO_OCCURRENCES)

for word, count in sorted(WORD_TO_OCCURRENCES.items()):
    print(f"{word:{width}} : {count}")