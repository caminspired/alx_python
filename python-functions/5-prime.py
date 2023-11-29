def is_prime(number):
    if number < 2:
        return False
    prime = True
    for i in range(2, number):
        if number % i == 0:
            return False
    if prime:
        return True
    else:
        return False
