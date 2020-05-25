fname = "README.md"
count = 0
file_1 = open(fname, 'r')
for line in file_1:
    count += 1
file_1.close()
print("total lines in README: ", count)