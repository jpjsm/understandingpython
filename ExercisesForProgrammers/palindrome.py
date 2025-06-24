#Checks id string is palindrome

def IsPalindrome(text):
    length = len(text)
    lenhalf = int(length/2)
    for i in range(0,lenhalf):
        if (text[i] != text[length - (i + 1)]):
            return False
    return True

def IsAlmostPalindrome(text):
    length = len(text)
    halflen = int(length/2)
    # print "length: {0}. halflen: {1}".format(length, halflen)
    for i in range(0,halflen):
        # print "Comparing {0} to {1}.".format(text[i], text[length - (i + 1)])
        if (text[i] != text[length - (i + 1)]):
            #print "OptionA: {0}".format(text[(i):(length - (i + 1))])
            #print "OptionB: {0}".format(text[(i+1):(length - (i))])
            return IsPalindrome(text[(i):(length - (i + 1))]) or IsPalindrome(text[(i + 1):(length - (i))])
    return True
