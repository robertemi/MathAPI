names = ["Lucas", "Nataly", "Megi", "Maria", "Steven"]

scores = [85, 92, 78, 81, 67]

name_score = list(zip(names, scores))
print(name_score)


filtered = [pair for pair in name_score if pair[1] > 80]

sorted_name_score = sorted(filtered, key=lambda pair: pair[1], reverse=True)
print(sorted_name_score)



