import re

with open("dict.txt") as f:
    words = f.read().splitlines()

s = [re.sub("[^a-zA-Z]", "", ''.join(sorted(words[i].lower()))) for i in range(len(words))]

fs = s[0]
fw = words[0]

m = {s[0] : [words[0]]}

for i in range(1, len(s)):
    if s[i] in m.keys():
        m[s[i]].append(words[i])
    else:
        m[s[i]] = [words[i]]

with open("sorted-lookup.txt", "w") as f:
    for k in sorted(m):
        f.write(k + " " + " ".join(m[k]) + "\n")
