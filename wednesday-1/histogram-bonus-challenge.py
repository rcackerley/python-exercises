from operator import itemgetter, attrgetter

sentence = raw_input("Please enter a sentence.").lower()
histogram = {}

for word in sentence.split():
    if word in histogram:
        histogram[word] += 1
    else: 
        histogram[word] = 1
#print histogram
sorted_histogram = sorted(histogram.items(), key=itemgetter(1), reverse=True)
print sorted_histogram[0]
print sorted_histogram[1]
print sorted_histogram[2]
#print sorted(histogram, key=lambda i: int(histogram[i]))
#print histogram