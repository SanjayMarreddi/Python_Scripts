def palindrome(a):
    if a[0]==a[-1]:
        print "True"
    elif a[0] != a[-1]:
        print "False"
    else:
        return palindrome(a[1:-1])

b="1010"
palindrome(b)  
