def Countwordsfromfile():
    fileName = input("Enter the file name: ")
    file = open(fileName,'r')
    words = 0
    for line in file:
        noofwords = line.split()
        words = words + len(noofwords)
    print("Number of words: ")
    print(words)

Countwordsfromfile()