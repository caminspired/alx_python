import sys 

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_arguments = len(argv)
    for i, argument in enumerate(argv, start=1):
        
        if num_arguments == 0:
            print("{} arguments:\n".format(num_arguments))
            
        elif num_arguments == 1:
            print("{} argument:\n".format(num_arguments))
            print("{}: {}".format(i, argument))
            
        else:
            print("{} arguments:\n".format(num_arguments))
            print("{}: {}".format(i, argument))
