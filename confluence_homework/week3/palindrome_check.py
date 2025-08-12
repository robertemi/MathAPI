def check_palindrome(word: str):
    return word == word[::-1]

print(check_palindrome('level'))