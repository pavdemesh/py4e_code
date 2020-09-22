import urllib.request

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/regex_sum_42.txt')

counts = dict()

for line in fhand:
    words = line.decode().split()
    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

sorted_words = list()
for k, v in counts.items():
    sorted_words.append((v, k))
print(sorted_words)

sorted_words.sort(reverse=True)

for v, k in sorted_words[:6]:
    print("word \"{}\" has frequency of {}".format(k, v))
