# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1


# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# Quick Quiz: Write a program to print the Fibonacci sequence
def print_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Check if the input is valid
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print(a)
    else:
        # Print the first two Fibonacci numbers
        print(a, b, end=" ")

        # Generate and print the remaining Fibonacci numbers
        for _ in range(2, n):
            c = a + b
            print(c, end=" ")
            a, b = b, c

# Get the number of terms from the user
n = int(input("Enter the number of Fibonacci terms to print: "))

# Call the function to print the Fibonacci sequence
print_fibonacci(n)
# 0 1 1 2 3 5 8....
