import re

words = {}
with open("sorted-lookup.txt") as f:
    for line in f:
        lt = line.split()
        words[lt[0]] = lt[1:]

while True:
    k = re.sub("[^a-zA-Z]", "", "".join(sorted(input("Enter in a scrambled word (blank to end): ").lower())))
    if len(k) == 0:
        break
    if not k in words.keys():
        print("Cannot find a match.")
    else:
        print("Found these matches:")
        for w in words[k]:
            print("* ", w)