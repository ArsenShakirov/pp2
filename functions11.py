def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

word_or_phrase = input("Enter a word or phrase: ")
print(is_palindrome(word_or_phrase))
