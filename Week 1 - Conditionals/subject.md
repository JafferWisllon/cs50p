# CS50P – Introduction to Programming with Python  
## Lecture: Conditionals (Complete Summary)

---

## 1. What Are Conditionals?

- **Conditionals** allow programs to make decisions.
- They control which parts of the code run based on whether a condition is:
  - `True`
  - `False`
- In Python, conditionals are implemented using:
  - `if`
  - `elif`
  - `else`

Conditionals are essential for writing programs that react to user input and changing data.

---

## 2. Boolean Expressions

- A **Boolean expression** evaluates to either `True` or `False`.
- They are the foundation of conditionals.

### Common Comparison Operators

| Operator | Meaning |
|--------|--------|
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

### Example
```python
x = 10
x > 5    # True
x == 3   # False
```

## 3. Basic if Statements
- The if keyword checks a condition.
- If the condition is True, the indented block executes.

Example
```python
if x > 0:
    print("x is positive")
```

Important Rules

- Indentation is required in Python.
- A colon (`:`) starts the conditional block.

## 4. if / else Statements

- else runs when the if condition is False.
- Ensures that one of two paths always executes.

Example
```python
if x > 0:
    print("Positive")
else:
    print("Not positive")
```

## 5. Multiple Conditions with elif

- elif means else if
- Used when more than two outcomes are possible.

Example
```python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```
Python checks conditions top to bottom and stops at the first True.

## 6. Logical Operators

Python allows combining conditions using logical operators:

- and → all conditions must be True
- or → at least one condition must be True
- not → reverses a condition

Example
```python
if x >= 0 and x <= 100:
    print("Valid value")
```

## 7. Using input() with Conditionals

- input() always returns a string
- Numeric comparisons require type conversion.

Example
```python
age = int(input("Age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Failing to convert input can cause logic errors or crashes.

## 8. Comparing Strings

- Strings can be compared using ==
- Comparisons are case-sensitive by default.

Example
```python
answer = input("Yes or no? ")

if answer == "yes":
    print("Confirmed")
```

Improving Robustness

```python
answer = answer.lower()

if answer == "yes":
    print("Confirmed")
```

## 9. Equality (==) vs Assignment (=)

- = assigns a value to a variable
- == compares two values

⚠️ A very common beginner mistake.

Incorrect
```python
if x = 5:
```
Correct
```python
if x == 5:
```

## 10. Chained Comparisons

Python allows chaining comparisons for cleaner logic.

Example
```python
if 0 <= x <= 100:
    print("Valid score")
```

Equivalent to:
```python
if x >= 0 and x <= 100:
```

## 11. Style and Readability

CS50P emphasizes:
- Clear logic
- Readable conditionals
- Avoiding unnecessary nesting

Example
```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

Readable code is easier to debug and maintain.

## 12. Common Pitfalls
- Forgetting indentation
- Using = instead of ==
- Not converting input types
- Writing overly complex nested conditionals

## 13. Key Takeaways
- Conditionals control program flow
- Boolean expressions drive decisions
- Python syntax prioritizes readability
- Clean conditionals reduce bugs
- Conditionals are foundational for:
  - Loops
  - Functions
  - Real-world applications