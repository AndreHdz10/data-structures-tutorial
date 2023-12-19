# Stack

## Introduction to Stacks

Imagine organizing a pile of books: the last book you place becomes the first one you remove. That's the essence of a stack in computer science—Last-In, First-Out (LIFO). Stacks manage data just like this, enabling operations like push (adding an element) and pop (removing the most recently added element).

![Stack of Books](<Images/stack of books.jpg>)

## Implementing a Stack in Python

In Python, you can create a stack using a list:

```Python

#Stack implementation in python


# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))


```

![Stack Example](Images/stack-operations.jpg)

## Problem Example - Checking Balanced Parentheses

Stacks are great for checking balanced parentheses:

## Problem:

Write a function to check if a string of parentheses is balanced.

```python

def is_balanced(parentheses):
    stack = []  # Initialize an empty stack to track open parentheses
    for char in parentheses:
        if char == '(':  # If the character is an opening parenthesis
            stack.append(char)  # Push it onto the stack
        elif char == ')':  # If the character is a closing parenthesis
            # Check if the stack is empty or the top of the stack does not match the closing parenthesis
            if not stack or stack.pop() != '(':
                return False  # If it doesn't match or the stack is empty, the parentheses are unbalanced
    return not stack  # If the stack is empty at the end, parentheses are balanced

# Example usage:
expression = "((()))"
print(is_balanced(expression))  # Output: True


```

## Challenge Problem - Reverse a String Using a Stack

Here's a challenge for you:

Write a function to reverse a string using a stack. Here's the [solution](./solutions.py).

Feel free to try the challenge problem! If you need guidance, the solution is available for reference.

### Go back to [welcome](./0-welcome.md) page
