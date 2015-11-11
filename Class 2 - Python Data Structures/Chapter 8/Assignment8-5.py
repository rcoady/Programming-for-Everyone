# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the
# following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the
# person who sent the message). Then print out a count at the end.

fname = raw_input("Enter file name: ")

fh = open(fname)
lst = []

for line in fh:
    line = line.strip()

    if line == '':
        continue
    words = line.split()
    if len(words) == 0:
        continue
    if words[0] != 'From':
        continue
    lst.append(words[1])
    print words[1]

print "There were", len(lst), "lines in the file with From as the first word"
