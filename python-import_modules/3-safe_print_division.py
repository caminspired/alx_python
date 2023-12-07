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
        print("{} / {} = {}".format(a, b, result) if 'result' in locals() else "{} / {} = {}".format(a, b, None))

