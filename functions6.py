def reverse_sentence():
    user_input = input("Enter a sentence: ")
    words = user_input.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

reversed_sentence = reverse_sentence()
print(reversed_sentence)

