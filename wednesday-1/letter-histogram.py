word = raw_input("Please enter a word.").lower()
histogram = {}

for letter in range(0, len(word)):
    print word[letter]
    if word[letter] in histogram:
        histogram[word[letter]] += 1
    else:
        histogram[word[letter]] = 1

print histogram
