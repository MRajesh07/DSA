##--largest Palindrome--
def palindrome(x):
    #x=madam
    newString=""
    for i in range(len(x)-1,-1,-1):
        newString+=x[i]
    if(x==newString):
        return True
    else:
        return False
        
#'efmadamfg'
def largestPalindrome(x):
    largePalin=""
    largestDrome=""
    maxlength=0
    for i in range(0,len(x)):
        largePalin=""
        largePalin+=x[i]
        for j in range(i+1,len(x)):
            largePalin+=x[j]
            if(palindrome(largePalin)):
                if(len(largePalin)>maxlength):
                    largestDrome=largePalin
                    maxlength=len(largePalin)
    return largestDrome
                
        
print(largestPalindrome('fhjhjdfjabcba'))