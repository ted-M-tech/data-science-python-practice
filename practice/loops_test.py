# Python Loops Test – 10
# ----------------------------------------
# 1. Shopping Cart Total
print("No1: Shopping Cart Total")
prices = [3.50, 7.20, 4.99, 12.00, 8.75]

total_price = 0
for price in prices:
    total_price += price
print(f"Total Price is {total_price:.2f}")
# ----------------------------------------
# 2. Format Shopping List
print("\nNo2: Format Shopping List")
groceries = ["bananas", "tomatoes", "chicken", "rice"]
for grocery in groceries:
    print(f"- {grocery}")
# ----------------------------------------
# 3. Count Vowels in User Input
print("\nNo3: Count Vowels in User Input")
user_input = input()
vowels = ["a", "b", "c", "d", "e"]

count = 0
for word in user_input:
    if word in vowels:
        count += 1
print(f'Number of vowels: {count}')
# ----------------------------------------
# 4. Verify 5-Digit PIN
print("\nNo4: Verify 5-Digit PIN")
input_PIN = input('Please input 5-Digit PIN: ')

if len(input_PIN) == 5:
    is_valid = True
    for char in input_PIN:
        if not char.isdigit():
            is_valid = False
            break
    if is_valid:
        print("PIN accepted.")
    else:
        print("Invalid PIN.")
else:
    print("Invalid PIN.")
# ----------------------------------------
# 5. Even Steps Filter
print("\nNo5: Even Steps Filter")
steps = [3450, 6700, 12345, 8000, 4321, 10000]
even_steps = []
for step in steps:
    if step % 2 == 0:
        even_steps.append(step)
print(even_steps)
# ----------------------------------------
# 6. Extract Name Initials
print("\nNo6: Extract Name Initials")
name = "Avery Lee Johnson"
initials = ""
for part in name.split():
    initials += part[0]
print(initials)
# ----------------------------------------
# 7. Palindrome Detector
print("\nNo7: Palindrome Detector")
words = ["madam", "python", "racecar", "hello", "civic", "world"]    

for word in words:
    if word == word[::-1]:
        print(word)
# ----------------------------------------
# 8. Inventory Status
print("\nNo8: Inventory Status")
items = ["pens", "notebooks", "erasers", "highlighters", "staples"]
stock = [15, 0, 7, 0, 30]

item_stocks = zip(items, stock)
for item, stock in item_stocks:
    if stock == 0:
        print(f"Out of stock: {item}")
    else:
        print(f"{stock} left of {item}")
# ----------------------------------------
# 9. Count a Target Word
print("\nNo9: Count a Target Word")
feedback = ["good", "excellent", "good", "okay", "good", "poor", "okay", "good"]
input_word = input("Input word like: good, okay, bad, poor, excellent: ")

count = 0
for word in feedback:
    if word == input_word:
        count += 1

print(f"{input_word} appears {count} time(s).")
# ----------------------------------------
# 10. Reverse Each Word
print("\nNo10: Reverse Each Word")
input_sentence = input("Input sentence: ")
words = input_sentence.split()
reversed_words = []

for word in words:
    reversed_word = word[::-1]
    reversed_words.append(reversed_word)

result_sentence = " ".join(reversed_words)

print(f"\nOriginal sentence: {input_sentence}")
print(f"Reversed sentence: {result_sentence}")