def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    fib_sequence = list(fibonacci(n))
    print("Fibonacci sequence:", fib_sequence)

if __name__ == "__main__":
    main()
