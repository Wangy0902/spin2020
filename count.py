fname = "README.md"
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1

print("total lines in README: ", count)