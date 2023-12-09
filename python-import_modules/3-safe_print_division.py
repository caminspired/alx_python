def safe_print_division(a, b):
    result_printed = False  

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
        result_printed = True
        return result
    finally:
        if 'result' in locals() and not result_printed:
            print("{} / {} = {}".format(a, b, result) if b != 0 else "{} / {} = {}".format(a, b, None))
