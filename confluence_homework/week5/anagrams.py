word1 = 'listen'
word2 = 'silent'

def check_anagrams(word1, word2):
    counter_word1 = {}
    counter_word2 = {}

    for letter_word1, letter_word2 in zip(word1, word2):
        if letter_word1 in counter_word1:
            counter_word1[letter_word1] += 1
        else: 
            counter_word1[letter_word1] = 1

        if letter_word2 in counter_word2:
            counter_word2[letter_word2] += 1
        else: 
            counter_word2[letter_word2] = 1

    return counter_word1 == counter_word2

print(check_anagrams(word1, word2))
        