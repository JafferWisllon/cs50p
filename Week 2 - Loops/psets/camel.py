camel = input("camelCase: ")
snake = ""

for index, i in enumerate(camel):
    if i.isupper():
        if index != 0:
            snake += "_"
        snake += i.lower()
    else:
        snake += i

print(snake)