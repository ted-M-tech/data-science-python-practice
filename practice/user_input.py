# --- input text ---
input_text = input()
vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for i in input_text:
    if i in vowels:
        count += 1

print(f'{count}')

# PIN check
import re

input_PIN = input()
patterns = r"^\d{4}$"

if re.match(patterns, input_PIN):
    print("PIN accepted")
else:
    print("invalid PIN")
