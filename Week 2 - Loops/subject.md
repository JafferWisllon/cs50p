# CS50P — Week 2  
## Loops  
### Conceptual Summary

---

## 1. Purpose of Loops

Loops allow a program to **repeat instructions** without duplicating code.

Instead of writing the same statement multiple times, loops enable:
- cleaner code
- better scalability
- easier maintenance

Loops are fundamental for automation and dynamic behavior.

---

## 2. `while` Loops

A `while` loop runs **as long as a condition is true**.

Conceptually:
- Check a condition
- If true → execute the block
- Repeat
- Stop when the condition becomes false

Key idea:
> A `while` loop depends on a changing condition.

If the condition never becomes false, the program results in an **infinite loop**.

---

## 3. Infinite Loops

An infinite loop occurs when:
- the condition always remains true
- there is no state change inside the loop

Example scenario:
- forgetting to update a counter variable
- using `while True` without a `break`

Infinite loops are sometimes intentional but must be controlled carefully.

---

## 4. `break` Statement

The `break` statement:
- immediately exits a loop
- overrides the loop’s condition

It is commonly used:
- in input validation
- when waiting for a specific condition
- inside `while True` loops

---

## 5. `for` Loops

A `for` loop is used when:
- the number of iterations is known
- iterating over a sequence

Conceptually:
> A `for` loop repeats a block a specific number of times.

It is generally more concise and safer than manually managing counters in a `while` loop.

---

## 6. The `range()` Function

`range()` generates a sequence of numbers.

Common patterns:
- `range(n)` → 0 up to (but not including) n
- `range(start, stop)`
- `range(start, stop, step)`

Important concept:
> The stop value is not included.

This reinforces understanding of boundaries and indexing.

---

## 7. Iteration Over Strings

Python allows looping directly over characters in a string.

Example conceptually:
- Each iteration processes one character at a time

This demonstrates:
- Python’s high-level abstraction
- automatic iteration over sequences

---

## 8. Input Validation with Loops

Loops are often used to:
- repeatedly ask for input
- validate user data
- ensure correct format

Pattern introduced:
- keep asking until input meets a condition
- use `break` to exit when valid

This shows loops as a **control mechanism**, not just repetition.

---

## 9. Indentation and Structure

Python uses indentation to define:
- loop bodies
- scope
- control flow

Incorrect indentation can:
- change logic
- cause syntax errors
- create unintended behavior

Indentation is not optional — it defines structure.

---

## 10. Nested Loops

Loops can exist inside other loops.

This allows:
- multi-level repetition
- grid-like behavior
- pattern generation

Nested loops increase complexity and require careful reasoning.

---

## 11. Loop Variables and Scope

Loop variables:
- are assigned values each iteration
- change automatically in `for` loops
- must be updated manually in `while` loops

Understanding how loop variables evolve is essential to avoid logical errors.

---

## 12. Choosing Between `while` and `for`

Use `while` when:
- repetition depends on a condition
- the number of iterations is unknown

Use `for` when:
- iterating a fixed number of times
- iterating over a sequence

Choosing correctly improves readability and reduces bugs.

---

## 13. Common Logical Errors

Typical loop mistakes:
- forgetting to update the counter
- off-by-one errors
- incorrect loop boundaries
- infinite loops

Debugging loops requires tracking:
- the condition
- the state change
- the termination condition

---
