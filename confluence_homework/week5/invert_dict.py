grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Diana": "C"
}

def invert_dict(dictionary):
    inverted_dict = {}
    for key, value in dictionary.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict

print(invert_dict(grades))