sentence = 'Python is fun because Python is powerful'
target_word = 'Python'
new_word = 'Programming'

def replace_word(sentence, target, new):
    new_sentence = []
    
    for word in sentence.split():
        if word == target:
            word = new
        new_sentence.append(word)    

    return str(new_sentence)

print(replace_word(sentence, target_word, new_word))