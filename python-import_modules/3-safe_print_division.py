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
        if 'result' in locals():
            print("{} / {} = {}".format(a, b, result) if b != 0 else "{} / {} = None".format(a, b))
        else:
            print("{} / {} = None".format(a, b))

