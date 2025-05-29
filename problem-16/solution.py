from functools import lru_cache  # Importing the LRU (Least Recently Used) cache decorator

@lru_cache(maxsize=None)  # This will cache all results of the function to avoid redundant calculations
def fibonacci(n):
    """
    Recursive function to compute Fibonacci numbers using memoization.
    
    Parameters:
    n (int): The position in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.
    """
    # Base case 1: F(0) = 0
    if n == 0:
        return 0
    # Base case 2: F(1) = 1
    elif n == 1:
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Input from the user
user_input = int(input("Enter the number: "))

# Output the result
print(f"Fibonacci({user_input}) =", fibonacci(user_input))
