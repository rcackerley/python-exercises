sentence = raw_input("Please enter a sentence.").lower()
histogram = {}

for word in sentence.split():
    if word in histogram:
        histogram[word] += 1
    else: 
        histogram[word] = 1
print histogram
