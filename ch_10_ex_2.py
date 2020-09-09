# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line
# by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# # Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fhandle = open(fname, "r")

hours = dict()

for line in fhandle:
    line = line.strip()
    if not line.startswith("From "):
        continue
    hour = line.split()[-2].split(":")[0]
    hours[hour] = hours.get(hour, 0) + 1

hours_list = list()
for k, v in hours.items():
    hours_list.append((k, v))

hours_list = sorted(hours_list)

for k, v in hours_list:
    print(k, v)
