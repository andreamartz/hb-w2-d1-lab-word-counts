"""Count words in file."""

# put your code here.
#open the file in read mode

#find how many times each word repeats or is used
# split each line into words
#output each word and the number of times it shows up
# bonus: add the r arg back in and see if it all still works

word_counts = {}

# { 'As': 1, 'I': 2 }

file= open('twain.txt')

for line in file:
    line = line.strip()
    words = line.split(' ')   # returns a list
    for word in words:
        # word_counts[word] = word_counts[word] + 1
        # print(word_counts.get(word, 0))
        word_counts[word] = word_counts.get(word, 0) + 1
        
    # print(line)

print(word_counts)
