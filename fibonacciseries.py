def fibonacci(n):
   
    fib_sequence = [0, 1]
    
    for i in range(2, n):

        next_number = fib_sequence[-1] + fib_sequence[-2]

        fib_sequence.append(next_number)
    
    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))

print(f"Fibonacci sequence of {n} numbers:", fibonacci(n))
