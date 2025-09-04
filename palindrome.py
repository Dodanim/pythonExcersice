#The program solves the palindome issue
#First we have  list with some words

def is_palindrome_sensitive(s: str) ->  bool:
    #it ignores spaces
    s_clean = s.replace(" ", "")
    #normalize Capital letters and lowcases
    s_clean = s_clean.casefold()
    #compare overwise string
    return s_clean == s_clean[::-1]

randomWords = ["A toyota", "Dennis sinned" , "This is a palindrome"]
#
for word in randomWords:
    if(is_palindrome_sensitive(word)):
        print(word, "-> is palindrome" )
    else:
        print(word, "-> is not palindrome" )


