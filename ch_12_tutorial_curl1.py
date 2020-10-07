# Reads in all data in one giant block
import urllib.request

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
# print(img)
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()

# Successive reading in by pieces
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
counter = 0
while True:
    info = img.read(40000)
    counter += 1
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
print("read was executed {} times".format(counter))
fhand.close()
