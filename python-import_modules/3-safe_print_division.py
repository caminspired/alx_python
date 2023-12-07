def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return None
    except Exception as e:
        print("Inside result: {}".format(None))
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        if 'result' in locals():
            print("{} / {} = {}".format(a, b, result) if b != 0 else "{} / {} = {}".format(a, b, None))
        else:
            print("{} / {} = {}".format(a, b, None))

# Example usage:
result1 = safe_print_division(10, 2)
result2 = safe_print_division(0, 2)
a = 10
b = -2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
