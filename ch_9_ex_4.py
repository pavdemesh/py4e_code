# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhandle = open(fname, "r")

senders = dict()

for line in fhandle:
    line = line.strip()
    if not line.startswith("From "):
        continue
    words = line.split()
    if len(words) >= 2:
        senders[words[1]] = senders.get(words[1], 0) + 1

big_count, big_sender = None, None

for sender, count in senders.items():
    if big_count is None or count > big_count:
        big_count = count
        big_sender = sender

print(big_sender, big_count)


