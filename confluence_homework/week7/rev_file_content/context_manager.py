logs = []

with open('log.txt', 'r') as f:
    logs = [line.strip() for line in f]
    f.seek(0)

with open('reversed_log.txt', 'w') as f:
    f.writelines(reversed(logs))