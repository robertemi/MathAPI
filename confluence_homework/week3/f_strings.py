
name = "Alice"
age = 30
balance = 1234.56789
membership_date = "2023-08-12"
status = True

print(f'Hi, my name is {name}, and I am {age} years old')

formatted_balance = f"${balance:>10.2f}"

formatted_date = f"Member since: {membership_date}"

status_sentence = f"Active member: {'Yes' if status else 'No'}"


print(f"Balance: {formatted_balance}")
print(formatted_date)
print(status_sentence)