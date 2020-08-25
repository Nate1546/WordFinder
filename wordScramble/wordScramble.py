def wordfinder ():
    numberOfwords=0
    file=open("word.txt")
    fileLines=file.readlines()
    for line in fileLines:
        words = line.split() 
        numberOfwords = numberOfwords+len(words)
        print(" numberOfwords ")
        print(numberOfwords) 
wordfinder()                   # len is used to find out the length
