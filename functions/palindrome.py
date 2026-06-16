def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()
#
# word = input("enter a word: ")
# if is_palindrome(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))
#--------------------------------------------------------

def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    #return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


word = input("enter a word: ")
if palindrome_sentence(word):
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))
