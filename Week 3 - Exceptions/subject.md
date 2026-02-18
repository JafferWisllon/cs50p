# CS50P – Week 3: Exceptions

## Overview

This lecture introduces **exceptions** in Python — mechanisms that allow programs to handle runtime errors gracefully instead of crashing.

### Main Goals

- Understand the difference between syntax and runtime errors  
- Learn how to use `try` and `except`  
- Handle invalid user input safely  
- Write more defensive and professional code  
- Refactor error handling into reusable functions  

---

## 1. Syntax Errors vs Runtime Errors

### Syntax Errors

- Caused by incorrect Python syntax  
- Prevent the program from running  
- Must be fixed before execution  

Example:

```python
print("hello
```
Error:
```bash
SyntaxError: unterminated string literal
```

Runtime Errors (Exceptions)

- Occur while the program is running
- Often caused by unexpected user input
- Can be handled using exception handling

Example:
```python
x = int(input("What's x? "))
```

If the user types:
```bash
cat
```
Python raises:
```bash
ValueError: invalid literal for int() with base 10: 'cat'
```

### 2. Handling Exceptions with try and except
Basic structure:
```python
try:
    # code that might fail
except SomeError:
    # handle the error
```
Example:
```python
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```

Key Ideas

- Only catch exceptions you expect
- Be specific (ValueError, not just Exception)
- Prevent your program from crashing

### 3. ValueError and NameError
ValueError
Occurs when a function receives a value of the correct type but invalid content.

Example:
```python
int("cat")
```

NameError
Occurs when a variable is used before being defined.

Example:
```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")  # Might cause NameError
```
If conversion fails, x is never assigned.

### 4. Using else with try/except
Python allows:
```python
try:
    ...
except ValueError:
    ...
else:
    ...
```
The else block runs only if no exception occurs.

Example:
```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```
This ensures safe variable usage.

### 5. Re-Prompting the User with Loops
Instead of exiting after invalid input:
```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
```
Concepts Used
- while True → infinite loop
- break → exits loop
- Defensive programming improves UX

### 6. Using pass
pass allows you to ignore an exception silently.

Example:
```python
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        pass
```
This avoids error messages while still retrying.

### 7. Creating a Reusable Function

Instead of repeating logic:
```python
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass
```

Using it:
```python
def main():
    x = get_int()
    print(f"x is {x}")

main()
```

This improves:
- Reusability
- Abstraction
- Code organization

### 8. Making the Function More Flexible
Add a parameter:
```python
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
```

Now it can be reused:
```python
x = get_int("What's x? ")
```

### 9. Python Philosophy: EAFP

Python often follows:
EAFP — Easier to Ask Forgiveness than Permission

Instead of checking first:
```python
if s.isnumeric():
    x = int(s)
```

Python prefers:
```python
try:
    x = int(s)
except ValueError:
    ...
```

Try it first, handle failure if necessary

### 10. Indentation and Structure

Indentation defines:
- Function scope
- Loop scope
- try/except structure
- Program logic

Python enforces indentation strictly for readability and clarity.

### 11. Keywords Learned

| Keyword  | Purpose |
|-----------|----------|
| `try`     | Attempt to execute code that might raise an exception |
| `except`  | Catch and handle a specific exception |
| `else`    | Execute code only if no exception occurs in the `try` block |
| `pass`    | Do nothing (used as a placeholder) |
| `break`   | Exit a loop immediately |
| `return`  | Exit a function and optionally send back a value |
