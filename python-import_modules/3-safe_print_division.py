def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    except Exception as e:
        print("Inside result: None")
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("{:d} / {:d} = {}".format(a, b, result) if 'result' in locals() else "{:d} / {:d} = None".format(a, b))
