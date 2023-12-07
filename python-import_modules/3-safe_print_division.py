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
            if b != 0:
                print("{} / {} = {}".format(a, b, result))
        else:
            print("{} / {} = None".format(a, b))
