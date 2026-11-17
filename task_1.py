def caching_fibonacci():
    # Create an empty dictionary to store calculated Fibonacci numbers
    cache = {}

    def fibonacci(n):
        # Check if the input is an integer
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n must be an integer")

        # Return 0 if n is less than or equal to 0
        if n <= 0:
            return 0

        # Return 1 if n equals 1
        if n == 1:
            return 1

        # Check if the result is already stored in the cache
        if n in cache:
            return cache[n]

        # Calculate Fibonacci number using recursion and store it in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        # Return the calculated Fibonacci number
        return cache[n]

    # Return the inner function
    return fibonacci


# Create a Fibonacci function
fib = caching_fibonacci()

# Calculate and print Fibonacci numbers
print(fib(10))  # Output: 55
print(fib(15))  # Output: 610
print(fib(20))  # Output: 6765