def is_palindrome(s):
    c = []
    for e in s:
        if e.isalnum():
            c.append(e)
    s = ''.join(c).lower()
    return s == s[::-1]

w = input("Enter a word")
print(is_palindrome(w))
