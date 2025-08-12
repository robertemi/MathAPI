testing = {"Ana", "Bob", "Charlie", "Diana"}

development = {"Charlie", "Eve", "Frank", "Ana"}

devops = {"George", "Ana", "Bob", "Eve"}

# attemded all 3

attended_all = testing & development & devops
print(attended_all)

# attended only one

def check_attended_one(conf1, conf2, conf3):
    all_attendees = conf1 | conf2 | conf3  # union of all names
    attended_once = []

    for person in all_attendees:
        count = sum([
            person in conf1,
            person in conf2,
            person in conf3
        ])
        if count == 1:
            attended_once.append(person)
    
    return attended_once

print(check_attended_one(testing, development, devops))

# check if all testing also in devops

all_testing_also_in_devops = testing.intersection(devops)
print(all_testing_also_in_devops)

print(all_testing_also_in_devops == devops)

# unique attendees alphabetically

attendees = []
for t, d, dev in zip(testing, development, devops):
    if t not in attendees:
        attendees.append(t)
    if d not in attendees:
        attendees.append(d)
    if dev not in attendees:
        attendees.append(dev)

sorted_attendees = sorted(attendees)

print(sorted_attendees)

# copy
development_copy = development
development = {}
print(development)
print(development_copy)
print(id(development))
print(id(development_copy))