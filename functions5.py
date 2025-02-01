def get_permutations(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            remaining = s[:i] + s[i+1:]
            get_permutations(remaining, prefix + s[i])

def print_permutations():
    user_input = input("Enter a string: ")
    get_permutations(user_input)

print_permutations()
