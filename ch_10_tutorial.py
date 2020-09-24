tt = ['a', 'b', 'c', 'd', 'e']
print(type(tt))
t1 = (1,)
print(type(t1))
print(t1)
t2 = tuple()
print(t2)

t3 = tuple(tt)
print(t3)

t3 = ("A",) + t3[1:]
print(t3)

# Sort words by length
txt = 'but soft what light in yonder window breaks'
words = txt.split()
# print(words)
t = list()
for word in words:
    t.append((len(word), word))
    # print(t)

t.sort(reverse=True)
# print(t)

res = list()
for length, word in t:
    res.append(word)

print(res)

# Tuple assignment
m = ['have', 'fun']
x, y = m
print(x)
print(y)

m.append((x, y))
print(m)

# Swap the values of two variables
x, y = y, x
print(x)
print(y)

# Use tuple assignment to assign values from split-list
addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname, type(uname))
print(domain, type(domain))

# Tuples and dictionaries
d = {'n': 17, 'a': 10, 'b': 1, 'c': 22}
x = list()
for key, val in list(d.items()):
    x.append((val, key))
x.sort(reverse=True)
for val, key in x:
    print(key, val)
