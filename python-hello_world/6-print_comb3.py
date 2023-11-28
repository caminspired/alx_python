for i in range (90):
    if i < 89:
        if str(i)[-1] > str(i)[0]:
            print("{:02d}".format(i), end=", ")
        else:
            continue
    else:
        print("{:02d}".format(i))                   
