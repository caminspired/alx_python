import sys 

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_arg = len(argv)
    
for i, arg in enumerate(argv, start=1):
    if num_arg == 0:
        print("{} arguments:".format(num_arg))
        
    elif num_arg == 1:
        print("{} argument:".format(num_arg))
        print("{}: {}".format(i, arg))
        
    else:
        print("{} arguments:".format(num_arg))
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))
