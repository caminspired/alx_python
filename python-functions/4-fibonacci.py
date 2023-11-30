def fibonacci_sequence(n):
    if n <= 2:
        return [0, 1][:n]
    fib_seq = fibonacci_sequence(n - 1)
    fib_seq.append(sum(fib_seq[-2:]))
    return fib_seq
