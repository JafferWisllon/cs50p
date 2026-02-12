output = ""

for letter in input("Input: "):
    if letter.lower() in "aeiou":
        continue
    output += letter

print(output)