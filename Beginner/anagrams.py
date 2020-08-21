a=open("words2.txt")
for line in a:
    for word1 in line():
        s1=str(word1)
        print s1
        for word2 in line():
            s2=str(word2)
            if(sorted(s1)==sorted(s2)):
                print(word1,word2)



